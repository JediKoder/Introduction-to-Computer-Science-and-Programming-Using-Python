# polySum
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

def polysum(n, s):
    '''
    :param n: number of sides of regular polygon
    :param s: side length
    :return: sum of area and square of the perimeter of the regular polygon (4 decimal places)
    '''

    import math

    area = 0.25 * n * (s**2) / math.tan(math.pi/n)
    perimeter = n * s

    return round(area + (perimeter ** 2), 4)

# Test Cases
print(polysum(9, 6))    # 3138.5457
print(polysum(28, 89))  # 6702169.7359
print(polysum(14, 20))  # 84533.8008