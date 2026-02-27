import com.es2.singleton.Registry;

public class Main {
    public static void main(String[] args) {

        Registry config1 = Registry.getInstance();
        config1.setPath("C:/ficheiros");
        config1.setConnectionString("jdbc:mysql://localhost/mydb");

        Registry config2 = Registry.getInstance();

        System.out.println(config2.getPath());
        System.out.println(config1 == config2);
    }
}
