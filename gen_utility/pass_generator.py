def Pgenerator:
  import random as rd
  print("Hi")
  Lunghezza = int(input("how would you like your password to be? \n"))

  #Here are the letters that the program uses to create the password
  Password = ""
  Index = "QWERTYUIOPASDFGHJKLòàè+ZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!£$%&/()=?^é"

  for i in range(Lunghezza):
    Password += rd.choice(Index)#Here the program creates the password with the letters from before

print(Password)
print("Program by Martin449 and foxeritocretito")
input()
