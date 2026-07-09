def greet():
    print("Hello Asmita")

greet()
greet()
greet()

#Parameters
def greet(name):
    print("Hello", name)


   #Arguments
   #greet("Asmita")


#print()
#Only displays the value.

def add(a, b):
    print(a + b)


#return
#Returns the value so it can be stored or reused.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


#Calling Function Multiple Times
def greet(name):
    print("Hello", name)

greet("Asmita")
greet("Rahul")
greet("Priya")