package com.es2.factory;

public abstract class Product {
    private String brand;

    public Product(String brand) {
        this.brand = brand;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
}
