import random 
import string 
# the length of password 
length= 16
lower = string.ascii_lowercase
upper =string.ascii_uppercase
num=string.digits
symbols=string.punctuation
#combine the data
all_=lower+upper+num+symbols
#create the password 
password="".join(random.sample(all_,length))
print(password)