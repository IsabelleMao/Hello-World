import java.util.Scanner;

/*
**    Coded by Isabelle Mao
**    December 1, 2016
**    Junior Question 2, CCC Waterloo competition 2016
*/
public class juniorCCC2015J2
{
   public static void main (String[] args)
   {
      Scanner scanner = new Scanner(System.in);
      int num1, num2, num3, num4; //row 1
      int num5, num6, num7, num8;
      int num9, num10, num11, num12; //row 3, etc.
      int num13, num14, num15, num16;

      num1 = scanner.nextInt();
      num2 = scanner.nextInt();
      num3 = scanner.nextInt();
      num4 = scanner.nextInt();
      num5 = scanner.nextInt();
      num6 = scanner.nextInt();
      num7 = scanner.nextInt();
      num8 = scanner.nextInt();
      num9 = scanner.nextInt();
      num10 = scanner.nextInt();
      num11 = scanner.nextInt();
      num12 = scanner.nextInt();
      num13 = scanner.nextInt();
      num14 = scanner.nextInt();
      num15 = scanner.nextInt();
      num16 = scanner.nextInt();
      
      int row1 = num1 + num2 + num3 + num4;
      int row2 = num5 + num6 + num7 + num8;
      int row3 = num9 + num10 + num11 + num12;
      int row4 = num13 + num14 + num15 + num16; //Rows, which are horizontal.
      
      int col1 = num1 + num5 + num9 + num13;
      int col2 = num2 + num6 + num10 + num14;
      int col3 = num3 + num7 + num11 + num15;
      int col4 = num4 + num8 + num12 + num16; //Columns, which are vertical.
      
      int magicSum = row1; //A sum. If magic, all rows/columns will add up to this.
      
      if(row2 == magicSum && row3 == magicSum
       && row4 == magicSum && col1 == magicSum
        && col2 == magicSum && col3 == magicSum
        && col4 == magicSum ){
         System.out.print("Magic");
      }
      else{
         System.out.print("Not magic");
         //:(
      }
      
   }//Static void
} //public class