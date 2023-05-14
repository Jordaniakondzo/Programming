abstract class Unit{
    int tip, score;
    int x, y;
    Field field;

    Unit(Field field, int x, int y){
        this.field = field;
        this.x = x;
        this.y = y;
        tip = 3;
        score = 0;
    }

    abstract void move(char key);

}

class Standard extends Unit{
    Standard(Field field, int x, int y){
        super(field, x, y);
    }
    void move(char key)
    {
        int nx=x;
        int ny=y;
        switch(key)
        {
            case 'u':
                ny--;
                break;
            case 'l':
                nx--;
                break;
            case 'd':
                ny++;
                break;
            case 'r':
                nx++;
                break;
            default: System.out.println("...");
                return;
        }
        if(field.illegal_Move(nx, ny))
        {
            x=nx;
            y=ny;
            if(field.collect(x, y))
            {
                score++;
                System.out.println("You win a coin");
                System.out.println("Now you have a score of: " + score);
            }
            if(field.stepOnTrap(x, y))
            {
                tip--;
                System.out.println("You lost a live");
                System.out.println("Now you have " + tip + " live");
            }
        }
        else{
            System.out.println("Illegal move!");
        }
        if(tip==0)
        {
            System.out.println("You lost all the lives, now you can't keep playing");
            System.exit(0);
        }
        if(key == 'e')
        {
            System.out.println("Stopping of program");
            System.exit(0);
        }
        x=nx;
        y=ny;
    }
}

class Jumper extends Unit{
    Jumper(Field field, int x, int y){
        super(field, x, y);
    }
    void move(char key)
    {
        int nx=x;
        int ny=y;
        switch(key)
        {
            case 'u':
                ny-=2;
                break;
            case 'l':
                nx-=2;
                break;
            case 'd':
                ny+=2;
                break;
            case 'r':
                nx+=2;
                break;
            default: System.out.println("...");
                return;
        }
        if(field.illegal_Move(nx, ny))
        {
            x=nx;
            y=ny;
            if(field.collect(x, y))
            {
                score++;
                System.out.println("You win a coin");
                System.out.println("Now you have a score of: " + score);
            }
            if(field.stepOnTrap(x, y))
            {
                tip--;
                System.out.println("You lost a live");
                System.out.println("Now you have " + tip + " live");
            }
        }
        else{
            System.out.println("Illegal move!");
            return;
        }
        if(tip==0)
        {
            System.out.println("You lost all the lives, now you can't keep playing");
            System.exit(0);
        }
        if(key == 'e')
        {
            System.out.println("Stopping of program");
            System.exit(0);
        }
        x=nx;
        y=ny;
    }
}