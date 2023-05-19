import javax.swing.*;
import java.awt.*;

public class Calculateentry extends JFrame{
    public Calculateentry(){
        super();
        build(); //Мы инициализируем наше окно
    }
    private void build(){
        setTitle("Calculate"); //Даем название приложению
        setSize(400,200); //Задаем размер нашему окну
        setLocationRelativeTo(null); //Центрируем окно на экране
        setResizable(true); //Разрешаем изменение размера окна
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Приложению говорят закрыться при нажатии на крестик

        setContentPane(buildContentPane());
    }
    private JTextField field1;
    private JTextField field2;
    private JComboBox list;
    private JPanel buildContentPane() {
        JPanel panel = new JPanel();
        panel.setBackground(Color.GRAY);
        panel.setLayout(new FlowLayout(FlowLayout.CENTER,10,5));
        add(panel, BorderLayout.CENTER);

        field1 = new JTextField();
        field1.setColumns(10);
        panel.add(field1);
        list = new JComboBox((new OperateursModel()));
        panel.add(list);

        field2 = new JTextField();
        field2.setColumns(10);
        panel.add(field2);

        JButton button = new JButton("Calculate");
        Listener listener = new Listener(button);
        button.addActionListener(listener);
        panel.add(button);

        JLabel label = new JLabel("Result = ");
        panel.add(label);
        return panel;
    }

    public JTextField getField1() {

        return field1;
    }

    public JTextField getField2() {

        return field2;
    }
    public OperateursModel getModelOperateurs(){
        return (OperateursModel)list.getModel();
    }
}
