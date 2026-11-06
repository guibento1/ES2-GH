# Sprint 3 — M4 (Composite) e M5 (Object Pool)

---

## M4 — Composite (Estruturação de Registos)

### O que é o Composite?

O Composite é um padrão estrutural que permite **executar operações num objeto sem lidar diretamente com a hierarquia de objetos**. Utiliza composição recursiva numa estrutura em árvore de objetos relacionados hierarquicamente, permitindo processar objetos primitivos (folhas) e compósitos (grupos) da mesma forma.

Enquanto os objetos primitivos são indivisíveis, os objetos compósitos podem ser decompostos em outros compósitos ou objetos primitivos.

---

### Analogia do mundo real — Escola

Uma escola é um exemplo de um compósito que pode ser dividido em outros compósitos:

```
Escola                  ← composite
└── Departamento TI     ← composite
    └── Curso Java      ← composite
        ├── Aluno A     ← folha (indivisível)
        └── Aluno B     ← folha (indivisível)
```

Podes chamar `getInfo()` na escola e ela propaga por departamentos, cursos e alunos automaticamente — sem distinguir quem é compósito e quem é folha.

### Analogia do mundo real — Sistema de ficheiros

```
/home                  ← composite (pasta)
├── documento.txt      ← folha (ficheiro)
└── projetos/          ← composite (pasta)
    ├── main.java      ← folha (ficheiro)
    └── src/           ← composite (pasta dentro de composite)
        └── App.java   ← folha (ficheiro)
```

### Analogia do mundo real — Exército

```
Exército               ← composite
└── Divisão Norte      ← composite
    ├── Brigada A      ← composite
    │   ├── Soldado    ← folha
    │   └── Soldado    ← folha
    └── Brigada B      ← composite
```

Uma ordem dada ao exército propaga até ao último soldado sem o general precisar de saber quantos níveis existem.

---

### Os papéis do padrão

| Papel                           | Diagrama da aula        | Exercício da escola | Teu projeto                |
| ------------------------------- | ----------------------- | ------------------- | -------------------------- |
| **Componente** (contrato comum) | `Component` (interface) | `Menu` (abstrata)   | `LogComponent` (interface) |
| **Folha** (elemento individual) | `Leaf`                  | `Link`              | `LogEntry`                 |
| **Composite** (grupo)           | `Composite`             | `SubMenu`           | `LogGroup`                 |

---

### Exercício da escola explicado

#### `Menu` — componente base (classe abstrata)

Define o contrato comum para folhas e grupos. No exercício da escola é uma **classe abstrata** em vez de interface porque tem atributos e implementação partilhada (`label`, `getLabel()`, `setLabel()`).

```java
public abstract class Menu {
    private String label;

    public Menu(String label) {
        this.label = label;
    }

    public String getLabel() { return label; }
    public void setLabel(String label) { this.label = label; }

    public abstract void showOptions(); // contrato comum
}
```

#### `Link` — folha (elemento individual)

É o elemento primitivo e indivisível. Tem um URL e quando `showOptions()` é chamado, mostra o label e o URL. Não tem filhos.

```java
public class Link extends Menu {
    private String URL;

    public Link(String label, String URL) {
        super(label);
        this.URL = URL;
    }

    @Override
    public void showOptions() {
        System.out.println(getLabel()); // faz o trabalho real
        System.out.println(getURL());
    }
}
```

#### `SubMenu` — composite (grupo)

Pode conter outros `Menu` — tanto `Link` (folhas) como outros `SubMenu` (composites). Quando `showOptions()` é chamado, propaga para todos os filhos.

```java
public class SubMenu extends Menu {
    private List<Menu> children;

    public void addChild(Menu child) {
        children.add(child);
    }

    public void removeChild(Menu child) {
        children.remove(child);
    }

    @Override
    public void showOptions() {
        System.out.println(getLabel());
        for (Menu child : children) {
            child.showOptions(); // propaga para todos os filhos
        }
    }
}
```

#### Exemplo de uso na escola

