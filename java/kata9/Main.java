import java.util.List;

public class Main {
    public static void main(String[] args) {
        ReportJob job = new ReportJob();
        job.prepare("Monthly sales", List.of(
            new Sale("Keyboard", 3, 45.0),
            new Sale("Mouse", 5, 18.0)
        ));
        System.out.println(job.run("csv"));
        System.out.println(job.run("json"));
    }
}
