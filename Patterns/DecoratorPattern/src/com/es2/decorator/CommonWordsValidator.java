package com.es2.decorator;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class CommonWordsValidator extends Decorator{

    public CommonWordsValidator(AuthInterface auth) {
        super(auth);
    }

    @Override
    public void auth(String username, String password) throws AuthException {
        super.auth(username, password);
    }

    public String getHTTPRequest(String word) throws Exception {
        StringBuilder result = new StringBuilder();
        URL url = new URL("https://api.dictionaryapi.dev/api/v2/entries/en/" + word + "?format=json");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB;     rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13 (.NET CLR 3.5.30729)");
        conn.setRequestMethod("GET");
        BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = rd.readLine()) != null) {
            result.append(line);
        }
        rd.close();
        return result.toString();
    }
}
