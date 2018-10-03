#rock paper 
import random 
p={1:'r',2:'p',3:'s'}
while True:
	z=str(input("Enter a to play and b to quit "))
	if(z=='a'):
		yc=input("your choice r/p/s:  ")
		cc=p[random.randint(1,3)]

		print("computer gave: ",cc)

		if(yc=='r' and cc=='p'):
			print("Computer Wins ")
		elif(yc=='r' and cc=='r'):
			print("Draw ")
		elif(yc=='r' and cc=='s'):
			print("You win ")
		elif(yc=='p' and cc=='r'):
			print("You win")
		elif(yc=='p' and cc=='p'):
			print("Draw ")	
		elif(yc=='p' and cc=='s'):
			print("You win")
		elif(yc=='s' and cc=='r'):
			print("Computer wins")			
		elif(yc=='s' and cc=='p'):
			print("You win ")
		elif(yc=='s' and cc=='s'):
			print("Draw ")
	else:
		print("Bye ")
		exit() 
						