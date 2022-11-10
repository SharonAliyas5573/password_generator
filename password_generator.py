
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
   
   print("generatingg......")
   print("Your strong password is  :" + password)


opt = input("DO you want to Generate password [Yes/no] :")

if opt=='Yes' or opt=='yes':
    
  passwords()

  opt_1 = input("Generate Another [yes/No]")

  if opt_1 == 'yes' or opt_1 =='YES':

    
    passwords()
  elif opt=='No' or 'no':
    print("OK,Have a good day :)")
    quit()
  else:
    print("Invalid input :(")

    quit()            
elif opt=='No' or 'no':
    print("OK,Have a good day :)")
    quit()
else:
    print("Invalid input :(")

    quit()


          



