#include <iostream>
#include <cmath>

using namespace std;

// Function prototypes
double calculateCircleArea(double radius);
double calculateTriangleArea(double base, double height);
double calculateRectangleArea(double length, double width);

int main() {
    char choice;
    cout << "Choose the shape to calculate the area:" << endl;
    cout << "1. Circle" << endl;
    cout << "2. Triangle" << endl;
    cout << "3. Rectangle" << endl;
    cout << "Enter your choice (1/2/3): ";
    cin >> choice;

    switch(choice) {
        case '1': {
            double radius;
            cout << "Enter the radius of the circle: ";
            cin >> radius;
            cout << "The area of the circle is: " << calculateCircleArea(radius) << endl;
            break;
        }
        case '2': {
            double base, height;
            cout << "Enter the base of the triangle: ";
            cin >> base;
            cout << "Enter the height of the triangle: ";
            cin >> height;
            cout << "The area of the triangle is: " << calculateTriangleArea(base, height) << endl;
            break;
        }
        case '3': {
            double length, width;
            cout << "Enter the length of the rectangle: ";
            cin >> length;
            cout << "Enter the width of the rectangle: ";
            cin >> width;
            cout << "The area of the rectangle is: " << calculateRectangleArea(length, width) << endl;
            break;
        }
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}