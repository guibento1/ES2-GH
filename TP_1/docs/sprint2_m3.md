# Sprint 2 — M3 (Bridge)

## O que é o Bridge?

O Bridge é um padrão estrutural que **separa a abstração da implementação** para que possam variar independentemente. O cliente interage sempre com o objeto que representa a interface (abstração), que por sua vez delega os pedidos para o objeto que contém a implementação.

Desta forma, a implementação pode ser acrescentada em runtime, sem recompilar a aplicação.

---

## O problema que resolve

Imagina que tens uma classe `Shape` com subclasses `Circle` e `Square`. Queres adicionar cores — planeias criar `RedCircle`, `BlueCircle`, `RedSquare`, `BlueSquare`. Para cada nova cor ou forma a hierarquia cresce exponencialmente:

```
Sem Bridge — explosão de classes:
RedCircle, BlueCircle, GreenCircle
RedSquare, BlueSquare, GreenSquare
N formas × M cores = N×M classes! ❌

Com Bridge — duas hierarquias independentes:
Shape  → Circle, Square       (2 classes)
Color  → Red, Blue, Green     (3 classes)
Total: 2 + 3 = 5 classes ✅
```

---

## Analogia do mundo real — Controlo remoto e dispositivos

O exemplo clássico do refactoring.guru: tens controlos remotos e dispositivos. Sem Bridge precisarias de `TVBasicRemote`, `TVAdvancedRemote`, `RadioBasicRemote`, `RadioAdvancedRemote`. Com Bridge:

```
Abstração (controlo remoto)      Implementação (dispositivo)
BasicRemote ────────────────►  Device (interface)
AdvancedRemote                     ├── TV
                                   └── Radio
```

O controlo remoto delega as operações para o dispositivo. Podes adicionar novos dispositivos sem tocar nos controlos remotos, e vice-versa.

---

## Analogia do mundo real — Computadores e impressoras

Tens dois tipos de computadores (Mac e Windows) e dois tipos de impressoras (Epson e HP). Sem Bridge precisavas de quatro combinações. Com Bridge:

```
Abstração               Implementação
Mac    ────────────►  Printer (interface)
Windows                   ├── Epson
                          └── HP
```

Adicionas uma nova impressora sem tocar nas classes `Mac` ou `Windows`.

---

## Os papéis do padrão

| Papel | Diagrama da aula | Exercício da escola | Teu projeto |
|---|---|---|---|
| **Abstração** | `InterfaceEncapsulation` | `APIRequest` | `Logger` |
| **Abstração especializada** | `InterfaceSpecialization` | `APIRequestContentAggregator` | — |
| **Interface de implementação** | `InterfaceEncapsulation` (direita) | `APIServiceInterface` | `LogDestination` |
| **Implementação concreta** | `ImplementationOne`, `ImplementationTwo` | `APIMoodle` | `ConsoleDestination`, `FileDestination`, `DatabaseDestination` |

---

## Exercício da escola explicado

### `APIServiceInterface` — interface de implementação

Define o contrato que todas as implementações concretas devem seguir. É o lado direito do Bridge.

```java
public interface APIServiceInterface {
    String getContent(String contentId);
    String setContent(String content);
}
```

### `APIMoodle` — implementação concreta

Implementa `APIServiceInterface`. Guarda conteúdos num `LinkedHashMap` para garantir ordem de inserção. O `contentId = "0"` é um caso especial que agrega todo o conteúdo.

```java
public class APIMoodle implements APIServiceInterface {
    protected LinkedHashMap<String, String> content;

    public APIMoodle() {
        content = new LinkedHashMap<>();
    }

    @Override
    public String setContent(String contentValue) {
        String id = String.valueOf(content.size() + 1);
        content.put(id, contentValue);
        return id;
    }

    @Override
    public String getContent(String contentId) {
        if ("0".equals(contentId)) {
            // agrega todo o conteúdo
            StringBuilder sb = new StringBuilder();
            for (Map.Entry<String, String> entry : content.entrySet()) {
                sb.append(entry.getValue());
            }
            return sb.toString();
        } else {
            return content.get(contentId);
        }
    }
}
```

### `APIRequest` — abstração

É o lado esquerdo do Bridge. Mantém uma referência às implementações (`APIServiceInterface`) e delega as operações para elas.

```java
public class APIRequest {
    protected HashMap<String, APIServiceInterface> services; // referência às implementações

    public String addService(APIServiceInterface service) {
        String id = String.valueOf(nextServiceId);
        services.put(id, service);
        return id;
    }

    public String getContent(String serviceId, String contentId)
            throws ServiceNotFoundException {
        APIServiceInterface service = services.get(serviceId);
        if (service == null) throw new ServiceNotFoundException();
        return service.getContent(contentId); // delega para a implementação
    }

    public String setContent(String serviceId, String content)
            throws ServiceNotFoundException {
        APIServiceInterface service = services.get(serviceId);
        if (service == null) throw new ServiceNotFoundException();
        return service.setContent(content); // delega para a implementação
    }
}
```

