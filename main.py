print("Denys, pay attention!!!") # Денис, приділи цьому увагу!!!
print("Цей рядок для того, щоб пояснити git push")

LOGIN = "LOGIN"
PASSWORD = "PASS"

def input_cred():
    login = input(">>>") 
    password = input(">>>")
    
    if login != LOGIN or password != PASSWORD:
        print("Wrong login or password")
    elif login == LOGIN and password == PASSWORD:
        print("Success")

input_cred()