import javax.swing.*;

public class Main {
    public static void main(String[] args){
        SwingUtilities.invokeLater(() -> {
            Calculateentry entry = new Calculateentry();
            entry.setVisible(true);
            Registration registration = new Registration();
                    registration.setVisible(true);
        });
    }
}