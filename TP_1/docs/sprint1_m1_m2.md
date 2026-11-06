# Sprint 1 — M1 (Singleton) e M2 (Factory)

---

## M1 — Singleton (Configuração Centralizada)

### O que é o Singleton?

O Singleton é um padrão de **criação** que obriga à criação de uma **única instância** de um objeto na aplicação, quando ele for necessário pela primeira vez (lazy instantiation). A classe Singleton é responsável pela criação do objeto (static), enquanto que os clientes chamam um método assessor para aceder à instância. Desta forma, nenhum objeto adquire a posse do objeto Singleton.

---

### Analogia do mundo real — Governo

Um país pode ter apenas um governo oficial. Independentemente das identidades pessoais dos indivíduos que formam os governos, o título "O Governo de X" é um ponto de acesso global que identifica o grupo de pessoas responsável. Não importa quantas vezes perguntes — recebes sempre o mesmo governo.

### Analogia do mundo real — Configuração de aplicação

Uma aplicação tem um ficheiro de configuração com definições globais. Se cada módulo criasse a sua própria cópia das configurações, podiam existir valores inconsistentes em diferentes partes do sistema. O Singleton garante que há apenas um objeto de configuração partilhado por toda a aplicação.

---

### Os papéis do padrão

| Papel | Diagrama da aula | Exercício da escola | Teu projeto |
|---|---|---|---|
| **Singleton** | `Singleton` | `Registry` | `LogConfig` |
| **Cliente** | `Client` | Qualquer classe que chame `getInstance()` | `Logger` |

---

### Exercício da escola explicado

#### `Registry` — Singleton com lazy instantiation

A escola usa **lazy instantiation** — a instância só é criada quando `getInstance()` é chamado pela primeira vez. Também é **thread-safe** com `synchronized`.

```java
public class Registry {
    private static Registry instance; // null até ser necessária
    private String path;
    private String connectionString;

    private Registry() {} // construtor privado — ninguém cria diretamente

    public static synchronized Registry getInstance() {
        if (instance == null) { // lazy — só cria quando necessário
            instance = new Registry();
        }
        return instance;
    }

    public String getPath() { return path; }
    public void setPath(String path) { this.path = path; }
    public String getConnectionString() { return connectionString; }
    public void setConnectionString(String cs) { this.connectionString = cs; }
}
```

**Como se usa:**
```java
Registry reg = Registry.getInstance();
reg.setPath("/app/files");
reg.setConnectionString("jdbc:mysql://localhost/db");

// Noutro lado da aplicação — mesma instância!
Registry reg2 = Registry.getInstance();
System.out.println(reg2.getPath()); // "/app/files"
```

---

### Como funciona no projeto — M1

O teu projeto usa **eager instantiation** — a instância é criada logo quando a classe é carregada, sem esperar pela primeira chamada. É mais simples que a versão da escola mas igualmente válida para o enunciado.

```java
public class LogConfig {
    private static final LogConfig instance = new LogConfig(); // eager — cria logo
    private LogLevel globalLevel;
    private List<LogDestination> destinations;
    private String formatPatterns;

    private LogConfig() { // construtor privado
        this.globalLevel = LogLevel.INFO;
        this.destinations = new ArrayList<>();
        this.formatPatterns = "[%level] %message";
    }

    public static LogConfig getInstance() { // ponto de acesso global
        return instance;
    }

    // getters e setters...
}
```

**Como se usa:**
```java
LogConfig config = LogConfig.getInstance();
config.setGlobalLevel(LogLevel.DEBUG);
config.setFormatPatterns("[%level] %time - %message");

// Noutro lado da aplicação — mesma instância!
LogConfig config2 = LogConfig.getInstance();
System.out.println(config2.getGlobalLevel()); // DEBUG
```

---

### Comparação escola → projeto

| Escola (`Registry`) | Projeto (`LogConfig`) | Diferença |
|---|---|---|
| `lazy instantiation` | `eager instantiation` | Escola cria na 1ª chamada, projeto cria logo |
| `synchronized` | sem `synchronized` | Escola é thread-safe, projeto não |
| `instance == null` | `final` | Escola verifica se existe, projeto garante com `final` |
| `path`, `connectionString` | `globalLevel`, `destinations`, `formatPatterns` | Conteúdo diferente, conceito igual |
| `getPath()`, `setPath()` | `getGlobalLevel()`, `setGlobalLevel()` | Getters/setters do estado global |

---

### Porquê é importante ter um único ponto de acesso?

