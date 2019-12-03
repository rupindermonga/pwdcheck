
#creating password list manually for now
#Try for 3 attempts

passwdList = [";lfhksnf", 'ruandhu',"ijamkfbihfe","abcdef","asdfg","qwerty"]
count = 3

valid = False
    
while count>0:  
    pwd = input("Enter Password: ")
    for eachPwd in passwdList:
        if pwd == eachPwd:
            valid = True
            print("Successful")
            break
    if not valid:
        print("Invalid input")
        count -= 1
        continue
    else:
        break