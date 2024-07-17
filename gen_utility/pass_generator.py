import random as rd
print("Hi")
Lunghezza = int(input("how would you like your password to be? \n"))


Password = ""
Index = "QWERTYUIOPASDFGHJKLòàè+ZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!£$%&/()=?^é"

for i in range(Lunghezza):
  Password += rd.choice(Index) 

print(Password)
print("Program by Martin449")
input()