import os,sys,time

x = "IzyanzZ"
y = "Tampan"

def login():
  b()
  user = input("Username 》 ")
  passw = input("Password 》 ")
  if user == x and passw == y:
    print("Login Succes!")
    time.sleep(2)
    sys.exit
def b():
  os.system("clear")
def menu():  
  print("\033[1;98######################################")
  print("\033[1,98#                                    #")
  print("\033[1,98######################################")
  print("")
  print("\033[1;97[1]\033[1;33 DarkFB")
  print("\033[1;97[2]\033[1;33 Keluar")
  
b()
login()
menu()
i = input("1/2: ")
if i == 1:
  print("Wait..")
if i == 2:
  print("Kluar!")