```java
// Estrutura de menu HTML
SubMenu principal = new SubMenu("Menu Principal");

SubMenu sobre = new SubMenu("Sobre");
sobre.addChild(new Link("Historia", "https://site.com/historia"));
sobre.addChild(new Link("Equipa",   "https://site.com/equipa"));

SubMenu contactos = new SubMenu("Contactos");
contactos.addChild(new Link("Email", "https://site.com/email"));

principal.addChild(sobre);
principal.addChild(contactos);
principal.addChild(new Link("Home", "https://site.com"));

// O cliente trata tudo da mesma forma
principal.showOptions(); // propaga por toda a árvore
```

---

### Como funciona no projeto — M4

A diferença principal em relação à escola é que o teu projeto usa uma **interface** (`LogComponent`) em vez de classe abstrata, porque `LogEntry` já tem os seus próprios atributos e implementação — não precisas de os repetir no componente base.

#### `LogComponent` — interface comum

```java
public interface LogComponent {
    void log(Logger logger);
    String getCategory();
}
```

#### `LogEntry` — folha

Já existia no projeto. Passou a implementar `LogComponent` ganhando `log()` e `getCategory()`.

```java
public abstract class LogEntry implements LogComponent {
    // atributos e getters existentes...

    @Override
    public void log(Logger logger) {
        logger.log(this); // faz o trabalho real — é uma folha
    }

    @Override
    public String getCategory() {
        return getLevel().name();
    }
}
```

#### `LogGroup` — composite

Equivalente ao `SubMenu` da escola. Agrupa `LogComponent` e propaga o `log()` para todos os filhos.

```java
public class LogGroup implements LogComponent {
    private String category;
    private List<LogComponent> components = new ArrayList<>();

    public LogGroup(String category) {
        this.category = category;
    }

    public void add(LogComponent log) {
        components.add(log);
    }

    public void remove(LogComponent log) {
        components.remove(log);
    }

    @Override
    public void log(Logger logger) {
        for (LogComponent component : components) {
            component.log(logger); // propaga para todos os filhos
        }
    }

    @Override
    public String getCategory() {
        return category;
    }
}
```

---

### Comparação escola → projeto

| Escola            | Projeto                    | Papel                            |
| ----------------- | -------------------------- | -------------------------------- |
| `Menu` (abstrata) | `LogComponent` (interface) | Contrato comum                   |
| `Link`            | `LogEntry`                 | Folha — elemento individual      |
| `SubMenu`         | `LogGroup`                 | Composite — agrupa e propaga     |
| `addChild()`      | `add()`                    | Adicionar ao grupo               |
| `removeChild()`   | `remove()`                 | Remover do grupo                 |
| `showOptions()`   | `log(Logger)`              | Operação que propaga pela árvore |
| `children`        | `components`               | Lista de filhos                  |

---

### Exemplo de uso no Main

```java
// Criar grupos por categoria — igual aos SubMenu da escola
LogGroup autenticacao = new LogGroup("Autenticacao");
LogGroup baseDeDados  = new LogGroup("Base de Dados");
LogGroup interfacee   = new LogGroup("Interface");
LogGroup rede         = new LogGroup("Rede");

// Adicionar folhas — igual aos Link da escola
autenticacao.add(LogEntryFactory.create(LogLevel.INFO,    "Login com sucesso"));
autenticacao.add(LogEntryFactory.create(LogLevel.WARNING, "Mude a pass de mes a mes"));
autenticacao.add(LogEntryFactory.create(LogLevel.ERROR,   "Credenciais incorretas"));
autenticacao.add(LogEntryFactory.create(LogLevel.DEBUG,   "Modo debug ativado"));

baseDeDados.add(LogEntryFactory.create(LogLevel.ERROR, "Ligacao perdida"));
interfacee.add(LogEntryFactory.create(LogLevel.INFO,   "Interface carregada"));
rede.add(LogEntryFactory.create(LogLevel.WARNING,      "Latencia elevada"));

// Grupos dentro de grupos — igual aos SubMenu dentro de SubMenu da escola
LogGroup sistema = new LogGroup("Sistema");
sistema.add(autenticacao);
sistema.add(baseDeDados);
sistema.add(interfacee);
sistema.add(rede);

// O cliente trata tudo da mesma forma
sistema.log(logger); // propaga por toda a árvore
```

---

## M5 — Object Pool (Otimização de Recursos)

### O que é o Object Pool?

