import math

pi = 3.14159265358979323846

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def main():
    cartesian_x = [5.0, 10.0, 2.0]
    cartesian_y = [4.0, 5.0, 3.0]
    num_points = 3

    for i in range(num_points):
        r, theta = cartesian_to_polar(cartesian_x[i], cartesian_y[i])
        print(f"Cartesian coordinates ({cartesian_x[i]}, {cartesian_y[i]}) in the polar system: (r = {r}, theta = {theta})")

    print()

    polar_r = [6.0, 11.0, 3.6]
    polar_theta = [pi / 5, pi / 6, pi / 3]

    for i in range(num_points):
        x, y = polar_to_cartesian(polar_r[i], polar_theta[i])
        print(f"Polar coordinates (r = {polar_r[i]}, theta = {polar_theta[i]}) in the Cartesian system: ({x}, {y})")

if __name__ == "__main__":
    main()
