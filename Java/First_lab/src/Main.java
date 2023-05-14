import java.util.Scanner;

class Main{
    public static void main(String[] args){
        System.out.println("Hello");
        Field field = new Field(10,10);
        field.fill();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter unit to move (S/J): ");
        String unitToMove = scanner.nextLine();
        Unit unit;
        if(unitToMove.equalsIgnoreCase("S"))
        {
            unit=new Standard(field,5,5);
        }
        else
        {
            unit = new Jumper(field,5,5);
        }
        field.output(unit);
        int tip = 3;
        char key;
        Scanner reader = new Scanner(System.in);
        do{
            System.out.println("Press one of the keys between r, l, d and u to move right, left, down and up respectively: ");
            key = reader.next().charAt(0);
            unit.move(key);
            field.output(unit);
            System.out.println("If you want to stop the program, press the key 'e'.");
        }while(key != 'e'&& tip!=0);

    }
}