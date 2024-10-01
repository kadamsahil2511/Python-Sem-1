#Find the Perimeter, Area and Volume of 2D and 3D shapes
import math

def calculate_2d_shape(shape):
    if shape == "circle":
        radius = float(input("Enter the radius: "))
        perimeter = 2 * math.pi * radius
        area = math.pi * radius ** 2
        return perimeter, area, None
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        perimeter = 2 * (length + width)
        area = length * width
        return perimeter, area, None
    elif shape == "triangle":
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return perimeter, area, None
    elif shape == "square":
        a = float(input('Enter the side of the square'))
        area = a**2
        perimeter = 6*a
        return perimeter, area, None
    elif shape == "parallelogram":
        a=input('Enter the side 1 of the parallelogram')
        b=input('Enter the side 2 of the parallelogram')
        base = input('Enter the base of the parallelogram')
        height = input('Enter the height of the parallogram')
        if a != "" :
            x=float(a)
            y=float(b)
            perimeter = 2*(x+y)
            return perimeter
        elif base != "" : 
            x=float(a)
            y=float(b)
            area = x*y
            return area
        else :
            pass 
    elif shape == "rhombus":
        a=input('Enter the side 1 of the rhombus')
        D1 = input('Enter the diagonal of the rhombus')
        D2 = input('Enter the diagonal 2 of the rhombus')
        if a != "" :
            x=float(a)
            perimeter = 6*a
            return perimeter
        elif base != "" : 
            x=float(D1)
            y=float(D2)
            area = (x*y)/2
            return area
        else :
            pass 
    else:
        return None, None, None

def calculate_3d_shape(shape):
    if shape == "sphere":
        radius = float(input("Enter the radius: "))
        surface_area = 4 * math.pi * radius ** 2
        volume = (4/3) * math.pi * radius ** 3
        return None, surface_area, volume
    elif shape == "cuboid":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        surface_area = 2 * (length * width + width * height + height * length)
        volume = length * width * height
        return None, surface_area, volume
    elif shape == "cylinder":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        surface_area = 2 * math.pi * radius * (radius + height)
        volume = math.pi * radius ** 2 * height
        return None, surface_area, volume
    elif shape == "cube" :
        side = float(input("Enter the side length: "))
        surface_area = 6 * side ** 2
        volume = side ** 3
        return None, surface_area, volume
    elif shape == "cone":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        slant_height = math.sqrt(radius ** 2 + height ** 2)
        surface_area = math.pi * radius * (radius + slant_height)
        volume = (1/3) * math.pi * radius ** 2 * height
        return None, surface_area, volume
    elif shape == "hemisphere":
        radius = float(input("Enter the radius: "))
        surface_area = 3 * math.pi * radius ** 2
        volume = (2/3) * math.pi * radius ** 3
        return None, surface_area, volume
    else:
        return None, None, None

def main():
    shape_type = input("Enter the type of shape (2D or 3D): ").lower()
    shape = input("Enter the shape (e.g., circle, rectangle, triangle for 2D; sphere, cuboid, cylinder for 3D): ").lower()

    if shape_type == "2d":
        perimeter, area, _ = calculate_2d_shape(shape)
        if perimeter is not None:
            print(f"Perimeter: {perimeter}")
            print(f"Area: {area}")
        else:
            print("Invalid 2D shape.")
    elif shape_type == "3d":
        _, surface_area, volume = calculate_3d_shape(shape)
        if surface_area is not None:
            print(f"Surface Area: {surface_area}")
            print(f"Volume: {volume}")
        else:
            print("Invalid 3D shape.")
    else:
        print("Invalid shape type.")

main()
