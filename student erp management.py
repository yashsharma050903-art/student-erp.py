username = "Yash"
password = "1234"
user = input("enter the username")
pwd = input("enter the password")
if user == username and pwd == password:
  print("Login Successful")
  while True:
    print("STUDENT DASHBOARD")
    print("1.Profile")
    print("2.Marks")
    print("3.Result")
    print("4.Attendance")
    print("5.Exit")
    choice = int(input("enter the choice"))
    if choice == 1:
      print("1.Profile")
      print("Name : Yash")
      print("Roll.no : 325")
      print("Course : Btech Cse")
      print("Batch : 2025-2029")
    elif choice == 2:
      print("2.Marks")
      print("Python : 72")
      print("Software engineering : 80")
      print("Java : 60")
      print("Physics :90")
    elif choice == 3:
      python = 72
      se = 80
      java = 60
      physics = 90
      Total = Python + Software engineering + Java + Physics
            72 + 80 + 60 + 90 = 302
      percentage =  Total / 4
                 =     302/4
                 =     75.5
      print("Result")
      print("Total:",total)
      print("Percentage:",percentage)
      if percentage >= 90:
          grade = "A+"
      elif percentage >= 80:
          grade = "A"
      elif percentage >= 70:
          grade = "B"
      else:
          grade = "C"
      print("Grade:",grade)
      if percentage >= 40:
        print("result : pass")
      else:
        print("result : fail")
    elif choice == 4:
       print("Attendance")
       print("total attendance : 82%")
       if 82 >= 75:
         print("eligible")
       else:
         print("short attendance")
    elif choice == 5:
        print("logout successful")
      
        break   
    else:
       print("Invalid Choice")
  else:
    print("Invalid Username or Password")
