area =0
height =10
width =20
pi=3.1415
radius =2.55
# area of triangle
area =width*height/2
#printing formats
print("the area of the triangel is = ",area)
print("the area of the triangel is = %f" % area)
print("the area of the triangel is = {:2f}".format(area))
print("the area of the triangel is = %.2f" % area)

#area of circle
area_circle=pi*radius**2
print("Arear of circle =",area_circle)
print("Arear of circle = %.4f" % area_circle)
print("Arear of circle = {0:.4f}, {1:.4f}".format(area,area_circle))