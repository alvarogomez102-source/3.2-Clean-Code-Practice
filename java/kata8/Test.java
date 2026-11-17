import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class Test {
    public static void main(String[] args) throws Exception {
        Path directory = Files.createTempDirectory("kata3-");
        String classPath = Path.of(Test.class.getProtectionDomain()
            .getCodeSource().getLocation().toURI()).toString();
        Process process = new ProcessBuilder(
            Path.of(System.getProperty("java.home"), "bin", "java").toString(),
            "-cp", classPath, "Main"
        ).directory(directory.toFile()).redirectErrorStream(true).start();
        String output = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
        int status = process.waitFor();
        Files.delete(directory);
        if (status != 0) throw new AssertionError(output);
        require(output, "EMAIL to ada@example.org: Your account is ready");
        require(output, "SMS to +34000000000: URGENT: Your parcel will arrive today");
        require(output, "AUDIT email -> ada@example.org");
        require(output, "AUDIT sms -> +34000000000");
        System.out.println("Test passed");
    }

    private static void require(String output, String expected) {
        if (!output.contains(expected)) throw new AssertionError("Missing: " + expected);
    }
}
