package com.es2.objectpool;

import java.io.IOException;
import java.net.HttpURLConnection;

public class Main {
    public static void main(String[] args) throws IOException, PoolExhaustedException, ObjectNotFoundException {
        ReusablePool pool = ReusablePool.getInstance();

        // Adquirir conexão
        HttpURLConnection conn1 = pool.acquire();
        System.out.println("Conexão adquirida: " + conn1);

        // Libertar conexão
        pool.release(conn1);
        System.out.println("Conexão libertada");

        // Reset da pool
        pool.resetPool();
        System.out.println("Pool reiniciada");
    }
}