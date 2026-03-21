package tp.es2.logging;

public abstract class LogEntry implements LogComponent {
    private final LogLevel level;
    private final String message;
    private final long timestamp;

    public LogEntry(LogLevel level, String message) {
        this.level = level;
        this.message = message;
        this.timestamp = System.currentTimeMillis();
    }

    public LogLevel getLevel() {
        return level;
    }

    public String getMessage() {
        return message;
    }

    public long getTimestamp() {
        return timestamp;
    }

    @Override
    public void log(Logger logger) {
        logger.log(this);
    }

    @Override
    public String getCategory() {
        return getLevel().name();
    }
}
