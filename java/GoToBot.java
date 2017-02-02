/*|
|*|Project Name: Unit 4 Project- Isabelle Mao
|*|Description: A GoToBot that can face
|*|any given avenue or street and go there.
|*|Author: Isabelle Mao 
|*|Date started: 1/31/2017
|*|Date finished: 1/31/2017
|*/

import becker.robots.*;

//GoToBot is a subclass of RobotSE.
public class GoToBot extends RobotSE
{

   /*All the arguments of RobotSE except for number of Things,
   which is irrelevant in this project. */
   public GoToBot(City aCity, int str, int ave, Direction dir)
	{
      //The user specifies the city, street, avenue and direction.
		super(aCity, str, ave, dir);
   }
	
	//Face a specified direction
   public void faceDirection(Direction dir)
   {
      //turn left until it's facing that direction
      while (this.getDirection() != dir)
      {
         this.turnLeft(); 
      }
   }
   
   //Face a specified avenue
	public void faceAve(int ave)
	{
      /*If the robot is at an avenue to the left of the specified avenue */
      if (this.getAvenue() < ave)
      {
         //Turn east, because the avenue is to its left.
         this.faceDirection(Direction.EAST);
      }
      
      /*If the robot is at an avenue to the right of the specified avenue */
      else if (this.getAvenue() > ave)
      {
         //Turn west, because the avenue is to its left.
         this.faceDirection(Direction.WEST);
      }
 
      /*If the robot is ON the specified avenue */
      else
      {
         //face north (it's aesthetically pleasing)
         this.faceDirection(Direction.NORTH);
      }
      
	} //end of the method faceAve
   
   //Face a specified street
	public void faceStr(int str)
	{
      /*If it's at a street over the specified street */
      if (this.getStreet() < str)
      {
         //Turn south, because the avenue is under it.
         this.faceDirection(Direction.SOUTH);
      }
      
      /*If it's at a street under the specified street */
      else if (this.getStreet() > str)
      {
         //Turn north, because the street is above it.
         this.faceDirection(Direction.NORTH);
      }
      
      /*If it's ON the specified street) */
      else
      {
         //Face East
         this.faceDirection(Direction.WEST);
      }
      
	}//end of the method faceStr
   
   //Face the avenue 0
   public void faceAveZero()
   {
      this.faceAve(0);
   }
   
   //Face the street 0
   public void faceStrZero()
   {
      this.faceStr(0);
   }
   
   //Move to the specified avenue
   public void moveToAve(int ave)
   {
      //First, face that avenue
      this.faceAve(ave);
      //Move forward until it's AT that avenue
      while (this.getAvenue() != ave)
      {
         this.move();
      }
   }
   
   //Move to the specified street
   public void moveToStr(int str)
   {
      //First, face that street
      this.faceStr(str);
      //Move forward until it's AT that street
      while (this.getStreet() != str)
      {
         this.move();
      }
   }
   
   //Move to the 0th avenue
   public void moveToAveZero()
   {
      this.moveToAve(0);
   }
   
   //Move to the 0th street
   public void moveToStrZero()
   {
      this.moveToStr(0);
   }
   
   //Go to any given intersection
   public void goTo(int str, int ave)
   {
      //Go to the street or avenue.
      this.moveToStr(str);
      this.moveToAve(ave);
   }
   
   //Go to the origin (0,0)
   public void goToOrigin()
   {
      this.goTo(0, 0);
   }
   
} //end of class GoToBot
