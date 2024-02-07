from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.threed.cuboid import volume as cuboid_volume, surface_area as cuboid_surface_area
from graphics.threed.sphere import volume as sphere_volume, surface_area as sphere_surface_area

# Rectangle
length_rect, width_rect = 4, 6
print(f"Rectangle Area: {rect_area(length_rect, width_rect)}")
print(f"Rectangle Perimeter: {rect_perimeter(length_rect, width_rect)}\n")

# Circle
radius_circle = 5
print(f"Circle Area: {circle_area(radius_circle)}")
print(f"Circle Perimeter: {circle_perimeter(radius_circle)}\n")

# Cuboid
length_cuboid, width_cuboid, height_cuboid = 3, 4, 5
print(f"Cuboid Volume: {cuboid_volume(length_cuboid, width_cuboid, height_cuboid)}")
print(f"Cuboid Surface Area: {cuboid_surface_area(length_cuboid, width_cuboid, height_cuboid)}\n")

# Sphere
radius_sphere = 2
print(f"Sphere Volume: {sphere_volume(radius_sphere)}")
print(f"Sphere Surface Area: {sphere_surface_area(radius_sphere)}")
