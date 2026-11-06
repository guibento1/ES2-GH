package com.es2.logging;

import java.util.ArrayList;
import java.util.List;

public class LogConfigMemento {
    private final String formatPatterns;
    private final LogLevel globalLevel;
    private final List<LogDestination> destinations;

    public LogConfigMemento(LogLevel globalLevel, List<LogDestination> destinations, String formatPatterns) {
        this.globalLevel = globalLevel;
        this.destinations = new ArrayList<>(destinations);
        this.formatPatterns = formatPatterns;
    }

    public LogLevel getGlobalLevel() { return globalLevel; }

    public List<LogDestination> getDestinations() { return new ArrayList<>(destinations); }

    public String getFormatPatterns() { return formatPatterns; }
}