```java
// SEM Singleton — configurações inconsistentes
LogConfig config1 = new LogConfig(); // instância 1
config1.setGlobalLevel(LogLevel.DEBUG);

LogConfig config2 = new LogConfig(); // instância 2 — diferente!
config2.setGlobalLevel(LogLevel.ERROR);

// O Logger usa config1 ou config2? Qual é a correta? ❌

// COM Singleton — sempre a mesma instância
LogConfig config = LogConfig.getInstance(); // sempre a mesma
config.setGlobalLevel(LogLevel.DEBUG);
// qualquer parte da aplicação que chame getInstance() obtém o mesmo DEBUG ✅
```

---

### Exemplo de uso no Main

```java
// 1. Configurar o Singleton
LogConfig config = LogConfig.getInstance();
config.setGlobalLevel(LogLevel.DEBUG);
config.setFormatPatterns("[%level] %time - %message");
```

---

## M2 — Factory (Criação de Registos de Log)

### O que é o Factory Method?

O Factory Method é um padrão de **criação** que define uma interface para a criação de objetos, sem comprometer as especificidades de cada objeto. A superclasse implementa o comportamento genérico, enquanto que as subclasses implementam os detalhes da criação.

Para evitar várias formas de instanciação, os construtores não podem ser públicos e o método da fábrica deve ser `static`.

---

### Analogia do mundo real — Logística

Imagina uma aplicação de logística. A primeira versão só consegue lidar com transporte por caminhão. Depois precisas de adicionar transporte marítimo. Se o código estiver acoplado à classe `Truck`, alterar toda a base de código seria necessário. O Factory resolve isto:

```
Logistics (factory abstrata)
    ├── RoadLogistics → cria Truck
    └── SeaLogistics  → cria Ship
```

O cliente chama `createTransport()` sem saber se vai receber um caminhão ou um navio.

### Analogia do mundo real — Interface de utilizador cross-platform

Uma aplicação precisa de botões diferentes para Windows e Mac:

```
Dialog (factory abstrata)
    ├── WindowsDialog → cria WindowsButton
    └── HtmlDialog    → cria HtmlButton
```

O cliente chama `createButton()` — a factory decide o tipo concreto.

---

### Os papéis do padrão

| Papel | Exercício da escola | Teu projeto |
|---|---|---|
| **Interface/produto base** | `Product` (interface) | `LogEntry` (abstrata) |
| **Produtos concretos** | `Computer`, `Software` | `LogInfo`, `LogDebug`, `LogWarning`, `LogError` |
| **Factory** | `FactoryProduct` (abstrata) | `LogEntryFactory` |

---

### Exercício da escola explicado

#### `Product` — interface do produto

Define o contrato que todos os produtos devem seguir. É uma **interface** porque não tem atributos nem implementação partilhada — é só um contrato.

```java
public interface Product {
    String getBrand();
    void setBrand(String brand);
}
```

#### `Computer` e `Software` — produtos concretos

Implementam `Product`. Os construtores são `protected` — ninguém os pode instanciar diretamente, só a factory.

```java
public class Computer implements Product {
    private String brand;

    protected Computer() {} // protected — só a factory cria

    @Override
    public String getBrand() { return brand; }

    @Override
    public void setBrand(String brand) { this.brand = brand; }
}
```

#### `FactoryProduct` — factory abstrata

É `abstract` e tem um método `static` que decide qual produto criar com base no tipo passado.

```java
public abstract class FactoryProduct {
    public static Product makeProduct(String type)
            throws UndefinedProductException {
        if (type == null) throw new UndefinedProductException();
        switch (type.toLowerCase()) {
            case "computer": return new Computer();
            case "software": return new Software();
            default: throw new UndefinedProductException();
        }
    }
}
```

**Como se usa:**
```java
Product p1 = FactoryProduct.makeProduct("computer");
p1.setBrand("Dell");

Product p2 = FactoryProduct.makeProduct("software");
p2.setBrand("Adobe");
```

---

### Como funciona no projeto — M2

A diferença principal face à escola é que o teu projeto usa uma **classe abstrata** (`LogEntry`) em vez de interface (`Product`), porque `LogEntry` tem atributos e implementação partilhada (`level`, `message`, `timestamp` e os getters) — seria repetição de código em cada subclasse se fosse interface.

#### `LogEntry` — produto base (classe abstrata)

```java
public abstract class LogEntry implements LogComponent {
    private final LogLevel level;
    private final String message;
    private final long timestamp;

    public LogEntry(LogLevel level, String message) {
        this.level = level;
        this.message = message;
        this.timestamp = System.currentTimeMillis();
    }

    public LogLevel getLevel() { return level; }
    public String getMessage() { return message; }
    public long getTimestamp() { return timestamp; }

    @Override
    public void log(Logger logger) { logger.log(this); }

    @Override
    public String getCategory() { return getLevel().name(); }
}
```

