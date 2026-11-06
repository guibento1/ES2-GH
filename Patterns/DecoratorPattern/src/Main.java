import com.es2.decorator.*;


public class Main {
    public static void main(String[] args) {
        // Componente base
        AuthInterface auth = new Auth();

        // Decorar com logging
        auth = new Logging(auth);

        // Decorar com validação de palavras comuns
        auth = new CommonWordsValidator(auth);

        try {
            // Tenta autenticar
            auth.auth("admin", "admin");
        } catch (AuthException e) {
            System.out.println("Authentication failed: " + e.getMessage());
        }
    }
}