O Object Pool é um padrão de criação que define o design de uma **pool de objetos reutilizáveis**. A criação de pools de objetos é uma prática popular para aumentar a eficiência de aplicações onde o custo e a frequência de instanciação de classes são elevados e o número de objetos a ser utilizados é pequeno.

A eficiência é assegurada pela **reutilização de objetos já existentes** na pool. Um processo pode reutilizar objetos da pool quando estes já não forem utilizados por nenhum outro processo.

Para garantir uma política de criação de objetos coerente, a classe que implementa a pool deve ser **Singleton**.

---

### Analogia do mundo real — Biblioteca

Uma biblioteca tem um número limitado de salas de estudo. Em vez de construir uma sala nova para cada estudante:

```
Pool de Salas
├── Sala 1 → DISPONÍVEL
├── Sala 2 → EM USO (João)
└── Sala 3 → DISPONÍVEL

João termina  → Sala 2 volta a DISPONÍVEL
Maria pede    → Sala 1 passa a EM USO (Maria)
```

### Analogia do mundo real — Armazém de escritório

Quando um novo funcionário é contratado, o gestor verifica se há equipamento disponível no armazém. Se houver usa-o, se não encomenda novo. Quando um funcionário sai, o equipamento volta ao armazém.

```
Armazém (Pool)
├── Computador A → DISPONÍVEL
├── Computador B → EM USO (Maria)

acquire() → Computador A sai do armazém
release() → Computador volta ao armazém
```

---

### Os papéis do padrão

| Papel                   | Diagrama da aula | Exercício da escola | Teu projeto          |
| ----------------------- | ---------------- | ------------------- | -------------------- |
| **Pool** (Singleton)    | `ReusablePool`   | `ReusablePool`      | `LogDestinationPool` |
| **Objeto reutilizável** | `Reusable`       | `HttpURLConnection` | `LogDestination`     |

---

### Exercício da escola explicado

#### `ReusablePool` — pool Singleton com criação dinâmica

Na escola o `ReusablePool` é também um **Singleton** (combina dois padrões) e tem lógica mais avançada — cria novos objetos quando o pool está vazio, até um máximo de `maxSize`. Também é **thread-safe** com `synchronized`.

```java
public class ReusablePool {
    private static ReusablePool instance;
    private List<HttpURLConnection> inUse;
    private List<HttpURLConnection> available;
    private int maxSize = 10; // máximo de conexões

    private ReusablePool() {
        available = new ArrayList<>();
        inUse = new ArrayList<>();
    }

    // Singleton + thread-safe
    public static synchronized ReusablePool getInstance() {
        if (instance == null) {
            instance = new ReusablePool();
        }
        return instance;
    }

    // Cria nova conexão se necessário
    private HttpURLConnection createConnection() {
        try {
            URL url = new URL("https://www.ipv.pt");
            return (HttpURLConnection) url.openConnection();
        } catch (Exception e) { return null; }
    }

    public synchronized HttpURLConnection acquire() throws PoolExhaustedException {
        if (!available.isEmpty()) {
            // reutiliza existente
            HttpURLConnection conn = available.remove(available.size() - 1);
            inUse.add(conn);
            return conn;
        } else if (inUse.size() < maxSize) {
            // cria novo se ainda não atingiu o máximo
            HttpURLConnection conn = createConnection();
            inUse.add(conn);
            return conn;
        } else {
            throw new PoolExhaustedException(); // pool esgotado
        }
    }

    public synchronized void release(HttpURLConnection conn)
            throws ObjectNotFoundException {
        boolean found = false;
        for (int i = 0; i < inUse.size(); i++) {
            if (inUse.get(i) == conn) {
                inUse.remove(i);
                found = true;
                break;
            }
        }
        if (!found) throw new ObjectNotFoundException();
        available.add(conn);
    }
}
```

**Diferenças face ao teu projeto:**

| Escola (`ReusablePool`)          | Teu projeto (`LogDestinationPool`)    |
| -------------------------------- | ------------------------------------- |
| Singleton (`getInstance()`)      | Não é Singleton (instanciado no Main) |
| Cria novos objetos se necessário | Só usa os que foram inicializados     |
| `maxSize` configurável           | Sem limite máximo                     |
| Thread-safe (`synchronized`)     | Não thread-safe                       |
| `PoolExhaustedException`         | `RuntimeException`                    |
| `ObjectNotFoundException`        | Sem verificação                       |

