package com.es2.factorymethod;

public abstract class FactoryProduct {

    public static Product makeProduct(String type) throws UndefinedProductException {
        if (type == null) {
            throw new UndefinedProductException();
        }
        switch (type.toLowerCase()) {
            case "computer":
                return new Computer();
            case "software":
                return new Software();
            default:
                throw new UndefinedProductException();
        }
    }
}
