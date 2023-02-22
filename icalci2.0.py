print("\nWelcome in our calculator"
,"\nPlease select your operator from following:")
print(
 "\n(1) For Addition  or Subtraction select : O"
,"\n(2) For Multiplication select : M "
,"\n(3) For Division select : D"
,"\n(4) For Taking Power select : P"
,"\n(5) For Taking squre root select : Sr    (NOTE: FOR SECOND NUMBER PLEASE DON'T WRITE ANYTHING.)"
,"\n(6) For Taking cube root select : Cr  (NOTE: FOR SECOND NUMBER PLEASE DON'T WRITE ANYTHING.)  "
,"\n(7) For Taking Modulo select : Md "
,"\n(8) For taking percentage select : Pr   ( NOTE : FOR TAKING PERCENTAGE PLEASE WRITE YOUR GIVEN NUMER AS A FIRST NUMBER AND TOTAL AS A SECOND NUMBER.)")
while True:
	opt =input("\n Please enter your operator or Enter 'Q' to quit :").capitalize()
	num1=input("\n Please enter your first number:")
	num2=input("\n Please enter your second number:")
	if opt== "O" :
		print(" Type + or - sign before numbers for you desire operation")
		print("\n Total of these two numbers is:",int(num1)+int(num2))		 
	elif opt=="M" :
		print("\n Multiplication of these two numbers is:",int(num1)*int(num2))
	elif opt=="D" :
		print("\n Division of these two numbers is:",int(num1)/int(num2))
	elif opt=="P" :
		print("\n Power of the first number is:",int(num1)**int(num2))
	elif opt=="Sr":
		print("\n Squre root of the first number is:",int(num1)**(0.5))
	elif opt=="Cr":
		print("\n Approximate Cube root of the first number is:",int(num1)**(0.333334))
	elif opt=="Md":
		print("\n Module of these two numbers is : ",int(num1)%int(num2))
	elif opt=="Pr":
		print("\n Percentage of the first number is:",(int(num1)/int(num2))*int(100))
	elif opt =="Q": 
		print("\n THANK YOU FOR USING OUR CALCULATOR \n") 
		break
	else : print("\nError , Please check you operator again.")