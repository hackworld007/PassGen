# demo.py
import random 
length=int(input("Choose Your Password Length:"))

print("")

print("Password Generated ")

print("")

char="abcdefghijklmnopqrstuvwxyz1234567890£$%^&*"
password=("")

for i in range(length):
  password+=random.choice(char)
  
print(password)

print("Subscribe my channel For more")
