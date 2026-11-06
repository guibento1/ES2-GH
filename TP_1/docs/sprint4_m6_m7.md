# Sprint 4 — M6 (Memento) e M7 (Decorator)

---

## M6 — Memento (Armazenamento de Estado)

### O que é o Memento?

O Memento é um padrão comportamental que permite **guardar e restaurar o estado anterior de um objeto** sem revelar os detalhes da sua implementação. É como tirar uma fotografia ao estado de um objeto num determinado momento — podes sempre voltar a esse momento.

### Analogia do mundo real — Editor de texto

O exemplo mais clássico é o `Ctrl+Z` de um editor de texto. Cada vez que fazes uma alteração, o editor guarda um snapshot do estado anterior. Se quiseres desfazer, restauras o snapshot mais recente.

```
Estado 1: "Olá"         ← snapshot 0
Estado 2: "Olá Mundo"   ← snapshot 1
Estado 3: "Olá Mundo!"  ← snapshot 2 (estado atual)

Ctrl+Z → restaura snapshot 1 → "Olá Mundo"
Ctrl+Z → restaura snapshot 0 → "Olá"
```

### Os três papéis do padrão

| Papel          | Escola          | Teu projeto          | Responsabilidade                                |
| -------------- | --------------- | -------------------- | ----------------------------------------------- |
| **Originator** | `Server`        | `LogConfig`          | Cria e restaura snapshots do seu próprio estado |
| **Memento**    | `Memento`       | `LogConfigMemento`   | Guarda uma cópia imutável do estado             |
| **Caretaker**  | `BackupService` | `LogConfigCaretaker` | Gere o histórico de snapshots                   |

---

### Como funciona no projeto

#### `LogConfigMemento` — o snapshot

Guarda uma cópia do estado do `LogConfig` num momento específico. Os atributos são `final` — depois de criado, o snapshot não pode ser alterado.

```java
public class LogConfigMemento {
    private final LogLevel globalLevel;
    private final List<LogDestination> destinations;
    private final String formatPatterns;

    public LogConfigMemento(LogLevel globalLevel,
                            List<LogDestination> destinations,
                            String formatPatterns) {
        this.globalLevel = globalLevel;
        this.destinations = new ArrayList<>(destinations); // cópia independente!
        this.formatPatterns = formatPatterns;
    }

    public LogLevel getGlobalLevel() { return globalLevel; }
    public List<LogDestination> getDestinations() { return new ArrayList<>(destinations); }
    public String getFormatPatterns() { return formatPatterns; }
}
```

**Porquê `new ArrayList<>(destinations)`?**
Se simplesmente guardasses a referência da lista, quando a lista original fosse alterada o snapshot também mudava — deixava de ser um snapshot. A cópia garante independência total.

---

#### `LogConfig` — o originator

Ganha dois métodos: `backup()` para criar um snapshot e `restore()` para restaurar um.

```java
// Criar um snapshot do estado atual
public LogConfigMemento backup() {
    return new LogConfigMemento(globalLevel, destinations, formatPatterns);
}

// Restaurar a partir de um snapshot
public void restore(LogConfigMemento memento) {
    this.globalLevel    = memento.getGlobalLevel();
    this.destinations   = new ArrayList<>(memento.getDestinations());
    this.formatPatterns = memento.getFormatPatterns();
}
```

---

#### `LogConfigCaretaker` — o gestor do histórico

Gere a lista de snapshots. Não sabe o que está dentro de cada snapshot — apenas os guarda e devolve quando pedido.

```java
public class LogConfigCaretaker {
    private LogConfig logConfig;
    private ArrayList<LogConfigMemento> snapshots = new ArrayList<>();

    public LogConfigCaretaker(LogConfig logConfig) {
        this.logConfig = logConfig;
    }

    public void takeSnapshot() {
        LogConfigMemento m = logConfig.backup();
        snapshots.add(m);
    }

    public void restoreSnapshot(int snapshotNumber) {
        if (snapshotNumber < 0 || snapshotNumber >= snapshots.size()) {
            throw new IndexOutOfBoundsException("Snapshot invalido");
        }
        LogConfigMemento m = snapshots.get(snapshotNumber);
        logConfig.restore(m);
    }
}
```

