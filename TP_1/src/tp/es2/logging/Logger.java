package tp.es2.logging;

import java.util.List;

public class Logger {
    private List<LogDestination> destinations;

    public Logger(List<LogDestination> destinations){
        this.destinations = destinations;
    }

    public void log(LogEntry entry){
        LogConfig config = LogConfig.getInstance();

        //1. Filtragem por nível (só loga se entry.level >= globalLevel)
        if(entry.getLevel().ordinal() < config.getGlobalLevel().ordinal()){
            return;
        }

        //2. Ler o pattern configurado
        String pattern = config.getFormatPatterns();

        //3. Construir a mensagem formatada
        String formatted = pattern
                .replace("%level", entry.getLevel().name())
                .replace("%message", entry.getMessage())
                .replace("%time", String.valueOf(entry.getTimestamp()));

        //4. Bridge - delega para cada destino configurado
        for (LogDestination destination : destinations){
            destination.write(entry,formatted);
        }
    }
}