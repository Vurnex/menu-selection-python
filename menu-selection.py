import os
import os.path

def main():
 MainMenu()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def MainMenu(): #main menu
  
 cls()
 
 print("\nIn Main Menu\n")

 userChoice = 0 #create variable to hold our user's choice
 
 while int(userChoice) !=5: #loops through while not equal to 5
   
   #print our options
   print("\n1- Appointments")
   print("2- Patients")
   print("3- Staff")
   print("4- Exit\n")

   #prompt our input and get choice from the user
   userChoice = input("Please enter your menu choice: ")
   
   while int(userChoice) < 1 or int(userChoice) > 4: #ensure a response of 1-3
     print("Valid choices are 1-4\n")
     userChoice = input("Please enter your menu choice") #reenter their choice

   if int(userChoice) == 1:
     AppointmentsMenu()
   elif int(userChoice) == 2:
     PatientsMenu()
   elif int(userChoice) == 3:
     StaffMenu()
   elif int(userChoice) == 4:
    print("\nLogging off...have a nice day.")
    quit()

def AppointmentsMenu():

 cls()
 
 print("\nIn Appointments Menu\n")
 
 subMenuChoice = 0
 
 addAppmnt = 0

 print("1- Add Appointment")
 print("2- Change Appointment")
 print("3- Delete Appointment")
 print("4- Return to Main Menu\n")
 
 subMenuChoice = input("Please enter your selection: ")
 
 if int(subMenuChoice) == 1:
   
   addAppmnt = input("Please enter Appointment Information: ")
   
   myFile = open("appointment_info.txt", "w")
   myFile.write(addAppmnt +"\n")
   print("\nAppointment successfully created.")
   input("\nPress Enter to continue...")
   myFile.close()
   MainMenu()
 
 elif int(subMenuChoice) == 2:
   addAppmnt = input("Please enter changes to the appointment: ")
   myFile = open("appointment_info.txt", "w")
   myFile.write(addAppmnt +"\n")
   print("\nAppointment successfully updated.")
   input("\nPress Enter to continue...")
   myFile.close()
   MainMenu()
 
 elif int(subMenuChoice) == 3:
  if not os.path.exists('appointment_info.txt'):
    print("\nThere are currently no appointments registered.")
    input("\nPress Enter to continue...")
    MainMenu()

  os.remove("appointment_info.txt")
  print("\nAppointment successfully deleted.")
  input("\nPress Enter to continue...")
  MainMenu()

 elif int(subMenuChoice) == 4:
  MainMenu()
   
 
def PatientsMenu():

 cls()
 
 print("\nIn Patients Menu\n")
 
 subMenuChoice = 0
 
 addPatient = 0

 print("1- Add Patient Information")
 print("2- Update Patient Information")
 print("3- Delete Patient Information")
 print("4- Return to Main Menu\n")
 
 subMenuChoice = input("Please enter your selection: ")
 
 if int(subMenuChoice) == 1:
  addPatient = input("Please enter Patient Information: ")
  myFile = open("patient_info.txt", "w")
  myFile.write(addPatient +"\n")
  print("\nPatient info successfully added.")
  input("\nPress Enter to continue...")
  myFile.close()
  MainMenu()
 
 elif int(subMenuChoice) == 2:
   addPatient = input("Please enter changes to the Patient Information: ")
   myFile = open("patient_info.txt", "w")
   myFile.write(addPatient +"\n")
   print("\nPatient info successfully updated.")
   input("\nPress Enter to continue...")
   myFile.close()
   MainMenu()
 
 elif int(subMenuChoice) == 3:

  if not os.path.exists('patient_info.txt'):
    print("\nThere are currently no patients registered.")
    input("\nPress Enter to continue...")
    MainMenu()

  os.remove("patient_info.txt")
  print("\nPatient(s) successfully deleted.")
  input("\nPress Enter to continue...")
  MainMenu()
  
 elif int(subMenuChoice) == 4:
  MainMenu()
 
def StaffMenu():
  
  cls()
  
  print("\nIn Staff Menu\n")
  
  subMenuChoice = 0
  
  addStaff = 0

  print("1- Add Staff Information")
  print("2- Update Staff Information")
  print("3- Delete Staff Information")
  print("4- Return to Main Menu\n")
  
  subMenuChoice = input("Please enter your selection: ")
  
  if int(subMenuChoice) == 1:
    addStaff = input("Please enter Staff Information: ")
    myFile = open("staff_info.txt", "w")
    myFile.write(addStaff +"\n")
    print("\nStaff info successfully registered.")
    input("\nPress Enter to continue...")
    myFile.close()
    MainMenu()
  
  elif int(subMenuChoice) == 2:
   addStaff = input("Please enter changes to the Staff Information: ")
   myFile = open("staff_info.txt", "w")
   myFile.write(addStaff +"\n")
   print("\nStaff info successfully updated.")
   input("\nPress Enter to continue...")
   myFile.close()
   MainMenu()
  
  elif int(subMenuChoice) == 3:
   if not os.path.exists('staff_info.txt'):
    print("\nThere is currently no staff info registered.")
    input("\nPress Enter to continue...")
    MainMenu()

   os.remove("staff_info.txt")
   print("\nStaff info successfully deleted.")
   input("\nPress Enter to continue...")
   MainMenu()

  elif int(subMenuChoice) == 4:
    MainMenu()

main()