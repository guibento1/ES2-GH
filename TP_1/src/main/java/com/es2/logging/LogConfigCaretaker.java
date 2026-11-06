package com.es2.logging;

import java.util.ArrayList;

public class LogConfigCaretaker {
    private LogConfig logConfig;
    private ArrayList<LogConfigMemento> mementos = new ArrayList<>();

    public LogConfigCaretaker(LogConfig logConfig) {
        this.logConfig = logConfig;
    }

    public void save() {
        LogConfigMemento memento = logConfig.createMemento();
        mementos.add(memento);
    }

    public void restore(int index) {
        if (index < 0 || index >= mementos.size()) {
            throw new IndexOutOfBoundsException("Índice de memento inválido");
        }
        LogConfigMemento memento = mementos.get(index);
        logConfig.restoreMemento(memento);    
    }
}
