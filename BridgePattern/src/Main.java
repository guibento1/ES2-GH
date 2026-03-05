import com.es2.bridge.APIMoodle;
import com.es2.bridge.APIRequest;
import com.es2.bridge.APIRequestContentAggregator;
import com.es2.bridge.ServiceNotFoundException;

public class Main {
    public static void main(String[] args) {
        // serviço concreto (implementação)
        APIMoodle moodle = new APIMoodle();

        // abstração normal
        APIRequest request = new APIRequest();

        // abstração especializada (agregador)
        APIRequestContentAggregator aggregator = new APIRequestContentAggregator();

        // registar o mesmo serviço nas duas abstrações
        String serviceId1 = request.addService(moodle);
        String serviceId2 = aggregator.addService(moodle);

        // adicionar conteúdos através da APIRequest normal
        try {
            String c1 = request.setContent(serviceId1, "A");
            String c2 = request.setContent(serviceId1, "B");
            String c3 = request.setContent(serviceId1, "C");

            System.out.println("IDs criados: " + c1 + ", " + c2 + ", " + c3);

            // ler um conteúdo específico
            String one = request.getContent(serviceId1, c2);
            System.out.println("Conteúdo individual (c2): " + one);

            // ler todos agregados via aggregator (deve imprimir ABC)
            String all = aggregator.getContent(serviceId2, "ignored");
            System.out.println("Conteúdo agregado: " + all);
        } catch (ServiceNotFoundException e) {
            e.printStackTrace();
        }

        // testar ServiceNotFoundException
        try {
            request.getContent("999", "1");
        } catch (ServiceNotFoundException e) {
            System.out.println("Apanhou ServiceNotFoundException para serviceId inexistente");
        }
    }
}
