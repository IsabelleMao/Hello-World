/*|
|*|Project Name: 
|*|Description:
|*|
|*|Author: Isabelle Mao    
|*|Date started: ~~/~~/~~~~
|*|Date finished: ~~/~~/~~~~
|*/

import becker.robots.*;

public class Classplate extends Robot 
{
	
   public Classplate(City aCity, int aStreet, int anAvenue, Direction aDirection)
	{
		super(aCity, 2, 2, Direction.NORTH); Change!

	}
	
	//Example method.
	public void turnAround()
	{
		this.turnLeft();
		this.turnLeft();
	}
}
