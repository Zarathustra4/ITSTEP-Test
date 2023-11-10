print("Denys, pay attention!!!") # Денис, приділи цьому увагу!!!
print("Цей рядок для того, щоб пояснити git push")

def input_cred():
    login = input(">>>") 
    password = input(">>>")
    
    if login != "login" or password != "password":
        print("Wrong login or password")