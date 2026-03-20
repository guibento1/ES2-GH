# M3 — Módulo de Abstração de Destino de Logs

## Padrão Aplicado: Bridge Pattern

O padrão **Bridge** permite separar a abstração (`Logger`) da sua implementação (destinos de logs), possibilitando que ambas evoluam de forma independente.

---

## Justificação

O sistema de logs deve suportar múltiplos destinos (consola, ficheiro, base de dados, etc.) sem alterar a lógica principal do `Logger`.

Se o `Logger` estivesse diretamente ligado a implementações concretas, qualquer novo destino obrigaria a modificar essa classe, violando o princípio **Open/Closed**.

O padrão Bridge resolve este problema ao introduzir uma interface (`LogDestination`) que abstrai o comportamento dos destinos, permitindo:

- adicionar novos destinos sem alterar o `Logger`
- trocar destinos dinamicamente
- reduzir o acoplamento entre componentes

---

## Classes Envolvidas

### `LogDestination` (interface)

Define o contrato que todos os destinos de log devem implementar.

```java
package tp.es2.logging;

public interface LogDestination {
    void write(LogEntry entry, String formattedMessage);
}
```

### `ConsoleDestination`

Implementação concreta para escrita na consola.

```java
package tp.es2.logging;

public class ConsoleDestination implements LogDestination {
    @Override
    public void write(LogEntry entry, String formattedMessage) {
        System.out.println(formattedMessage);
    }
}
```

### `FileDestination`

Implementação concreta para escrita em ficheiro.

```java
package tp.es2.logging;

import java.io.FileWriter;
import java.io.IOException;

public class FileDestination implements LogDestination {
    private String filePath;

    public FileDestination(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public void write(LogEntry entry, String formattedMessage) {
        try (FileWriter writer = new FileWriter(filePath, true)) {
            writer.write(formattedMessage + "\n");
        } catch (IOException e) {
            System.err.println("Erro ao escrever no ficheiro: " + e.getMessage());
        }
    }
}
```

### `Logger` (Abstraction)

Classe responsável por processar o log e delegar a escrita para os destinos.

```java
package tp.es2.logging;

import java.util.List;

public class Logger {
    private List<LogDestination> destinations;

    public Logger(List<LogDestination> destinations){
        this.destinations = destinations;
    }

    public void log(LogEntry entry){
        LogConfig config = LogConfig.getInstance();

        // 1. Filtragem por nível
        if(entry.getLevel().ordinal() < config.getGlobalLevel().ordinal()){
            return;
        }

        // 2. Ler o pattern
        String pattern = config.getFormatPatterns();

        // 3. Formatar mensagem
        String formatted = pattern
                .replace("%level", entry.getLevel().name())
                .replace("%message", entry.getMessage())
                .replace("%time", String.valueOf(entry.getTimestamp()));

        // 4. Bridge → delega para os destinos
        for (LogDestination destination : destinations){
            destination.write(entry, formatted);
        }
    }
}
```

### `LogConfig` (integração com M1)

Agora também armazena os destinos de log.

```java
private List<LogDestination> destinations;
```

---

## Como Funciona

| Elemento | Descrição |
|---|---|
| `LogDestination` | Interface comum para todos os destinos |
| `ConsoleDestination` | Escreve logs na consola |
| `FileDestination` | Escreve logs em ficheiro |
| `Logger` | Processa o log e delega para os destinos |
| `destinations` (List) | Permite múltiplos destinos ao mesmo tempo |

---

## Diagrama UML

```
┌──────────────────────────────────────────────────────────────┐
│                          Bridge                              │
│                                                              │
│  ┌──────────────────────────────┐                            │
│  │          Logger              │  (Abstraction)             │
│  ├──────────────────────────────┤                            │
│  │ - destinations: List<LogDestination>                      │
│  ├──────────────────────────────┤                            │
│  │ + log(entry: LogEntry): void │                            │
│  └──────────────┬───────────────┘                            │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────┐                            │
│  │       LogDestination         │  (Implementor)             │
│  ├──────────────────────────────┤                            │
│  │ + write(LogEntry, String)    │                            │
│  └──────────────┬───────────────┘                            │
│                 │                                            │
│     ┌───────────┼───────────┐                                │
│     ▼           ▼           ▼                                │
│ ConsoleDest  FileDest   (outros destinos)                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Interação com M1 e M2

A classe `Logger` faz a ligação entre os três módulos:

- usa `LogConfig` (M1 — Singleton) → obter configurações
- recebe `LogEntry` (M2 — Factory) → dados do log
- delega para `LogDestination` (M3 — Bridge) → destino do log

---

## Relações UML do M3

| Relação | Tipo | Seta |
|---|---|---|
| `Logger` → `LogDestination` | Associação (Bridge) | `───►` |
| `Logger` → `LogConfig` | Dependência | `- - ->` |
| `Logger` → `LogEntry` | Dependência | `- - ->` |
| `FileDestination` → `LogDestination` | Implementação | `───▷` |
| `ConsoleDestination` → `LogDestination` | Implementação | `───▷` |

---

## Resumo dos Padrões (Atualizado)

| Módulo | Padrão | Classe Principal | Benefício |
|---|---|---|---|
| M1 | Singleton | `LogConfig` | Configuração global única |
| M2 | Factory | `LogEntryFactory` | Criação centralizada de logs |
| M3 | Bridge | `Logger` / `LogDestination` | Abstração dos destinos de log |
