def main():
 MainMenu()

def MainMenu(): #main menu
 print("In Main Menu\n")

 userChoice = 0 #create variable to hold our user's choice
 
 while int(userChoice) !=5: #loops through while not equal to 5
   #print our options
   print("\n1- Appointments")
   print("2- Patients")
   print("3- Staff")
   print("4- Exit\n")
   #prompt our input and get choice from the user
   userChoice = input("Please enter your menu choice")
   while int(userChoice) < 1 or int(userChoice) > 4: #ensure a response of 1-3
     print("Valid choices are 1-3\n")
     userChoice = input("Please enter your menu choice") #reenter their choice
   if int(userChoice) == 1:
     AppointmentsMenu()
   elif int(userChoice) == 2:
     PatientsMenu()
   elif int(userChoice) == 3:
     StaffMenu()
   elif int(userChoice) == 4:
     break

def AppointmentsMenu():
 print("\nIn Appointments Menu\n")
 subMenuChoice = 0
 addAppmnt = 0

 print("1- Add Appointment")
 print("2- Change Appointment")
 print("3- Delete Appointment\n")
 subMenuChoice = input("Please enter your selection")
 if int(subMenuChoice) == 1:
   addAppmnt = input("Please enter Appointment Information")
   myFile = open("appointment_info.dat", "w")
   myFile.write(addAppmnt +"\n")
   myFile.close()
 elif int(subMenuChoice) == 2:
   addAppmnt = input("Please enter changes to the appointment")
   myFile = open("appointment_info.dat", "w")
   myFile.write(addAppmnt +"\n")
   myFile.close()
 elif int(subMenuChoice) == 3:
   import os
   os.remove("appointment_info.dat")
   
 
def PatientsMenu():
 print("\nIn Patients Menu\n")
 subMenuChoice = 0
 addPatient = 0

 print("1- Add Patient Information")
 print("2- Update Patient Information")
 print("3- Delete Patient Information\n")
 subMenuChoice = input("Please enter your selection")
 if int(subMenuChoice) == 1:
  addPatient = input("Please enter Patient Information")
  myFile = open("patient_info.dat", "w")
  myFile.write(addPatient +"\n")
  myFile.close()
 elif int(subMenuChoice) == 2:
   addPatient = input("Please enter changes to the Patient Information")
   myFile = open("patient_info.dat", "w")
   myFile.write(addPatient +"\n")
   myFile.close()
 elif int(subMenuChoice) == 3:
   import os
   os.remove("patient_info.dat")
 
def StaffMenu():
  print("\nIn Staff Menu\n")
  subMenuChoice = 0
  addStaff = 0

  print("1- Add Staff Information")
  print("2- Update Staff Information")
  print("3- Delete Staff Information\n")
  subMenuChoice = input("Please enter your selection")
  if int(subMenuChoice) == 1:
    addStaff = input("Please enter Staff Information")
    myFile = open("staff_info.dat", "w")
    myFile.write(addStaff +"\n")
    myFile.close()
  elif int(subMenuChoice) == 2:
   addStaff = input("Please enter changes to the Staff Information")
   myFile = open("staff_info.dat", "w")
   myFile.write(addStaff +"\n")
   myFile.close()
  elif int(subMenuChoice) == 3:
   import os
   os.remove("staff_info.dat")

main()