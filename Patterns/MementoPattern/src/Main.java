import com.es2.memento.*;

public class Main {
    public static void main(String[] args) {
        try {
            Server s = new Server();
            BackupService backup = new BackupService(s);

            // Estado inicial: []
            backup.takeSnapshot();              // snapshot 0

            s.addStudent("Maria José");
            // Estado: ["Maria José"]
            backup.takeSnapshot();              // snapshot 1

            s.addStudent("Manuel António");
            // Estado: ["Maria José", "Manuel António"]
            System.out.println("Antes do restore: " + s.getStudentNames().size()); // 2

            backup.restoreSnapshot(1);          // volta ao snapshot 1
            System.out.println("Depois do restore: " + s.getStudentNames().size()); // 1

            System.out.println("Alunos atuais: " + s.getStudentNames());
        } catch (ExistingStudentException | NotExistingSnapshotException e) {
            e.printStackTrace();
        }
    }
}
