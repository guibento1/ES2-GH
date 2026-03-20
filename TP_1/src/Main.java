import tp.es2.logging.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 1. Configurar o Singleton
        LogConfig config = LogConfig.getInstance();
        config.setGlobalLevel(LogLevel.DEBUG);
        config.setFormatPatterns("[%level] %time - %message");

        // 2. Criar os destinos (Bridge)
        LogDestination console = new ConsoleDestination();
        LogDestination file = new FileDestination("src/logs.txt");
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
    }
}