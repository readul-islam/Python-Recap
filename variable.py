# many value to multiple values

x, y , z = 1,2,3,

print(x)
print(y)
print(z)

# one value to multiple variables

x =y =z= "Orange"
print(x,y,z)

# Unpack a collection
# python allows us to extract tha list values to into variables this is called unpacking

fruits= ["Orange", "Mango", "Banana"]
x, y ,z = fruits

print(x,y,z)


# global variables

x = "awesome"

def myFirst():
    x = "amin"
    print("First", x)
    
    
myFirst()

print(x)