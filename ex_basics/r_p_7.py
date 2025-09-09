# password generator
# Ask the user to create a password and check that it contains at least:
# o	8 characters
# o	one uppercase letter
# o	one digit






def checkpassword(password_input):
  #stock the lenght of the password 
  password_len = len(password_input)
  #chzck the validity of the password
  if password_len >= 8 and any(char.isdigit() for char in password_input) and any(char.isupper() for char in password_input):
    print("mot de passe solide")
  else:
    print("wrong password")
    #call itselt untill the password is good
    newpassword = input("try another password")
    checkpassword(newpassword)



password_input =  input(" enter your password ")
checkpassword(password_input)






    



    
   

