package com.es2.logging;

public class AlertDecorator extends LogEntryDecorator {
    public AlertDecorator(LogComponent wrapped) {
        super(wrapped);
    }

    @Override
    public void log(Logger logger) {
        if (wrapped instanceof LogEntry) {
            LogEntry entry = (LogEntry) wrapped;
            if (entry.getLevel() == LogLevel.ERROR) {
                System.out.println("ALERTA ADMIN: Erro critico detetado - " 
                    + entry.getMessage());
            }
        }
        super.log(logger);
    }
}
