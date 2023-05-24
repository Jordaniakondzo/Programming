import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Registration extends JFrame implements ActionListener {
    JLabel label1, label2, label3, label4, label5;
    JTextField t1, t2;
    JRadioButton male, female;
    JComboBox<String> day, month, year;
    JTextArea ta1, screen;
    JCheckBox terms;
    JButton submit;
    JLabel msg;
    Registration(){
        super("Registration");
        setSize(700,500);
        setLocationRelativeTo(null); //Центрируем окно на экране
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(null);

        Container c = getContentPane();
        c.setLayout(null);
        label1 = new JLabel("Name");
        label1.setBounds(20,50,100,20);
        c.add(label1);

        t1 = new JTextField();
        t1.setBounds(130,50,100,20);
        c.add(t1);

        label2 = new JLabel("Mobile");
        label2.setBounds(20,100,100,20);
        c.add(label2);

        t2 = new JTextField();
        t2.setBounds(130,100,100,20);
        c.add(t2);

        label3 = new JLabel("Gender");
        label3.setBounds(20,150,100,20);
        c.add(label3);

        male = new JRadioButton("Male");
        male.setBounds(130,150,80,20);
        male.setSelected(true);
        c.add(male);

        female = new JRadioButton("Female");
        female.setBounds(220,150,80,20);
        female.setSelected(true);
        c.add(female);

        ButtonGroup gen = new ButtonGroup();
        gen.add(male);
        gen.add(female);

        label4 = new JLabel("Date of birthday");
        label4.setBounds(20,200,100,20);
        c.add(label4);

        String [] days = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"};
        String[] months = {"Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sep","Oct","Nov","Dec"};
        String[] years = {"2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990"};

        day = new JComboBox<>(days);
        day.setBounds(130,200,50,20);
        month = new JComboBox<>(months);
        month.setBounds(190,200,50,20);
        year = new JComboBox<>(years);
        year.setBounds(250,200,60,20);

        c.add(day);
        c.add(month);
        c.add(year);

        label5 = new JLabel("Address");
        label5.setBounds(20,250,100,20);
        c.add(label5);

        ta1 = new JTextArea();
        ta1.setBounds(130,240,200,50);
        c.add(ta1);

        //creates a new checkbox with no text
        terms = new JCheckBox("Please accept terms conditions");
        terms.setBounds(50,300,200,20);
        c.add(terms);

        submit = new JButton("Submit");
        submit.setBounds(150,350,80,20);
        submit.addActionListener(this);
        c.add(submit);

        screen = new JTextArea();
        screen.setBounds(350,50,300,300);
        c.add(screen);

        msg = new JLabel("");
        msg.setBounds(20,400,250,20);
        c.add(msg);
        c.setBackground(Color.gray);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(terms.isSelected()){
            msg.setText("Registration successful !!");
            String name = t1.getText();
            String mobile = t2.getText();
            String gender = "male";
            if(female.isSelected()){
                gender = "female";
            }
            JOptionPane.showMessageDialog(Registration.this, gender); // MessageDialog to show information selected radio buttons.
            String dob = day.getSelectedItem()+"/"+month.getSelectedItem()+"/"+year.getSelectedItem();
            String address = ta1.getText();
            screen.setText("Name : "+name+"\n"+"Mobile : "+mobile+"\n"+"Gender : "+gender+"\n"+"Date of birthday : "+dob+"\n"+"Address : "+address);
        }
        else{
            msg.setText("Accept terms and conditions to submit.");
            screen.setText("");
        }
    }
}
