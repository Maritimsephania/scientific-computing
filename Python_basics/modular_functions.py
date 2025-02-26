import math
def calculate_area(shape, dimension1, dimension2=0):
    match shape:
     case "circle":
         return math.pi*dimension1**2
     case "rectangle":
         return dimension2*dimension1
     case "triangle":
         return 0.5*dimension1*dimension2

area_circle = calculate_area("circle",5)
area_rectangle = calculate_area("rectangle",10,6)
area_triangle = calculate_area("triangle", 10,6)

print("Area of circle: ", area_circle)
print("Area of rectangle: ", area_rectangle)
print("Area of triangle: ", area_triangle)