package tp.es2.logging;

import java.util.ArrayList;
import java.util.List;

public class LogGroup implements LogComponent {
    private String category;
    private List<LogComponent> components = new ArrayList<>();

    public LogGroup(String category) {
        this.category = category;
    }

    public void add(LogComponent log) {
        components.add(log);
    }

    public void remove(LogComponent log) {
        components.remove(log);
    }

    @Override
    public void log(Logger logger) {
        for (LogComponent component : components) {
            component.log(logger);
        }
    }

    @Override
    public String getCategory() {
        return category;
    }
}
