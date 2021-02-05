import webbrowser
import mysql.connector
#def Aadhar_child():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="98499849",database="AIJAZ1")
mydb2=mysql.connector.connect(host="localhost",user="root",passwd="98499849",database="AIJAZ1")
mycursor=mydb.cursor()
mycursor2=mydb2.cursor()
point=0
h=0
#FUNCTION FOR LOGIN 
def LOGIN():
	log_option=int(input(" 1.Login \n 2.Sign Up"))
	if(log_option==1):
		id=input("Enter your user id")
		if("@gmail.com" not in id):
			print("Invalid id ")
			exit(0)
	elif(log_option==2):		
		web="https://www.gmail.com"
		webbrowser.open_new(web)
	else:
		print("Invalid enter")
		exit(0)						
def AADHAR_VALIDATION(A_no):
	mycursor2.execute("SELECT * FROM Aadhar_child WHERE Aa_no = %s",(A_no,))
	myre2=mycursor2.fetchall()
	if(not myre2):
		print("Invalid Aadhar number!. Enter a valid Aadhar number")
		exit(0)
	Aa_digit=len(str(A_no))
	if(Aa_digit != 12):
		print("Digits of Aadhar number not match!. Entger a valid Aadhar number") 
		exit(0)
#FUNCTION FOR POPULATION
def POPULATION():
	#if(option==1):0
	A_no=int(input("Enter your Aadhar number:"))
	AADHAR_VALIDATION(A_no)
	mycursor.execute("SELECT * FROM  Aadhar_child WHERE Aa_no = %s",(A_no,))
	myre=mycursor.fetchall()
	#print(myre)
    #print(myre)
	if(not myre):
		print("Enter a valid number No match found!")
		exit(0)
	else:

		c_no=int(myre[0][1]) 
		#print(c_no)
		if(c_no>2):
			print("Not eligible")
			print(f"The limit is 2 children.But you have {myre[0][1]} children")
			exit(0)
		else:
			print("You are Eligible. Check for eligibity for pollution")
			#point+=1
			mycursor.execute("SELECT * FROM POP WHERE Aa_no = %s",(A_no,))
			myre=mycursor.fetchall()
			#print(myre)
			if(not myre):
				#SQL1="SELECT COUNT(Aa_no) FROM POPULATION GROUP BY Aa_no HAVING COUNT(Aa_no)"
				sql="INSERT INTO POP(Aa_no) VALUES (%s)"
				mycursor.execute(sql,(A_no,))
				mydb.commit() 	
def POLLUTION():
    #elif(option==2):
	print(" 1.Water Response \n 2.Electricity Response \n 3.Traffic Response")
	option1=int(input())
#if(option1==1):
def WATER(h):
	if(h==1):
		h=0
		A_no=int(input("Enter Owner's Aadhar number:"))
	else:
	    A_no=int(input("Enter your Aadhar number:"))
	AADHAR_VALIDATION(A_no)
	mycursor.execute("SELECT * FROM  POP WHERE Aa_no = %s",(A_no,))
	myre=mycursor.fetchall()
	if(not myre):
		print("First you need to check in population response")
		return
	  	#exit(0)
	else:
		can_no=(input("Enter CAN number:"))
		mycursor.execute("SELECT * FROM  Aadhar_can WHERE Aa_no = %s",(A_no,))
		myre=mycursor.fetchall()
		#print(myre)
		ca_no=(myre[0][1])
		print(ca_no)
		p_n=(myre[0][2])
		if(can_no!=ca_no):
			print("NOT Matched! Enter a valid Can number")
			return
		if(p_n=="not"):
			print("Not eligible")
			print("Your's bill payment is still pending!")
			return 
			#exit(0)	  
		else:
			print("You are Eligible. Check for eligibity for Electricity response")
			#point+=1 
			mycursor2.execute("SELECT * FROM pop_water WHERE Aa_no = %s",(A_no,))
			myre2=mycursor2.fetchall()
			if(not myre2):
				sql="INSERT INTO pop_water(Aa_no) VALUES (%s)"
				mycursor.execute(sql,(A_no,))
				mydb.commit() 	
			else:
				pass
			#mycursor.close()
			#mycursor=mydb.cursor(buffered=True)
#elif(option1==2):
def ELETRICITY(h):
	if(h==1):
		h=0
		A_no=int(input("Enter Owner's Aadhar number:"))
	else:
	    A_no=int(input("Enter your Aadhar number:"))
	AADHAR_VALIDATION(A_no)
	mycursor.execute("SELECT * FROM  POP_WATER WHERE Aa_no = %s",(A_no,))
	myre=mycursor.fetchall()
	if(not myre):
		print("First You need to Check eligibilty for population response AND WATER!")
		return
		#exit(0)
	else:
		usc_no=(input("Enter  USC number:"))
		mycursor.execute("SELECT * FROM  Aadhar_usc WHERE Aa_no=%s",(A_no,))
		my=mycursor.fetchall()
		#print(my)
		u_no=(my[0][1])
		p_n=(my[0][2])
		if(usc_no!=u_no):
			print("NOT Matched! Enter a valid Usc number")
			exit(0)  
		if(u_no=="not"):
				print("Not eligible")
				print("Your's bill payment is still pending!")
				return
				#exit(0)
		else:
			#pass 
			print("You are Eligible. Check for eligibity for Traffic response")
			#point+=1
			mycursor2.execute("SELECT * FROM pop_water_el WHERE Aa_no = %s",(A_no,))
			myre2=mycursor2.fetchall()
			if(not myre2):
				sql="INSERT INTO pop_water_el(Aa_no) VALUES (%s)"
				mycursor.execute(sql,(A_no,))
				mydb.commit()

			else:
				pass 
			#mycursor.close()
	#elif(option1==3):
