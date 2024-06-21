def print_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

# Prompt user to enter any value for heights
height = int(input("Enter the value of heights: "))
print_right_triangle(height)
