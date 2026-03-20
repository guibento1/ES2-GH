package tp.es2.logging;

import java.io.FileWriter;
import java.io.IOException;

public class FileDestination implements LogDestination {
    private String filePath;

    public FileDestination(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public void write(LogEntry entry, String formattedMessage) {
        try (FileWriter writer = new FileWriter(filePath, true)) {
            writer.write(formattedMessage + "\n");
        } catch (IOException e) {
            System.err.println("Erro ao escrever no ficheiro: " + e.getMessage());
        }
    }
}
