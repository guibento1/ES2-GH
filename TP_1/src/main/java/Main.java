import java.util.Arrays;
import com.es2.logging.*;

public class Main {
    public static void main(String[] args) {
        // 1. Configurar o Singleton
        LogConfig config = LogConfig.getInstance();
        config.setGlobalLevel(LogLevel.DEBUG);
        config.setFormatPatterns("[%level] %time - %message");

        // 2. Criar os destinos (Bridge)
        LogDestination console = new ConsoleDestination();
        LogDestination file = new FileDestination("src/main/java/logs.txt");
        LogDestination databaseUrl = new DatabaseDestination("jdbc:mysql://localhost:3306/logs");

        // 3. Criar o Logger com os destinos
        Logger logger = new Logger(Arrays.asList(console, file,  databaseUrl));

        // 4. Criar entradas de log via Factory
        LogEntry info    = LogEntryFactory.create(LogLevel.INFO,    "Aplicação iniciada");
        LogEntry debug   = LogEntryFactory.create(LogLevel.DEBUG,   "A carregar configurações");
        LogEntry warning = LogEntryFactory.create(LogLevel.WARNING, "Memória a 80%");
        LogEntry error   = LogEntryFactory.create(LogLevel.ERROR,   "Falha na ligação à BD");

        // 5. Registar os logs
        logger.log(info);
        logger.log(debug);
        logger.log(warning);
        logger.log(error);

        // --------- Composite -------------
        // Criar groups
        LogGroup autenticacao = new LogGroup("Autenticacao");
        LogGroup baseDeDados = new LogGroup("Base de Dados");
        LogGroup interfacee = new LogGroup("Interface");
        LogGroup rede = new LogGroup("Rede");

        // Folhas/leafs
        autenticacao.add(LogEntryFactory.create(LogLevel.INFO, "Login com sucesso"));
        autenticacao.add(LogEntryFactory.create(LogLevel.WARNING, "Mude a pass de mes a mes"));
        autenticacao.add(LogEntryFactory.create(LogLevel.ERROR, "Credenciais incorretas"));
        autenticacao.add(LogEntryFactory.create(LogLevel.DEBUG, "Modo debug ativado"));

        baseDeDados.add(LogEntryFactory.create(LogLevel.ERROR, "Ligacao perdida"));
        interfacee.add(LogEntryFactory.create(LogLevel.INFO, "Interface carregada"));
        rede.add(LogEntryFactory.create(LogLevel.WARNING, "Latencia elevada"));

        // Adicionar os grupos ao sistema
        LogGroup sistema = new LogGroup("Sistema");
        sistema.add(autenticacao);
        sistema.add(baseDeDados);
        sistema.add(interfacee);
        sistema.add(rede);

        // Logar — trata grupos e individuais de forma uniforme
        sistema.log(logger);

        // --------- Object Pool -------------
        LogDestinationPool pool = new LogDestinationPool(Arrays.asList(
            new FileDestination("src/main/java/pool_logs_1.txt"),
            new FileDestination("src/main/java/pool_logs_2.txt")
        ));

        System.out.println("Disponiveis: " + pool.availableCount()); // 2

        LogDestination dest = pool.acquire();
        System.out.println("Disponiveis: " + pool.availableCount()); // 1
        System.out.println("Em uso: "      + pool.inUseCount());     // 1

        LogEntry poolLog = LogEntryFactory.create(LogLevel.INFO, "Log via pool");
        dest.write(poolLog, "[INFO] Log via pool");

        pool.release(dest);
        System.out.println("Disponiveis: " + pool.availableCount()); // 2

        // --------- Memento -------------
        LogConfigCaretaker caretaker = new LogConfigCaretaker(config);

        // Tirar snapshot
        caretaker.save();

        // Alterar configurações
        config.setGlobalLevel(LogLevel.ERROR);
        config.setFormatPatterns("[%level] %message %time");

        // Restaurar snapshot 0
        caretaker.restore(0);

        // --------- Decorator -------------
        LogComponent entry = LogEntryFactory.create(LogLevel.ERROR, "Falha critica");
        LogComponent decorated = new MonitorDecorator(new AlertDecorator(entry));
        decorated.log(logger);
    }
}