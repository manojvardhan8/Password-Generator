# It is done by S.Manoj Vardhan B-TECH(CSE)
#----------------PASSWORD GENERATOR---------------------------------
#generating password having atleast one lower case and uppercase aplhabet and having atleast one number and specialcharacter.

import random
#random module is used in randomselection on anything.
def generatePassword(pwlength):#pwlength is a list containing the individual length of passwords given by user

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] #It is used to store the passwords

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randint(1,1000)%26 #selecting index between 0 and 26 randomly.
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        password = replaceWithSpecialCharacter(password)
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    n=random.randrange(1,len(pword))
    f=-1
    i=0
    while i<n:
        replace_index = random.randrange(len(pword))
        if pword[replace_index].islower():
            if f==-1:
                f=replace_index #storing the index of lower aplhabet so that the password contain atleast one lower case
            elif f==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:] # replacing the character with the number
                  #random.randange(10)---->selecting the digit from 0to 9
                i+=1
        else:
            i+=1
    return pword


def replaceWithUppercaseLetter(pword):
    f=-1
    g=-1
    n=random.randrange(1,len(pword))
    i=0
    while i<n:
        replace_index = random.randrange(len(pword))
        if pword[replace_index].islower():
            if f==-1:
                f=replace_index     #storing the index of lower aplhabet so that the password contain atleast one lower case
            elif f==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
                i+=1
        elif pword[replace_index].isdigit():
            if g==-1:
                g=replace_index     #storing the index of digit  so that the password contain atleast one digit
            elif g==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:] #replacing the lower case with the Upper case letter
                i+=1
        else:
            i+=1
    return pword
def replaceWithSpecialCharacter(pword):
    specialchar="@#$_"
    f=-1
    g=-1
    h=-1
    n=random.randrange(1,len(pword))
    i=0
    while i<n:
        replace_index = random.randrange(len(pword))
        if pword[replace_index].islower():
            if f==-1:
                f=replace_index   #storing the index of lower aplhabet so that the password contain atleast one lower case
            elif f==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + specialchar[random.randint(1,1000)%4] + pword[replace_index+1:] #replacing the character with the special character.
                i+=1
        elif pword[replace_index].isdigit():
            if g==-1:
                g=replace_index   #storing the index of digit so that the password contain atleast one digit.
            elif g==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + specialchar[random.randint(1,1000)%4] + pword[replace_index+1:]
                i+=1
        elif pword[replace_index].isupper():
            if h==-1:
                h=replace_index    #storing the index of upper aplhabet so that the password contain atleast one upper case
            elif h==replace_index:
                continue
            else:
                pword = pword[0:replace_index] + specialchar[random.randint(1,1000)%4] + pword[replace_index+1:]
                i+=1
        else:
            i+=1 
    return pword


def main():
    
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 4")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<4:
            length = 4
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])



main()
