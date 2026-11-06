package com.es2.logging;

public class MonitorDecorator extends LogEntryDecorator {
    public MonitorDecorator(LogComponent wrapped) {
        super(wrapped);
    }

    @Override
    public void log(Logger logger) {
        if (wrapped instanceof LogEntry) {
            LogEntry entry = (LogEntry) wrapped;
            System.out.println("MONITOR: [" + entry.getLevel() 
                + "] " + entry.getMessage());
        }
        super.log(logger);
    }
}
