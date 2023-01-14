
import random
import string




def passwords(len):
     characters = list( string.ascii_uppercase + string.ascii_lowercase + string.digits)
     characters.append("@!_#%&")
     random.shuffle(characters)

     password=[]
     for i in range (len):
        password.append(random.choice(characters))

   

     password = "".join(password)
     return(password)


          