#### Subclasses concretas

```java
public class LogInfo extends LogEntry {
    public LogInfo(String message) { super(LogLevel.INFO, message); }
}

public class LogDebug extends LogEntry {
    public LogDebug(String message) { super(LogLevel.DEBUG, message); }
}

public class LogWarning extends LogEntry {
    public LogWarning(String message) { super(LogLevel.WARNING, message); }
}

public class LogError extends LogEntry {
    public LogError(String message) { super(LogLevel.ERROR, message); }
}
```

#### `LogEntryFactory` — factory

```java
public class LogEntryFactory {
    public static LogEntry create(LogLevel level, String message) {
        switch (level) {
            case INFO:    return new LogInfo(message);
            case DEBUG:   return new LogDebug(message);
            case WARNING: return new LogWarning(message);
            case ERROR:   return new LogError(message);
            default: throw new IllegalArgumentException("Nivel desconhecido: " + level);
        }
    }
}
```

---

### Comparação escola → projeto

| Escola | Projeto | Diferença |
|---|---|---|
| `Product` (interface) | `LogEntry` (abstrata) | Escola: só contrato. Projeto: atributos partilhados |
| `Computer`, `Software` | `LogInfo`, `LogDebug`, `LogWarning`, `LogError` | Conceito igual, nomes diferentes |
| `FactoryProduct` (abstrata) | `LogEntryFactory` (concreta) | Escola: abstrata. Projeto: concreta com método static |
| `makeProduct(String type)` | `create(LogLevel level, String message)` | Escola usa String, projeto usa enum |
| `UndefinedProductException` | `IllegalArgumentException` | Escola usa custom exception, projeto usa built-in |
| Construtores `protected` | Construtores `public` | Escola protege mais a instanciação |

### Porquê interface na escola e classe abstrata no projeto?

| | Interface (`Product`) | Classe abstrata (`LogEntry`) |
|---|---|---|
| Tem atributos? | ❌ | ✅ `level`, `message`, `timestamp` |
| Tem implementação partilhada? | ❌ | ✅ getters, `log()`, `getCategory()` |
| Só define contrato? | ✅ | ❌ |

Se `LogEntry` fosse interface, terias de repetir `level`, `message`, `timestamp` e os getters em **cada subclasse** — muito código duplicado.

---

### Extensibilidade — "sem alterar o código existente"

O enunciado pede que o sistema permita a adição futura de novos tipos sem alterar o código existente. Para adicionar `LogCritical`:

```java
// 1. Criar nova subclasse — ficheiro novo ✅
public class LogCritical extends LogEntry {
    public LogCritical(String message) {
        super(LogLevel.CRITICAL, message);
    }
}

// 2. Adicionar ao enum — uma linha ✅
public enum LogLevel { DEBUG, INFO, WARNING, ERROR, CRITICAL }

// 3. Adicionar ao switch da factory — uma linha ✅
case CRITICAL: return new LogCritical(message);
```

Não alteraste `LogInfo`, `LogDebug`, `LogWarning`, `LogError` — só adicionaste. ✅

---

### Exemplo de uso no Main

```java
// 4. Criar entradas de log via Factory
LogEntry info    = LogEntryFactory.create(LogLevel.INFO,    "Aplicacao iniciada");
LogEntry debug   = LogEntryFactory.create(LogLevel.DEBUG,   "A carregar configuracoes");
LogEntry warning = LogEntryFactory.create(LogLevel.WARNING, "Memoria a 80%");
LogEntry error   = LogEntryFactory.create(LogLevel.ERROR,   "Falha na ligacao a BD");

// 5. Registar os logs
logger.log(info);
logger.log(debug);
logger.log(warning);
logger.log(error);
```

---

## Comparação M1 vs M2

| | M1 — Singleton | M2 — Factory |
|---|---|---|
| Tipo | Criação | Criação |
| Objetivo | Uma única instância global | Encapsular a criação de objetos |
| Problema resolve | Configurações inconsistentes com múltiplas instâncias | Lógica de criação espalhada pelo código |
| Chave | `getInstance()` | `create()` / `makeProduct()` |
| Construtor | `private` | `protected` (escola) / `public` (projeto) |
| Escola | `Registry` | `FactoryProduct`, `Computer`, `Software` |
| Projeto | `LogConfig` | `LogEntryFactory`, `LogInfo`, `LogDebug`, etc. |
| Analogia | Governo de um país | Fábrica de produtos / logística |
