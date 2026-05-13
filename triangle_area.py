import math

def triangle_area(base, height):
    area = 0.5 * base * height
    return area

def Heron_area(a, b, c):
    s  =  (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def coordinate_geometry(x1, y1, x2, y2, x3, y3):
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5
    return area

print("Choose a method to calculate triangle area: ")
print("1. Base and Height")
print("2. Heron's Formula")
print("3. Coordinate Geometry")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Triangle Area: ", triangle_area(base, height))

elif choice == 2:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    print("Heron-Area: ", Heron_area(a, b, c))

elif choice == 3:
    x1 = float(input("Enter the value of x1: "))
    y1 = float(input("Enter the value of y1: "))
    x2 = float(input("Enter the value of x2: "))
    y2 = float(input("Enter the value of y2: "))
    x3 = float(input("Enter the value of x3: "))
    y3 = float(input("Enter the value of y3: "))
    print("Coordinate Geometry: ", coordinate_geometry(x1, y1, x2, y2, x3, y3))

else:
    print("Invalid choice. Please run the program again.")

