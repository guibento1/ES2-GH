package com.es2.memento;
import java.util.ArrayList;

public class Memento {
    private ArrayList<String> state;

    public Memento(ArrayList<String> studentNames) {
        this.state = new ArrayList<>(studentNames);
    }

    public ArrayList<String> getState(){
        return new ArrayList<>(state);
    }
}