---

### Exemplo completo de uso

```java
LogConfig config = LogConfig.getInstance();
LogConfigCaretaker caretaker = new LogConfigCaretaker(config);

// Estado inicial: INFO, formato simples
config.setGlobalLevel(LogLevel.INFO);
config.setFormatPatterns("[%level] %message");
caretaker.takeSnapshot(); // snapshot 0

// Alterar para modo debug
config.setGlobalLevel(LogLevel.DEBUG);
config.setFormatPatterns("[%level] %time - %message");
caretaker.takeSnapshot(); // snapshot 1

// Alterar para modo erro
config.setGlobalLevel(LogLevel.ERROR);
System.out.println(config.getGlobalLevel()); // ERROR

// Voltar ao modo debug
caretaker.restoreSnapshot(1);
System.out.println(config.getGlobalLevel()); // DEBUG

// Voltar ao estado inicial
caretaker.restoreSnapshot(0);
System.out.println(config.getGlobalLevel()); // INFO
```

### Porque é importante "sem expor detalhes internos"?

O enunciado diz *"sem expor os detalhes internos da implementação"*. O `LogConfigMemento` só tem getters — ninguém de fora consegue alterar o estado guardado. O `LogConfigCaretaker` nem sequer sabe o que está dentro do `LogConfigMemento` — só o guarda e devolve. Quem sabe criar e interpretar o snapshot é apenas o `LogConfig`.

---

## M7 — Decorator (Extensão de Funcionalidades)

### O que é o Decorator?

O Decorator é um padrão estrutural que permite **adicionar novas responsabilidades a um objeto dinamicamente**, sem modificar a sua classe. É uma alternativa à herança para estender funcionalidades.

A ideia é envolver (wrap) um objeto dentro de outro objeto que acrescenta comportamento, podendo empilhar vários decorators.

### Analogia do mundo real — Café

Imagina que tens um café simples. Podes adicionar leite, açúcar, chantilly — cada um é um decorator que envolve o café e acrescenta algo:

```
Cafe (componente base)
    ↑
ComLeite (decorator)     → adiciona leite ao café
    ↑
ComAcucar (decorator)    → adiciona açúcar ao café com leite
    ↑
ComChantilly (decorator) → adiciona chantilly ao café com leite e açúcar
```

O cliente final paga o preço total — cada decorator adiciona o seu custo ao anterior. Sem alterar a classe `Cafe`.

### Analogia do mundo real — Janela com scrollbars

O exemplo do exercício da escola: uma janela pode ter scrollbar vertical, scrollbar horizontal e contorno. Em vez de criar `JanelaComScrollbarVertical`, `JanelaComScrollbarHorizontal`, etc., empilhas decorators:

```java
Widget w = new Border(new HorizontalSB(new VerticalSB(new Window(80, 24))));
w.draw(); // desenha janela + scrollbar vertical + scrollbar horizontal + contorno
```

### Os papéis do padrão

| Papel                   | Escola                 | Teu projeto         | Responsabilidade                      |
| ----------------------- | ---------------------- | ------------------- | ------------------------------------- |
| **Interface**           | `AuthInterface`        | `LogComponent`      | Contrato comum                        |
| **Componente concreto** | `Auth`                 | `LogEntry`          | Objeto base a decorar                 |
| **Decorator base**      | `Decorator`            | `LogEntryDecorator` | Envolve o componente, delega chamadas |
| **Decorator concreto**  | `Logging`              | `AlertDecorator`    | Adiciona alertas                      |
| **Decorator concreto**  | `CommonWordsValidator` | `MonitorDecorator`  | Adiciona monitorização                |

---

### Como funciona no projeto

