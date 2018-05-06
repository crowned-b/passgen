import random

def testStrength(newPassword, vectors, passwordLen):
    for vector in vectors:
        if not set(newPassword).intersection(set(vector)):
            filler=random.randrange(passwordLen-1)
            newPassword=newPassword[:filler] + vector[random.randrange(len(vector))] + newPassword[filler+1:]
            return [newPassword,-1,vector]
    return [newPassword,1,vector]

def passwordGen(passwordLen):
    alphaLow = "abcdefghijklmnopqrstuvwxyz"
    alphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    special = ":;>.<,?/|\_-+=!@#$%^&*()\"\\"
    allChars=alphaLow+alphaUp+num+special
    vectors=[alphaLow,alphaUp,num,special]
    newPassword=""

    for i in range(passwordLen):
        newChar = random.choice(allChars)
        newPassword+=newChar
    while testStrength(newPassword, vectors, passwordLen)[1] == -1:
        newPassword=testStrength(newPassword,vectors,passwordLen)[0]
    return newPassword
try:
    passwordLen = int(raw_input("Please enter password length: "))
    if passwordLen >= 8:
        print("Your new password: %s" % passwordGen(passwordLen))
    else:
        print("Password too short. Using default of 8.")
        print("Your new password: %s" % passwordGen(8))
except ValueError:
    print("Invalid length. Using default length of 8.\n")
    print("Your new password: %s" % passwordGen(8))
