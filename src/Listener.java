import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Listener implements ActionListener {
    private Calculateentry entry;
    double result = 0;
    JButton button;
    public Listener(JButton button){
        this.button = button;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        //Действия при нажатии на кнопку расчета
        String number1String = entry.getField1().getText(); //Мы получаем значение в первом поле
        double number1 = Double.parseDouble(number1String); //Преобразуйте это значение в число

        String number2String = entry.getField2().getText(); //Получаем значение во втором поле
        double number2 = Double.parseDouble(number2String); //Преобразуйте это значение в число

        String operateur = entry.getModelOperateurs().getSelectedOperateur();
        if("+".equals(operateur)){
            result = number1 + number2;
        } else if ("-".equals(operateur)) {
            result = number1 - number2;
        } else if ("*".equals(operateur)) {
            result = number1 * number2;
        } else if ("/".equals(operateur)) {
            result = number1 / number2;
        }
        ++this.result;
        this.button.setText("Result = " + " " + this.result);
    }
}