---

### Como funciona no projeto — M5

O `LogDestinationPool` é uma versão mais simples do `ReusablePool` da escola — sem Singleton, sem criação dinâmica, sem thread-safety — adequado para o nível do sprint.

```java
public class LogDestinationPool {
    private List<LogDestination> available = new ArrayList<>(); // disponíveis
    private List<LogDestination> inUse     = new ArrayList<>(); // em uso

    public LogDestinationPool(List<LogDestination> initial) {
        available.addAll(initial); // inicializa com destinos já criados
    }

    public LogDestination acquire() {
        if (available.isEmpty()) {
            throw new RuntimeException("Sem destinos disponiveis no pool");
        }
        LogDestination destination = available.remove(0); // retira dos disponíveis
        inUse.add(destination);                           // coloca em uso
        return destination;
    }

    public void release(LogDestination destination) {
        inUse.remove(destination);   // retira dos em uso
        available.add(destination);  // devolve aos disponíveis
    }

    public int availableCount() { return available.size(); }
    public int inUseCount()     { return inUse.size(); }
}
```

---

### Comparação escola → projeto

| Escola                   | Projeto              | Papel                        |
| ------------------------ | -------------------- | ---------------------------- |
| `ReusablePool`           | `LogDestinationPool` | Gestor do pool               |
| `HttpURLConnection`      | `LogDestination`     | Objeto reutilizável          |
| `acquire()`              | `acquire()`          | Requisitar objeto do pool    |
| `release()`              | `release()`          | Devolver objeto ao pool      |
| `available`              | `available`          | Lista de objetos disponíveis |
| `inUse`                  | `inUse`              | Lista de objetos em uso      |
| `PoolExhaustedException` | `RuntimeException`   | Erro quando pool vazio       |

---

### Exemplo de uso no Main

```java
// Criar pool com destinos já instanciados
LogDestinationPool pool = new LogDestinationPool(Arrays.asList(
    new FileDestination("src/main/java/pool_logs_1.txt"),
    new FileDestination("src/main/java/pool_logs_2.txt")
));

System.out.println("Disponiveis: " + pool.availableCount()); // 2

// Adquirir do pool
LogDestination dest = pool.acquire();
System.out.println("Disponiveis: " + pool.availableCount()); // 1
System.out.println("Em uso: "      + pool.inUseCount());     // 1

// Usar
LogEntry poolLog = LogEntryFactory.create(LogLevel.INFO, "Log via pool");
dest.write(poolLog, "[INFO] Log via pool");

// Libertar — devolve ao pool, não destrói
pool.release(dest);
System.out.println("Disponiveis: " + pool.availableCount()); // 2
```

### O ciclo de vida de um objeto no pool

```
CRIAÇÃO (só uma vez, antes do pool)
        ↓
  DISPONÍVEL  ──── acquire() ────►  EM USO
      ▲                                │
      └──────── release() ─────────────┘

(nunca é destruído — é sempre reutilizado)
```

---

## Comparação M4 vs M5

|                   | M4 — Composite                           | M5 — Object Pool                    |
| ----------------- | ---------------------------------------- | ----------------------------------- |
| Tipo              | Estrutural                               | Criação                             |
| Objetivo          | Tratar grupos e indivíduos uniformemente | Reutilizar objetos caros            |
| Estrutura         | Árvore de objetos                        | Duas listas (disponíveis / em uso)  |
| Operações chave   | `add()`, `remove()`, `log()`             | `acquire()`, `release()`            |
| Problema resolve  | Distinção entre grupo e individual       | Criação repetida de objetos         |
| Analogia          | Menu HTML, escola, exército              | Biblioteca, armazém, ligações BD    |
| Classes novas     | `LogComponent`, `LogGroup`               | `LogDestinationPool`                |
| Classes alteradas | `LogEntry` (implementa `LogComponent`)   | Nenhuma                             |
| Exercício escola  | `Menu`, `Link`, `SubMenu`                | `ReusablePool`, `HttpURLConnection` |
