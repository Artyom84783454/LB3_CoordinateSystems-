import math

pi = 3.14159265358979323846

def degrees_to_radians(degrees):
    return degrees * pi / 180.0

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def polar_distance(r1, theta1, r2, theta2):
    return math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * math.cos(degrees_to_radians(theta2 - theta1)))

def spherical_distance(r1, theta1, phi1, r2, theta2, phi2):
    return math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * (math.sin(theta1) * math.sin(theta2) * math.cos(phi1 - phi2) + math.cos(theta1) * math.cos(theta2)))

def spherical_surface_distance(r, theta1, phi1, theta2, phi2):
    return r * math.acos(math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(theta1 - theta2))

def main():
    x1, y1, x2, y2 = 1, 2, 4, 6
    print(f"2D Distance: {distance_2d(x1, y1, x2, y2)}")

    z1, z2 = 3, 7
    print(f"3D Distance: {distance_3d(x1, y1, z1, x2, y2, z2)}")

    r1, theta1, r2, theta2 = 5, 30, 10, 60
    print(f"Polar Distance: {polar_distance(r1, theta1, r2, theta2)}")

    phi1, phi2 = 45, 60
    print(f"Spherical Distance: {spherical_distance(r1, theta1, phi1, r2, theta2, phi2)}")

    sphere_radius = 10
    print(f"Spherical Surface Distance: {spherical_surface_distance(sphere_radius, theta1, phi1, theta2, phi2)}")

if __name__ == "__main__":
    main()