#### `LogEntryDecorator` — decorator base (igual ao `Decorator` da escola)

Implementa `LogComponent` e guarda uma referência ao objeto que envolve. Delega todas as chamadas para o objeto envolvido.

```java
public class LogEntryDecorator implements LogComponent {
    protected LogComponent wrapped; // o objeto que está a ser decorado

    public LogEntryDecorator(LogComponent wrapped) {
        this.wrapped = wrapped;
    }

    @Override
    public void log(Logger logger) {
        wrapped.log(logger); // delega para o objeto envolvido
    }

    @Override
    public String getCategory() {
        return wrapped.getCategory();
    }
}
```

---

#### `AlertDecorator` — decorator concreto (igual ao `Logging` da escola)

Acrescenta envio de alertas quando o nível é ERROR, antes de delegar para o objeto envolvido.

```java
public class AlertDecorator extends LogEntryDecorator {
    public AlertDecorator(LogComponent wrapped) {
        super(wrapped);
    }

    @Override
    public void log(Logger logger) {
        if (wrapped instanceof LogEntry) {
            LogEntry entry = (LogEntry) wrapped;
            if (entry.getLevel() == LogLevel.ERROR) {
                System.out.println("ALERTA ADMIN: Erro critico detetado - "
                    + entry.getMessage());
            }
        }
        super.log(logger); // continua a cadeia
    }
}
```

---

#### `MonitorDecorator` — decorator concreto (igual ao `CommonWordsValidator` da escola)

Acrescenta monitorização — regista todos os logs num sistema de monitorização antes de os passar para a frente.

```java
public class MonitorDecorator extends LogEntryDecorator {
    public MonitorDecorator(LogComponent wrapped) {
        super(wrapped);
    }

    @Override
    public void log(Logger logger) {
        if (wrapped instanceof LogEntry) {
            LogEntry entry = (LogEntry) wrapped;
            System.out.println("MONITOR: [" + entry.getLevel()
                + "] " + entry.getMessage());
        }
        super.log(logger); // continua a cadeia
    }
}
```

---

### Exemplo completo de uso

```java
// Componente base
LogComponent entry = LogEntryFactory.create(LogLevel.ERROR, "Falha critica na BD");

// Empilhar decorators — igual ao exercício da escola
LogComponent decorated = new AlertDecorator(new MonitorDecorator(entry));

// Ao chamar log(), a cadeia executa:
// 1. AlertDecorator.log() → envia alerta
// 2. MonitorDecorator.log() → regista no monitor
// 3. LogEntry.log() → loga normalmente
decorated.log(logger);
```

**Output:**

```
ALERTA ADMIN: Erro critico detetado - Falha critica na BD
MONITOR: [ERROR] Falha critica na BD
[ERROR] 1774548077502 - Falha critica na BD
```

---

### Porquê Decorator e não herança?

O enunciado diz *"sem necessidade de modificar a estrutura principal do sistema"*. Com herança terias de criar:

```
LogEntryComAlerta
LogEntryComMonitor
LogEntryComAlertaEMonitor  ← explosão de classes!
```

Com Decorator combinas em runtime sem tocar nas classes existentes:

```java
new AlertDecorator(entry)                        // só alerta
new MonitorDecorator(entry)                      // só monitor
new AlertDecorator(new MonitorDecorator(entry))  // ambos
```

---

## Comparação M6 vs M7

|                    | M6 — Memento                     | M7 — Decorator                        |
| ------------------ | -------------------------------- | ------------------------------------- |
| Tipo               | Comportamental                   | Estrutural                            |
| Objetivo           | Guardar e restaurar estado       | Adicionar comportamento dinamicamente |
| Sem alterar o quê? | Detalhes internos do `LogConfig` | Estrutura principal do `LogEntry`     |
| Chave              | `backup()` / `restore()`         | Empilhar wrappers                     |
| Analogia           | `Ctrl+Z` do editor               | Café com leite e açúcar               |
