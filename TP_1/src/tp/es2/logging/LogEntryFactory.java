package tp.es2.logging;

public class LogEntryFactory {
    public static LogEntry create(LogLevel level, String message) {
        return new LogEntry(level, message);
    }
}
