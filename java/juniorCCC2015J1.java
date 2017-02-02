import java.util.Scanner;

/*
**    Coded by Isabelle Mao
**    December 1, 2016
**    Junior Question 1, CCC Waterloo competition 2015
*/
public class juniorCCC2015J1
{
   public static void main (String[] args)
   {
      Scanner scanner = new Scanner(System.in);
      int month, day;
      
      month = scanner.nextInt(); //month and day input
      day = scanner.nextInt();
      
      if (month == 2 && day == 18){ //Feb 18
         System.out.print("Special");
      }
      else if(month < 3){
         if(month == 2){ //February
            if(day < 18){ //Before 18
               System.out.print("Before");
            }
            else{ //After 18
               System.out.print("After");
            }
          }
         else{ //January
            System.out.print("Before");       
             }
         }
      else{ //March+
         System.out.print("After");
      }
   }//Static void
} //public class