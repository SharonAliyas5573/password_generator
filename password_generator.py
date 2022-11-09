
import random
import string

characters = list(string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
def passwords():
    
   pass_len = int(input("Enter the length of the password :"))
   random.shuffle(characters)

   password=[]
   for i in range (pass_len):
        password.append(random.choice(characters))

   random.shuffle(password)

   password = "".join(password)
   print("Your strong password is  :" + password)


opt = input("DO you want to Generate password [Yes/no] :")

if opt=='Yes' or opt=='yes':
    
  passwords()
          
elif opt=='No' or 'no':
    print("OK,Have a good day :)")
    quit()
else:
    print("Invalid input :(")

    quit()


          



