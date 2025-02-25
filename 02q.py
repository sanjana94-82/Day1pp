#swap two values
def swapping_values(x,y):
    x=x+y
    y=x-y
    x=x-y
    return x,y
a=10
b=5
print(swapping_values(a,b))