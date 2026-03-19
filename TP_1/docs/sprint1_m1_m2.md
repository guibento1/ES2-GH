# Sprint 1 — Sistema de Logs

## Objetivo

Aplicar padrões de desenho de software para criar um sistema de logs flexível, extensível e eficiente, capaz de evoluir com novas funcionalidades e necessidades da aplicação.

---

## M1 — Módulo de Configuração Centralizada

### Padrão Aplicado: **Singleton**

O padrão **Singleton** garante que uma classe tem **uma única instância** ao longo de toda a aplicação, fornecendo um ponto de acesso global a essa instância.

### Justificação

As configurações globais do sistema de logs (nível, destinos, formato) devem ser partilhadas de forma consistente. Criar múltiplas instâncias poderia resultar em configurações inconsistentes. O Singleton garante um único ponto de verdade.

### Classes Envolvidas

#### `LogLevel` (enum)

Define os níveis de log disponíveis, ordenados por gravidade crescente.

```java
package tp.es2.logging;

public enum LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR
}
```

#### `LogConfig` (Singleton)

Armazena todas as configurações globais do sistema de logs.

```java
package tp.es2.logging;

import java.util.ArrayList;
import java.util.List;

public class LogConfig {
    private static final LogConfig instance = new LogConfig();
    private LogLevel globalLevel;
    private List<String> destinations;
    private String formatPatterns;

    private LogConfig() {
        this.globalLevel = LogLevel.INFO;
        this.destinations = new ArrayList<>();
        this.formatPatterns = "[%level] %message";
    }

    public static LogConfig getInstance() {
        return instance;
    }

    public LogLevel getGlobalLevel() { return globalLevel; }
    public void setGlobalLevel(LogLevel globalLevel) { this.globalLevel = globalLevel; }

    public List<String> getDestinations() { return destinations; }
    public void setDestinations(List<String> destinations) { this.destinations = destinations; }
    public void addDestination(String destination) { this.destinations.add(destination); }

    public String getFormatPatterns() { return formatPatterns; }
    public void setFormatPatterns(String formatPatterns) { this.formatPatterns = formatPatterns; }
}
```

### Como Funciona

| Elemento | Descrição |
|---|---|
| `instance` (static, final) | Única instância criada na inicialização da classe |
| `LogConfig()` (privado) | Impede a criação de instâncias externas |
| `getInstance()` (static) | Único ponto de acesso à instância |

### Diagrama UML

```
┌─────────────────────────────────────────────────┐
│                   Singleton                      │
│                                                 │
│  ┌──────────────────────────────────────────┐   │
│  │           [Singleton] LogConfig          │◄──┘ (auto-referência)
│  ├──────────────────────────────────────────┤
│  │ - instance: LogConfig {static, final}    │
│  │ - globalLevel: LogLevel                  │
│  │ - destinations: List<String>             │
│  │ - formatPatterns: String                 │
│  ├──────────────────────────────────────────┤
│  │ - LogConfig()                            │
│  │ + getInstance(): LogConfig               │
│  │ + getGlobalLevel(): LogLevel             │
│  │ + setGlobalLevel(LogLevel): void         │
│  │ + getDestinations(): List<String>        │
│  │ + setDestinations(List<String>): void    │
│  │ + addDestination(String): void           │
│  │ + getFormatPatterns(): String            │
│  │ + setFormatPatterns(String): void        │
│  └──────────────────────────────────────────┘
└─────────────────────────────────────────────────┘

LogConfig - - -> LogLevel   (dependência)
```

---

## M2 — Módulo de Criação de Registos de Log

### Padrão Aplicado: **Factory (Static Factory)**

O padrão **Factory** encapsula a lógica de criação de objetos, permitindo adicionar novos tipos no futuro sem alterar o código existente.

### Justificação

A criação de objetos `LogEntry` deve ser centralizada para permitir extensibilidade. Ao usar uma factory, o código cliente não precisa de conhecer os detalhes de construção — e novos tipos de log podem ser adicionados apenas com uma nova entrada no enum `LogLevel`, sem alterar `LogEntryFactory`.

### Classes Envolvidas

#### `LogEntry`

Representa um registo de log com nível, mensagem e timestamp.

```java
package tp.es2.logging;

public class LogEntry {
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
}
```

#### `LogEntryFactory`

Utility class responsável por criar instâncias de `LogEntry`.

```java
package tp.es2.logging;

public class LogEntryFactory {
    public static LogEntry create(LogLevel level, String message) {
        return new LogEntry(level, message);
    }
}
```

### Extensibilidade

Para adicionar um novo tipo de log basta adicionar ao enum — **sem alterar** `LogEntryFactory`:

```java
public enum LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL  // ✅ novo tipo — nenhuma outra classe precisa de mudar
}
```

### Diagrama UML

```
┌──────────────────────────────────────────────────────────────┐
│                          Factory                             │
│                                                              │
│  ┌───────────────────────────┐                               │
│  │         LogEntry          │                               │
│  ├───────────────────────────┤                               │
│  │ - level: LogLevel         │                               │
│  │ - message: String         │                               │
│  │ - timestamp: long         │                               │
│  ├───────────────────────────┤                               │
│  │ + LogEntry(LogLevel, String)                              │
│  │ + getLevel(): LogLevel    │                               │
│  │ + getMessage(): String    │                               │
│  │ + getTimestamp(): long    │                               │
│  └───────────────────────────┘                               │
│              ▲                                               │
│         - - -┘  (dependência)                                │
│  ┌────────────────────────────────────┐                      │
│  │      [Factory] LogEntryFactory     │                      │
│  ├────────────────────────────────────┤                      │
│  │  <<utility class (static factory)>>│                      │
│  ├────────────────────────────────────┤                      │
│  │ + create(LogLevel, String): LogEntry                      │
│  └────────────────────────────────────┘                      │
└──────────────────────────────────────────────────────────────┘
```

---

## Interação entre Módulos

A classe `Logger` liga os dois módulos — usa `LogConfig` (M1) para obter as configurações e `LogEntry` (M2) para processar os registos.

```java
package tp.es2.logging;

public class Logger {
    public void log(LogEntry entry) {
        LogConfig config = LogConfig.getInstance();

        // Filtragem por nível
        if (entry.getLevel().ordinal() < config.getGlobalLevel().ordinal()) {
            return;
        }

        // Formatação da mensagem
        String formatted = config.getFormatPatterns()
                .replace("%level", entry.getLevel().name())
                .replace("%message", entry.getMessage())
                .replace("%time", String.valueOf(entry.getTimestamp()));

        System.out.println(formatted);
    }
}
```

### Relações UML do Logger

| Relação | Tipo | Seta |
|---|---|---|
| `Logger` → `LogConfig` | Dependência (usa `getInstance()`) | `- - ->` |
| `Logger` → `LogEntry` | Dependência (recebe como parâmetro) | `- - ->` |

---

## Resumo dos Padrões

| Módulo | Padrão | Classe Principal | Benefício |
|---|---|---|---|
| M1 | Singleton | `LogConfig` | Uma única instância de configuração global |
| M2 | Static Factory | `LogEntryFactory` | Criação centralizada e extensível de logs |
