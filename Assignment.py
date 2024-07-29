

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the widh of the rectangle: "))
    area = length * width
    print(f"The area of the recatngle is: {area:.2f}")

def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")

def main():
    print("Choose a shape to calculate the area: ")
    print("1. Circle") 
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        area_circle()
    elif choice == '2':
        rectangle_area()
    elif choice == '3':
        triangle_area()
    else:
        print("Invalid choice.")

    if __name__ == "__main__":
        main()
        