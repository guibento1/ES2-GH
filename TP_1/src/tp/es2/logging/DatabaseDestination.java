package tp.es2.logging;

public class DatabaseDestination implements LogDestination {
    private String databaseUrl;

    public DatabaseDestination(String databaseUrl) {
        this.databaseUrl = databaseUrl;
    }

    public String getDatabaseUrl() {
        return databaseUrl;
    }

    @Override
    public void write(LogEntry entry, String formattedMessage) {
        System.out.println(formattedMessage);
    }
}
