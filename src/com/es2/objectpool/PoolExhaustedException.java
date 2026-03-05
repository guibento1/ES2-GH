package com.es2.objectpool;

public class PoolExhaustedException extends Exception {
    public PoolExhaustedException() {
        super("A pool atingiu o número máximo de conexões.");
    }
}