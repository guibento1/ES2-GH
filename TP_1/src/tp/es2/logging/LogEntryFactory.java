package tp.es2.logging;

public class LogEntryFactory {
    public static LogEntry create(LogLevel level, String message) {
        switch (level) {
            case INFO: return new LogInfo(message);
            case DEBUG: return new LogDebug(message);
            case WARNING: return new LogWarning(message);
            case ERROR: return new LogError(message);
            default: throw new IllegalArgumentException("Nível desconhecido: " + level);
        }
    }
}
