import java.util.*;

public class Cal {

    static void menu(){
        System.out.println("-:Basic Calculator:-");
        System.out.println("1. Addition");
        System.out.println("2. subtraction");
        System.out.println("3. multiplication");
        System.out.println("4. division");
        System.out.println("5. square root");
        System.out.println("6. exponentiation");
        System.out.println("7. temperature");
        System.out.println("8. currency");
        System.out.print("Enter your choice:");
    }

    static double add(double num1,double num2){
        return num1 + num2;
    }

    static double sub(double num1,double num2){
        return num1 - num2;
    }

    static double mul(double num1,double num2){
        return num1 * num2;
    }

    static double div(double num1,double num2){
        if(num2 == 0){
            throw new IllegalArgumentException("Error: Division by zero is not allowed!");
        }
        return num1 / num2;
    }

    static double seq(double num){
        return Math.sqrt(num);
    }

    static double power(double num1,double num2){
        return Math.pow(num1, num2);
    }

    static void tem(int choice,double tem){
        switch (choice) {
            case 1:
            System.out.println("°C:" + ((tem - 32) * 5 / 9));
                break;

            case 2:
            System.out.println("°F:" + ((tem * 9 / 5) + 32));
                break;
        }
    }

    static void currency(int choice,double cur){
        switch (choice) {
            case 1:
            System.out.println("Ans:" + cur/83.55 + "$" );
                break;

            case 2:
            System.out.println("Ans:" + cur*83.55 + "INR" );
                break;
        }

    }


    public static void main(String[] args) {
      try{
        Scanner sc = new Scanner(System.in);

        menu();
        int choice = sc.nextInt();

            switch (choice) {
                case 1:
                System.out.print("Enter first number:");
                double num1 = sc.nextDouble();

                System.out.print("Enter second number:");
                double num2 = sc.nextDouble();

                System.out.println("Ans:" + add(num1, num2)); 
                break;

                case 2:
                System.out.print("Enter first number:");
                double num3 = sc.nextDouble();

                System.out.print("Enter second number:");
                double num4 = sc.nextDouble();

                System.out.println("Ans:" + sub(num3, num4)); 
                break;

                case 3:
                System.out.print("Enter first number:");
                double num5 = sc.nextDouble();

                System.out.print("Enter second number:");
                double num6 = sc.nextDouble();

                System.out.println("Ans:" + mul(num5, num6)); 
                break;

                case 4:
                System.out.print("Enter first number:");
                double num7 = sc.nextDouble();

                System.out.print("Enter second number:");
                double num8 = sc.nextDouble();

                System.out.println("Ans:" + div(num7, num8)); 
                break;

                case 5:
                System.out.print("Enter number:");
                double num9 = sc.nextDouble();

                if(num9 < 0){
                    System.out.println("Error:Invalid input!");
                }else{
                    System.out.println("Ans:" + seq(num9)); 
                }
                break;

                case 6:
                System.out.print("Enter number:");
                double num10 = sc.nextDouble();

                System.out.print("Enter number's exponentiation:");
                double num11 = sc.nextDouble();

                System.out.println("Ans:" + power(num10, num11)); 
                break;

                case 7:
                System.out.println("1. fahrenheit for  to celsius");
                System.out.println("2. for celsius to fahrenheit");
                System.out.print("Enter your choice:");
                int choice2 = sc.nextInt();
                if( choice2 != 1 && choice2 != 2){
                    System.out.println("Error:This option not valid!");
                }else{
                System.out.print("Enter your temperature:");
                double temp = sc.nextDouble();
                tem(choice2,temp);}
                break;

                case 8:
                System.out.println("1. INR to USD");
                System.out.println("2. for USD to INR");
                System.out.print("Enter your choice:");
                int choice3 = sc.nextInt();
                if( choice3 != 1 && choice3 != 2){
                    System.out.println("Error:This option not valid!");
                }else{
                System.out.print("Enter your amount:");
                double amount = sc.nextDouble();
                currency(choice3,amount);}
                break;

                default:
                System.out.println("Error:Invalid option!");
                    break;
            }

            sc.close();

        } catch (Exception e){
            System.out.println("Error:Invalid input!");
        }
    }
}
