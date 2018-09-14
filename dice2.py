#input from  user to roll the dice
a=str(input("enter r to roll the dice and q to quit"))
i=0
import random as ra
while i<5:
	if(a=='r'):
		print(ra.randint(1,6))
		break
	else:
		if(a=='q'):
			break



