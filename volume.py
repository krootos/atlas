import math

def cube(side: float)->float:
    '''
    side: float
    return: cube volume
    '''
    return side ** 3

def cylinder(r: float, h: float)->float:
    '''
    r: radius
    h: height
    '''
    return math.pi*r*r*h


if __name__ == "__main__":
    print(f'cube(2) = {cube(2)}')
    print(f'cylinder(1, 10)={cylinder(1, 10)}')