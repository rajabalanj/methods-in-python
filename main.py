import math
import sys


class Circle:
    def __init__(self, radius_of_circle):
        self.radius = radius_of_circle

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius




def main():
    radius = float(input("Enter a radius: "))
    instance = Circle(radius)
    choice = input('select what you want to calculate(area,circumference,diameter): ')
    if choice == 'area':
        print(instance.area())
    elif choice == 'diameter':
        print(instance.diameter())
    elif choice == 'circumference':
        print(instance.circumference())
    else:
        print("check for typo")
    continue_or_stop = input("Do you want to continue('yes' or 'no')")
    if continue_or_stop == 'yes':
        main()
    else:
        sys.exit()


main()