### `APIRequestContentAggregator` — abstração especializada

Estende a abstração base e especializa o `getContent` para sempre devolver todo o conteúdo agregado de um serviço.

```java
public class APIRequestContentAggregator extends APIRequest {
    @Override
    public String getContent(String serviceId, String contentId)
            throws ServiceNotFoundException {
        APIServiceInterface service = services.get(serviceId);
        if (service == null) throw new ServiceNotFoundException();
        return service.getContent("0"); // sempre agrega tudo
    }
}
```

---

## Como funciona no projeto — M3

### `LogDestination` — interface de implementação

Define o contrato que todos os destinos de log devem seguir. É o lado direito do Bridge.

```java
public interface LogDestination {
    void write(LogEntry entry, String formattedMessage);
}
```

### Implementações concretas

Cada implementação sabe como escrever para o seu destino específico. O `Logger` não sabe nem precisa de saber como cada uma funciona.

```java
// ConsoleDestination — sem estado, sempre escreve em System.out
public class ConsoleDestination implements LogDestination {
    @Override
    public void write(LogEntry entry, String formattedMessage) {
        System.out.println(formattedMessage);
    }
}

// FileDestination — precisa de saber o caminho do ficheiro
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

// DatabaseDestination — precisa da URL da base de dados
public class DatabaseDestination implements LogDestination {
    private String databaseUrl;

    public DatabaseDestination(String databaseUrl) {
        this.databaseUrl = databaseUrl;
    }

    @Override
    public void write(LogEntry entry, String formattedMessage) {
        // lógica de escrita na base de dados
    }
}
```

### `Logger` — abstração

É o lado esquerdo do Bridge. Tem uma referência direta às implementações (`List<LogDestination>`) e delega a escrita para cada uma.

```java
public class Logger {
    private List<LogDestination> destinations; // referência às implementações

    public Logger(List<LogDestination> destinations) {
        this.destinations = destinations;
    }

    public void log(LogEntry entry) {
        LogConfig config = LogConfig.getInstance();

        // filtragem por nível
        if (entry.getLevel().ordinal() < config.getGlobalLevel().ordinal()) {
            return;
        }

        // formatar a mensagem
        String formatted = config.getFormatPatterns()
                .replace("%level", entry.getLevel().name())
                .replace("%message", entry.getMessage())
                .replace("%time", String.valueOf(entry.getTimestamp()));

        // Bridge — delega para cada destino
        for (LogDestination destination : destinations) {
            destination.write(entry, formatted); // delega para a implementação
        }
    }
}
```

---

## Comparação escola → projeto

| Escola | Projeto | Papel |
|---|---|---|
| `APIServiceInterface` | `LogDestination` | Interface de implementação |
| `APIMoodle` | `ConsoleDestination`, `FileDestination`, `DatabaseDestination` | Implementações concretas |
| `APIRequest` | `Logger` | Abstração — delega para implementação |
| `APIRequestContentAggregator` | — | Abstração especializada (não foi necessária) |
| `services` (HashMap) | `destinations` (List) | Referência às implementações |
| `service.getContent()` | `destination.write()` | Delegação para implementação |

---

## Como se usa no Main

```java
// Criar implementações (destinos)
LogDestination console     = new ConsoleDestination();
LogDestination file        = new FileDestination("src/main/java/logs.txt");
LogDestination databaseUrl = new DatabaseDestination("jdbc:mysql://localhost:3306/logs");

// Criar abstração (Logger) com as implementações
Logger logger = new Logger(Arrays.asList(console, file, databaseUrl));

// O Logger delega para cada destino automaticamente
logger.log(LogEntryFactory.create(LogLevel.INFO, "Aplicacao iniciada"));
```

---

## Para adicionar um novo destino — sem alterar nada existente

```java
// Criar nova implementação
public class SlackDestination implements LogDestination {
    @Override
    public void write(LogEntry entry, String formattedMessage) {
        // envia para Slack
    }
}

// Usar no Main — Logger não muda
Logger logger = new Logger(Arrays.asList(
    new ConsoleDestination(),
    new FileDestination("logs.txt"),
    new SlackDestination() // novo destino ✅
));
```

Nenhuma classe existente foi alterada — só criaste uma nova. Isto é o princípio **Open/Closed** do Bridge em ação.

---

## Resumo

| Aspeto | Detalhe |
|---|---|
| Tipo de padrão | Estrutural |
| Problema resolve | Logger acoplado ao destino — mudança de destino exigiria alterar o Logger |
| Solução | Logger delega para `LogDestination` — destinos trocáveis em runtime |
| Hierarquia esquerda | `Logger` (abstração) |
| Hierarquia direita | `LogDestination` + implementações concretas |
| Chave do padrão | `destination.write(entry, formatted)` — delegação |
| Extensão | Criar nova classe que implementa `LogDestination` — sem tocar no `Logger` |
