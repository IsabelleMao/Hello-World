import java.util.Scanner;

/*
**    Coded by Isabelle Mao
**    December 1, 2016
**    Junior Question 3, CCC Waterloo competition 2016
*/
public class juniorCCC2015J3REAL
{
   public static void main (String[] args)
   {  
      //Scanner stuff
      Scanner scanner = new Scanner(System.in);
      String input = scanner.next();
     
      //The palindromes, used inside the for loop.
      String longestPalindrome = null;
      String currentPalindrome = "xo";
      int lengthOfLongest = 1;      
      int length = input.length(); //length of the string
      
      for(int currentLetter = 1; currentLetter < length-2; currentLetter++) //From the SECOND letter to the penultimate letter, adding one to i each time.
      {
         //The current, previous and next letters looping.
         char current = input.charAt(currentLetter);
         char previous = input.charAt(currentLetter-1);
         char next = input.charAt(currentLetter+1);
         
         int indexOfNext = currentLetter + 1;
         int indexOfPrev = currentLetter - 1;
         
         if(previous == next) //If there is a 3-letter palindrome
         {
            currentPalindrome = input.substring(currentLetter-1, currentLetter+2); //Changes the current palindrome to the one found
            
            while(indexOfPrev >= 0 && indexOfNext < length && input.charAt(indexOfNext) == input.charAt(indexOfPrev)) //If first and last letters of a 5-letter palindrome are the same
            {
               currentPalindrome = input.substring(indexOfPrev, indexOfNext + 1);
               indexOfPrev -= 1;
               indexOfNext += 1;
               int newLength = currentPalindrome.length();
               if (newLength > lengthOfLongest)
               {
                  lengthOfLongest = newLength;
                  longestPalindrome = input.substring(indexOfPrev + 1, indexOfNext);
               }
               
            }
                           
         }
         
      } //End of for loop
      
      System.out.println(lengthOfLongest); //the thing u have 2 print in teh end
   }//Static void
} //public class