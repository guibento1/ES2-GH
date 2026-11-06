package com.es2.logging;

public class LogEntryDecorator implements LogComponent {
    protected LogComponent wrapped;

    public LogEntryDecorator(LogComponent wrapped) {
        this.wrapped = wrapped;
    }

    @Override
    public void log(Logger logger) {
        wrapped.log(logger);
    }

    @Override
    public String getCategory() {
        return wrapped.getCategory();
    }
}
