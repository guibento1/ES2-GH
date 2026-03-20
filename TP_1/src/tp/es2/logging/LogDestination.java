package tp.es2.logging;

public interface LogDestination {
    void write(LogEntry entry, String formattedMessage);
}
