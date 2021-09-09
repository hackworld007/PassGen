# If you copy this ....... please give  credit to Hack workd channel
import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+gren+"""
 _   _            _     __        __         _     _
| | | | __ _  ___| | __ \ \      / /__  _ __| | __| |
| |_| |/ _` |/ __| |/ /  \ \ /\ / / _ \| '__| |/ _` |
|  _  | (_| | (__|   <    \ V  V / (_) | |  | | (_| |
|_| |_|\__,_|\___|_|\_\    \_/\_/ \___/|_|  |_|\__,_| v 2.0
"""+gren+red)

print (gren+b+"                   ____ __ __ ____ __ __ __ ____"+b+gren)
print (gren+b+"                  |     Coded By Steven Liam    |"+b+gren)
print (gren+b+"                  |    Youtube :- Hack World    |"+b+gren)
print (gren+b+"                  |___ __ __ __ __  __ __ __ ___|"+b+gren)


length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (gren+b+" "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
