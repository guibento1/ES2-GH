package com.es2.decorator;

public class Auth implements AuthInterface {
    public void auth(String username, String password) throws AuthException {
        if (username.equals("admin") && password.equals("admin")) {
            System.out.println("Auth successful");
        } else {
            throw new AuthException();
        }
    }
}
