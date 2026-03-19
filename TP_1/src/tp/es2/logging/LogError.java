package tp.es2.logging;

public class LogError extends LogEntry {
    public LogError(String message) {
        super(LogLevel.ERROR, message);
    }
}