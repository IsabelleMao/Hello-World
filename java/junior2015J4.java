/*
**    Coded by Isabelle Mao
**    December 12, 2016
**    Junior Question 4, CCC Waterloo competition 2016
*/

import java.util.Scanner;
public class junior2015J4
{
   public static void main (String[] args)
   {  
      //Scanner stuff
      Scanner scanner = new Scanner(System.in);
      String input = scanner.next();
      
      //Set the rush hour start and end times
      int rushHourStart1 = 7;
      int rushHourEnd1 = 10;
      int rushHourStart2 = 15;
      int rushHourEnd2 = 19;
      
      //Get the hour and minute from input
      String strHour = input.substring(0, 2);
      String strMinute = input.substring(3, 5);
      
      //Convert the strings to usable integers
      int hour = Integer.parseInt(strHour);
      int minute = Integer.parseInt(strMinute);
      
      for (int i = 1; i <= 120; i++)
      {
         //If it's currently rush hour
         if (hour >= rushHourStart1 && hour < rushHourEnd1 ||
         hour >= rushHourStart2 && hour < rushHourEnd2)
         {
            //Halfspeed
            minute += 2;
            //Start a new hour is minute is sixty
            if (minute == 60)
            {
               hour += 1;
               minute = 0;
               //Start a new day if hour is twenty four
               if (hour == 24)
               {
                  hour = 0;
               }//hour if
            } //minute if
         }//Deciding rush hour
         else
         {
            //just add one minute
            minute += 1;
            //new hour is minute = sixty
            if (minute == 60)
            {
               hour += 1;
               minute = 0;
               //Start a new day if hour is twenty four
               if (hour == 24)
               {
                  hour = 0;
               }//hour if
            } //minute if
         }//else
      }//big for
      
      // I know this is wrong by I'm tired...
      System.out.println(hour + ":"+ minute);
   }//Static void
} //public class