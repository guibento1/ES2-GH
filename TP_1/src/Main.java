import tp.es2.logging.*;

public class Main {
    public static void main(String[] args) {
        LogConfig config = LogConfig.getInstance();
        config.setGlobalLevel(LogLevel.DEBUG);
        config.setFormatPatterns("[%level][%time] %message");
        config.addDestination("console");

        Logger logger = new Logger();

        LogEntry info  = LogEntryFactory.create(LogLevel.INFO, "Aplicação iniciada");
        LogEntry error = LogEntryFactory.create(LogLevel.ERROR, "Falha na base de dados");

        logger.log(info);
        logger.log(error);
    }
}

