package tp.es2.logging;

public class ConsoleDestination implements LogDestination {
    @Override
    public void write(LogEntry entry, String formattedMessage) {
        System.out.println(formattedMessage);
    }
}
