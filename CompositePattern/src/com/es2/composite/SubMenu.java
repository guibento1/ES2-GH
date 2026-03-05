package com.es2.composite;

import java.util.ArrayList;
import java.util.List;

public class SubMenu extends Menu {
    private List<Menu> children = new ArrayList<>();

    public SubMenu() {}

    public void addChild(Menu child) {
        children.add(child);
    }

    public void removeChild(Menu child) {
        children.remove(child);
    }

    @Override
    public void showOptions() {
        System.out.println(getLabel());
        for (Menu child : children) {
            child.showOptions();
        }
    }
}