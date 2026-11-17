import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Test {
    public static void main(String[] args) throws Exception {
        Path directory = Files.createTempDirectory("kata5-");
        String classPath = Path.of(Test.class.getProtectionDomain()
            .getCodeSource().getLocation().toURI()).toString();
        Process process = new ProcessBuilder(
            Path.of(System.getProperty("java.home"), "bin", "java").toString(),
            "-cp", classPath, "Main"
        ).directory(directory.toFile()).redirectErrorStream(true).start();
        String output = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
        int status = process.waitFor();
        if (status != 0) throw new AssertionError(output);
        Path csv = directory.resolve("dispatches.csv");
        List<String> lines = Files.readAllLines(csv, StandardCharsets.UTF_8);
        Files.delete(csv);
        Files.delete(directory);
        require(output, "Quote PK-101: EUR 5.35");
        require(output, "Quote PK-102: EUR 41.73");
        require(output, "Quote PK-103: EUR 16.69");
        require(output, "Revenue: EUR 63.77");
        require(output, "Audit entries: 6");
        if (lines.size() != 4) throw new AssertionError("Expected three dispatch rows");
        require(lines.get(1), "PK-101,ES,1.5,false,false,5.35");
        require(lines.get(2), "PK-102,FR,3.0,true,true,41.73");
        require(lines.get(3), "PK-103,PT,2.2,false,true,16.69");
        System.out.println("Test passed");
    }

    private static void require(String output, String expected) {
        if (!output.contains(expected)) throw new AssertionError("Missing: " + expected);
    }
}
