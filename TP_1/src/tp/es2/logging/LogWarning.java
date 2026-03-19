package tp.es2.logging;

public class LogWarning extends LogEntry {
    public LogWarning(String message) {
        super(LogLevel.WARNING, message);
    }
}