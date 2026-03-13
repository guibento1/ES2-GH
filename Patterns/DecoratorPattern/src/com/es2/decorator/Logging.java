package com.es2.decorator;

public class Logging extends Decorator{

    public Logging(AuthInterface auth) {
        super(auth);
    }

    @Override
    public void auth(String username, String password) throws AuthException {
        long ts = System.currentTimeMillis();
        System.out.println(ts + ",auth()");
        super.auth(username, password);
    }
}

