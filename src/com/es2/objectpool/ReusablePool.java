package com.es2.objectpool;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class ReusablePool {

    private static ReusablePool instance;

    private ArrayList<HttpURLConnection> available;
    private ArrayList<HttpURLConnection> inUse;

    private int maxPoolSize = 10;

    private ReusablePool() {
        available = new ArrayList<>();
        inUse = new ArrayList<>();
    }

    public static synchronized ReusablePool getInstance() {
        if (instance == null) {
            instance = new ReusablePool();
        }
        return instance;
    }

    // Adquirir conexão
    public synchronized HttpURLConnection acquire() throws IOException, PoolExhaustedException {
        HttpURLConnection conn;
        if (!available.isEmpty()) {
            conn = available.remove(0);
        } else if (inUse.size() < maxPoolSize) {
            URL url = new URL("https://www.ipv.pt");
            conn = (HttpURLConnection) url.openConnection();
        } else {
            throw new PoolExhaustedException();
        }
        inUse.add(conn);
        return conn;
    }

    // Libertar conexão
    public synchronized void release(HttpURLConnection conn) throws ObjectNotFoundException {
        if (!inUse.contains(conn)) {
            throw new ObjectNotFoundException();
        }
        inUse.remove(conn);
        available.add(conn);
    }

    // Reset da pool
    public synchronized void resetPool() {
        available.clear();
        for (HttpURLConnection conn : inUse) {
            available.add(conn);
        }
        inUse.clear();
    }

    // Alterar tamanho máximo da pool
    public synchronized void setMaxPoolSize(int size) {
        this.maxPoolSize = size;
    }
}