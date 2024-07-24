import string
import random
import sys

if __name__=="__main__":
    s1 = string.ascii_lowercase
    #print(s1)     #check lowercase letters
    s2 = string.ascii_uppercase
    #print(s2)     #check uppercase letters
    s3 = string.digits
    #print(s3)     #check for digits
    s4 = string.punctuation
    #print(s4)     #check for punctuations
    
    try:
        plen = int(input("enter password length :\n"))
    except:
        sys.exit("Invalid length")
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)

    print("Your password is : ")
    print("".join(random.sample(s,plen)))
    
    
    