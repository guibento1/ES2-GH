package tp.es2.logging;

public class DatabaseDestination implements LogDestination {
    private String databaseUrl;

    public DatabaseDestination(String databaseUrl) {
        this.databaseUrl = databaseUrl;
    }

    @Override
    public void write(LogEntry entry, String formattedMessage) {
        return;
    }

    public String getDatabaseUrl() {
        return databaseUrl;
    }

    public void setDatabaseUrl(String databaseUrl) {
        this.databaseUrl = databaseUrl;
    }
}
