import com.es2.factorymethod.FactoryProduct;
import com.es2.factorymethod.Product;
import com.es2.factorymethod.Computer;
import com.es2.factorymethod.Software;

public class Main {
    public static void main(String[] args) throws Exception {
        Product p1 = FactoryProduct.makeProduct("computer");
        Product p2 = FactoryProduct.makeProduct("software");

        Computer c = (Computer) p1;
        c.setBrand("Dell");

        Software s = (Software) p2;
        s.setBrand("Windows");

        System.out.println(c.getBrand());
        System.out.println(s.getBrand());
    }
}
