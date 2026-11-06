import com.es2.factorymethod.FactoryProduct;
import com.es2.factorymethod.Product;

public class Main {
    public static void main(String[] args) throws Exception{
        Product c = FactoryProduct.makeProduct("computer");
        Product s = FactoryProduct.makeProduct("software");
    }
}
