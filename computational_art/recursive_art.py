""" TODO: Put your header comment here """
import math
import random
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    return func_maker([],0,random.randint(min_depth,max_depth))  

def func_maker(func,depth,max_depth):
    '''Give this puppy a funciton, current depth, and a max depth and 
    it will pop out a function that has the given depth
    '''

    func_dict={1:'x',2:'y',3:'cos',4:'sin',5:'sqr',6:'neg',7:'prod',8:'ave',9:'dif'}
    depth+=1
    if depth<max_depth:
        f=random.randint(3,9)
        if 3<=f<=6:
            return [func_dict[f],func_maker(func,depth,max_depth)]
        elif 7<=f<=9:
            return [func_dict[f],func_maker(func,depth,max_depth),func_maker(func,depth,max_depth)]
    else:    
        return [func_dict[random.randint(1,2)]]

def evaluate(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate(["y"],0.1,0.02)
        0.02
        >>> evaluate(['sin',["x"],],.25,.25)
        0.7071063120935576
    """
    if f!=['x'] and f!=['y']:
        if f[0]=='prod':
            return evaluate(f[1],x,y)*evaluate(f[2],x,y)
        elif f[0]=='ave':
            return .5*(evaluate(f[1],x,y)+evaluate(f[2],x,y))
        elif f[0]=='sqr':
            return (evaluate(f[1],x,y)**2)
        elif f[0]=='cos':
            return math.cos(3.14159*evaluate(f[1],x,y))
        elif f[0]=='sin':
            return math.sin(3.14159*evaluate(f[1],x,y))
        elif f[0]=='neg':
            return -1*evaluate(f[1],x,y)
        elif f[0]=='dif':
            return abs(evaluate(f[1],x,y))-abs(evaluate(f[2],x,y))      
    elif f==['x']:
        return x
    elif f==['y']:
        return y
    else:
        print 'invalid string'

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].
        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval
        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # (input end-val)/input range=(output end-res)/output range
    input_range=input_interval_end-input_interval_start
    output_range=output_interval_end-output_interval_start
    return output_interval_end-(input_interval_end-float(val))/(input_range)*output_range
  
def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.
        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]
        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)

def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(6,7)
    green_function = build_random_function(6,7)
    blue_function = build_random_function(6,7)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate(red_function, x, y)),
                    color_map(evaluate(green_function, x, y)),
                    color_map(evaluate(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #creates pictures 1 through 10
    for i in range(1,10):
        filename=str(i)+'.png'
        generate_art(filename)

