package com.es2.composite;

public abstract class Menu {
    private String label;

    public Menu() {}

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    // Metodo abstrato que vai ser implementado por Link e SubMenu
    public abstract void showOptions();
}