def greet (): 
    Firstname = input ("Enter your First name: ")   
    Lastname = input ("Enter your Last name: ")
    print (f"Welcome {Firstname} {Lastname} ") 
greet ()

def get_greeting(name):
    return f"Hello, {name}!"

message = get_greeting("Alice")
file = open("greeting.txt", "w")
file.write(message)