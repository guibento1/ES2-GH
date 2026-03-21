package tp.es2.logging;

public class LogDestinationPool {

    private List<LogDestination> available = new ArrayList<>(); // disponíveis
    private List<LogDestination> inUse     = new ArrayList<>(); // em uso

    public LogDestinationPool(List<LogDestination> initial) {
        available.addAll(initial);
    }

    public LogDestination acquire() {
        if (available.isEmpty()) {
            throw new RuntimeException("Sem destinos disponiveis no pool");
        }
        LogDestination destination = available.remove(0);
        inUse.add(destination);
        return destination;
    }

    public void release(LogDestination destination) {
        inUse.remove(destination);
        available.add(destination); // devolve ao pool para reutilização
    }

    public int availableCount() { return available.size(); }
    public int inUseCount()     { return inUse.size(); }
}
