package tp.es2.logging;

import java.util.ArrayList;
import java.util.List;

public class LogConfig {
    private static final LogConfig instance = new LogConfig();
    private LogLevel globalLevel;
    private List<String> destinations;
    private String formatPatterns;

    private LogConfig() {
        this.globalLevel = LogLevel.INFO; // Default log level
        this.destinations = new ArrayList<>(); // Default to no destinations
        this.formatPatterns = "[%level] %message"; // Default format
    }

    public static LogConfig getInstance() {
        return instance;
    }

    public LogLevel getGlobalLevel() {
        return globalLevel;
    }

    public void setGlobalLevel(LogLevel globalLevel) {
        this.globalLevel = globalLevel;
    }

    public List<String> getDestinations() {
        return destinations;
    }

    public void setDestinations(List<String> destinations) {
        this.destinations = destinations;
    }

    public void addDestination(String destination) {
        this.destinations.add(destination);
    }

    public String getFormatPatterns() {
        return formatPatterns;
    }

    public void setFormatPatterns(String formatPatterns) {
        this.formatPatterns = formatPatterns;
    }
}

