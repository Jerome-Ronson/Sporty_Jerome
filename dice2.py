#input from  user to roll the dice
i=0
import random as ra
while i<5:
	a=str(input("enter r to roll the dice and q to quit"))
	if(a=='r'):
		print(ra.randint(1,6))
	else:
		print("exit")
		break
		
	
		



