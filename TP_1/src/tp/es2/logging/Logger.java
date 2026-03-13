package tp.es2.logging;

public class Logger {
    public void log(LogEntry entry) {
        LogConfig config = LogConfig.getInstance();

        // 1. Filtragem por nível (só loga se entry.level >= globalLevel)
        if (entry.getLevel().ordinal() < config.getGlobalLevel().ordinal()) {
            return; // ignora este log
        }

        // 2. Ler o pattern configurado
        String pattern = config.getFormatPatterns();

        // 3. Construir a mensagem formatada
        String formatted = pattern
                .replace("%level", entry.getLevel().name())
                .replace("%message", entry.getMessage());

        // (Se quiseres já %time)
        formatted = formatted.replace("%time", String.valueOf(entry.getTimestamp()));

        // 4. Por agora, destino único: consola
        System.out.println(formatted);
    }
}
