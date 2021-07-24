import os,sys,time

def c():
  os.system("clear")

print("Install Depend? Y/n")
pil = input("Y/n")
if pil == "Y":
  os.system("pkg install neofetch")
  os.system("pkg install python2")
  os.system("pkg install net-tools")
  print(" Selesai! ")
  c()
  time.sleep(4)
  os.system("python2 index.py")
  time.sleep(5)