def TRAFFIC():
	A_no=int(input("Enter your Aadhar number:"))
	AADHAR_VALIDATION(A_no)	
	mycursor.execute("SELECT * FROM pop_water_el WHERE Aa_no = %s",(A_no,))
	myre=mycursor.fetchall()
	if(not myre or myre):
		print("First You need to Check eligibilty for population response ,WATER,Electric!")
		return
		#exit(0)
	else:
		vehi_no=(input("Enter your Vehicle number:"))
		mycursor.execute("SELECT * FROM Aadhar_traf WHERE Aa_no=%s",(A_no,))
		myre=mycursor.fetchall()
		#print(myre)
		v_no=(myre[0][1])
		p_n=(myre[0][2])
		if(vehi_no!=v_no):
			print("NOT Matched! Enter a valid Vehicle number")
			exit(0)  
		if(v_no=="not"):
			print("Not eligible")
			print("Your's challens are still pending!")
			return
			#exit(0)
		else:	
			#pass 
			print("You are Eligible. Go for Aadhar card validation")
			#point+=1
			mycursor2.execute("SELECT * FROM pop_water_el_vehi WHERE Aa_no = %s",(A_no,))
			myre2=mycursor2.fetchall()
			if(not myre2):
				sql="INSERT INTO pop_water_el_vehi(Aa_no) VALUES (%s)"
				mycursor.execute(sql,(A_no,))
				mydb.commit() 	
			else:
				pass
			#mycursor.close()		
	#elif(option==3):
#def RENT_HOME():
#	print("You need to Enter yours owenr's aadhar no")
#	own_no=int(input("Enter owner's Aadhar number"))
def E_CARD():
	A_no=int(input("Enter your Aadhar number:"))
	AADHAR_VALIDATION(A_no)
	mycursor.execute("SELECT * FROM pop_water_el_vehi WHERE Aa_no = %s",(A_no,))
	myre=mycursor.fetchall()
	print(myre)
	if(not myre):
		print("First You need to Check eligibilty for population and pollution response")
		print("Enter your option.... \n 1.procced \n 2.exit")
		option2=int(input())
		if(option2==2):
			exit(0)
		elif(option2==1):
			while(True):
				print(" 1.Population Response \n 2.Polution Response \n 3.exit")
				option21=int(input("Enter Your Option::"))
				if(option21==1):
					POPULATION()
				elif(option21==2):
					#POLLUTION()
					while(True):
						print(" 1.Water Response \n 2.Electricity Response \n 3.Traffic Response \n 4.exit")
						option22=int(input())
						if(option22==1):
							WATER(h)
						elif(option22==2):
							ELETRICITY(h)
						elif(option22==3):
							TRAFFIC()
						elif(option22==4):
							return	
						else:
							print("Invalid Enter")	

				elif(option21==3):
					return		
				else:
					print("Invalid enter")	
	else:
		print("You are eligible for E-card certification! \n")
		print("Now you are a Environment Card") 
		exit(0)
def Questionaire():						
	#if(option==4):
	print(" 1.Why E card? \n 2.Eligibility\n 3.Benifits of E card\n 4.Other conditions\n 5.Exit")
	option41=int(input())
	if(option41==1):
		print("E card is to avail the givernment benefits")
	elif(option41==2):
		print("One should pay electricity,water bill and should be with no pending challens on vehicle")
	elif(option41==3):
		print("One can get Govt jobs,Scholarship,discount in Govt hospitals etc.. ")
	elif(option41==4):
		print("There will be only one E card per familiy")
	elif(option41==5):
		exit(0)
	else:
		print("invalid enter")
#LOGIN()		
#functions implementations								
while(True):
	print(" 1.Population Response \n 2.Polution Response \n 3.Green Card Validation \n 4.Questionaire \n 5.Exit ")
	option=int(input("Enter Your Option::"))
	if(option==1):
		POPULATION()
	elif(option==2):
		#POLLUTION()
		while(True):
			print(" 1.Water Response \n 2.Electricity Response \n 3.Traffic Response \n 4.Exit")
			option1=int(input())
			if(option1==1):
				print("Do you leave in rent house?? ")
				option_rent=int(input(" 1.YES \n 2.NO \n"))
				if(option_rent==2):	
					WATER(h)
				elif(option_rent==1):
					print("You need to Enter yours owenr's aadhar no")
					h=1
					WATER(h)
				else:
					print("INVALID ENTER")	
			elif(option1==2):
				print("Do you leave in rent house?? ")
				option_rent=int(input("1.YES \n 2.NO \n"))
				if(option_rent==2):	
					ELETRICITY(h)		
				elif(option_rent==1):
					print("You need to Enter yours owenr's aadhar no")
					h=1
					ELETRICITY(h)
			elif(option1==3):
				TRAFFIC()
			elif(option1==4):
			    break	
			else:
				print("Invalid Enter")			
	elif(option==3):
		E_CARD()
	elif(option==4):
		Questionaire()
	elif(option==5):
		exit(0)
	else:
		print("Invalid enter")