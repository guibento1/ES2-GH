import tp.es2.logging.*;

public class Main {
    public static void main(String[] args) {
        // M1: usar o Singleton de configuração
        LogConfig config = LogConfig.getInstance();
        config.setGlobalLevel(LogLevel.DEBUG);
        config.setFormatPatterns("[%level][%time] %message");
        config.addDestination("console");

        System.out.println("Nível global: " + config.getGlobalLevel());
        System.out.println("Destinos: " + config.getDestinations());
        System.out.println("Formato: " + config.getFormatPatterns());

        // M2: criar registos de log via Factory
        LogEntry infoLog = LogEntryFactory.create(LogLevel.INFO, "Aplicação iniciada");
        LogEntry errorLog = LogEntryFactory.create(LogLevel.ERROR, "Falha na base de dados");

        System.out.println("INFO -> level=" + infoLog.getLevel()
                + ", ts=" + infoLog.getTimestamp()
                + ", msg=" + infoLog.getMessage());

        System.out.println("ERROR -> level=" + errorLog.getLevel()
                + ", ts=" + errorLog.getTimestamp()
                + ", msg=" + errorLog.getMessage());
    }
}
