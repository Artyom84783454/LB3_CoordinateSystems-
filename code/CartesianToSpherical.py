import math

pi = 3.14159265358979323846

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r)
    return r, theta, phi

def spherical_to_cartesian(r, theta, phi):
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

def main():
    cartesian_x = [5.0, 1.0, -2.0]
    cartesian_y = [4.0, 5.0, -3.0]
    cartesian_z = [6.0, 2.0, 4.0]
    num_points = 3

    for i in range(num_points):
        r, theta, phi = cartesian_to_spherical(cartesian_x[i], cartesian_y[i], cartesian_z[i])
        print(f"Cartesian coordinates ({cartesian_x[i]}, {cartesian_y[i]}, {cartesian_z[i]}) in the spherical system: (r = {r}, theta = {theta}, phi = {phi})")

    print()

    spherical_r = [8.77, 5.39, 5.39]
    spherical_theta = [pi / 4, pi / 3, -((2 * pi) / 3)]
    spherical_phi = [pi / 5, pi / 3, pi / 4]

    for i in range(num_points):
        x, y, z = spherical_to_cartesian(spherical_r[i], spherical_theta[i], spherical_phi[i])
        print(f"Spherical coordinates (r = {spherical_r[i]}, theta = {spherical_theta[i]}, phi = {spherical_phi[i]}) in the Cartesian system: ({x}, {y}, {z})")

if __name__ == "__main__":
    main()
