import numpy as np
import matplotlib.pyplot as plt

graph = plt.figure(figsize=(15,7))
draw = graph.add_subplot(111)
draw.set_title("plotter")

allowed_words = ['x','+', '-', '*', '/', '^'] 
allowed_numbers = ['0','1','2','3','4','5','6','7','8','9']
def func(string): 
    for word in range(len(string)): 
        if string[word] not in allowed_words and string[word] not in allowed_numbers: 
            raise ValueError('Invalid operator' , string[word]) # raise error if operator is not allowed
        else:
            continue   
    string = string.replace('^','**') # replace ^ with **
    def string_to_value(x):
        return eval(string)
    return string_to_value

xmin = int(input("xmin = ")) # input xmin
xmax = int(input("xmax = ")) # input xmax
if(xmin > xmax): 
    raise ValueError('xmin must be less than xmax') # raise error if xmin is greater than xmax

function = input("function = ") # input function
x = np.arange(xmin,xmax+0.1,0.1) # create array of x values
draw.plot(x,func(function)(x)) # plot function
plt.show() # show graph
       

       

