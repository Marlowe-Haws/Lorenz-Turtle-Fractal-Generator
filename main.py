## Fractal generator using turtle and tkinter. ##
import turtle
import random
import math
import tkinter as tk
from tkinter import ttk

## Global variables initialized with default values for use with interface. ##
# Initial values for lorenz equations.
x, y, z = 1, 1, 1
# The length in pixels of polygon sides drawn.
side_length = 50
# Smallest number of sides of polygons drawn.
num_sides_min = 3
# Largest number of sides of polygons drawn.
num_sides_max = 3
# How many times polygons are drawn in a group.
grouping = 3
# Angle of left turn after each polygon
angle1 = 160
# Angle of left turn after each group.
angle2 = 150
# The distance in pixels moved between groups of polygons.
move_length = 200
# Number of times groups are drawn.
iterations = 43
# Amount incremented to angle after each polygon is drawn (causes dynamic change over time).
increment_amount = 0.1
# This is a scalar to drastically increase/decrease angle distortion.
modulation_strength = 1
# This is a scalar to minimize the angle distortion caused by the golden ratio.
# You could also use a fraction to amplify instead.
golden_ratio_divisor = 100
# Multiplier to increase/decrease magnitude of lorenz distortion.
lorenz_multiplier = 0.01
# Starting x and y coordinates to recenter shapes that go off the screen.
start_x = 0
start_y = 0
# Turtle global initialization.
my_screen = None
my_turtle = None

## Functions for initializing turtle and drawing the fractal. ##
def initialize_turtle():
    global my_screen, my_turtle
    my_screen = turtle.Screen()
    my_screen.setup(width=1200, height=1000)
    my_screen.bgcolor(0, 0, 0)
    my_turtle = turtle.Turtle()
    my_turtle.color("red")
    my_turtle.speed(0)
    my_turtle.hideturtle()
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

# Lorenz attractor equations.
# This introduces chaotic variation to angle modulation.
def lorenz(x_val, y_val, z_val):
    dx = 10 * (y_val - x_val)
    dy = x_val * (28 - z_val) - y_val
    dz = x_val * y_val - (8/3) * z_val
    return dx, dy, dz

# Generates a random color for each polygon.
def set_random_color():
  r = random.random()
  g = random.random()
  b = random.random()
  return r, g, b

# Function to draw a distorted polygon
def draw_distorted_polygon(current_increment, sides, side, x_val, y_val, z_val):
    """Accepts arguments: angle_increment, # of sides for current polygon, side_length, and the 3 lorenz values.
    This function is where the distortions to the angle occur.
    Scalar global variables are accessed directly here since they are not dynamic."""
    # The angle_increment is passed as increment argument.
    # We access the global increment_amount to determine how impactful the angle_increment is.
    global modulation_strength, golden_ratio_divisor, lorenz_multiplier
    # This is the original angle of the undistorted polygon.
    angle = 360 / sides
    my_turtle.color(set_random_color())
    # This draws each side of the polygon.
    for _ in range(sides):
        # Calculate distortion based on Lorenz attractor
        dx, dy, dz = lorenz(x_val, y_val, z_val)
        # We scale up the distortion by multiplying by the golden ratio.
        # You can also scale down with the divisor variable
        angle_distortion = dx * ( (1 + math.sqrt(5)) / 2 )/golden_ratio_divisor
        # This is the first distortion applied.
        distorted_angle = angle + angle_distortion
        # Then we pass the current incremented value to a sine wave function to make it less linear.
        # Then we multiply this by the modulation strength to minimize/maximize the effect.
        # We add this to the first distortion, then we use modulo 180 on this sum.
        # This keeps angles < 180, which encourages circular/spiral behavior.
        modulated_angle = (distorted_angle + modulation_strength * math.sin(math.radians(current_increment))) % 180
        # This lets us see the angles generated to understand the effects of tweaking parameters.
        print(modulated_angle)

        my_turtle.forward(side)
        my_turtle.left(modulated_angle)

        # Update lorenz values.
        # This is also causing dynamic change over time.
        # And we can also minimize/maximize this effect with the multiplier variable.
        global x, y, z
        x += dx * lorenz_multiplier
        y += dy * lorenz_multiplier
        z += dz * lorenz_multiplier
        # This part bounds the values to < 180, to prevent potential infinity scenarios. 
        x = x % 180
        y = y % 180
        z = z % 180


def draw_distorted_fractal(side, sides_min, sides_max, group, move, reps, increment):
    """Accepts arguments: side_length, num_sides_min, num_sides_max, grouping, move_length, iterations, increment_amount.
    This function draws the overall fractal by recursively calling the draw_distorted_polygon function.
    It tracks the lorenz values and angle_increment through the iterations and passes them to the inner function.
    It also performs turns and movements between drawings."""
    global my_turtle, x, y, z
    angle_increment = 0
    for _ in range(reps):
        x, y, z = 1, 1, 1 # reset lorenz values
        for _ in range(group):
            for polygon in range(sides_min, sides_max + 1):
                draw_distorted_polygon(angle_increment, polygon, side, x, y, z)
                angle_increment += increment
                my_turtle.left(angle1) # Angle of left turn after each polygon.

        my_turtle.penup()
        my_turtle.forward(move)
        my_turtle.left(angle2) #Angle of left turn after each group.
        my_turtle.pendown()

# The Drawing Function (Called from the Button)
def draw_fractal():
    """This fetches all the global variables and reassigns values according to tkinter inputs.
    Then it calls draw_distorted_fractal and passes those values to it."""
    global move_length, side_length, grouping , iterations, num_sides_min, num_sides_max, increment_amount, x, y, z
    global golden_ratio_divisor, angle1, angle2, modulation_strength, lorenz_multiplier, start_x, start_y
    # Get values from the Tkinter entries
    try:
        set_group = int(grouping_entry.get())
        set_move = float(move_length_entry.get())
        set_increment = float(increment_amount_entry.get())
        set_sides_max = int(num_sides_max_entry.get())
        set_sides_min = int(num_sides_min_entry.get())
        set_side_length = float(side_length_entry.get())
        set_iterations = int(iterations_entry.get())
        set_divisor = float(golden_ratio_divisor_entry.get())
        set_angle1 = float(angle1_entry.get())
        set_angle2 = float(angle2_entry.get())
        set_modulation = float(modulation_strength_entry.get())
        set_multiplier = float(lorenz_multiplier_entry.get())
        set_start_x = int(starting_x_entry.get())
        set_start_y = int(starting_y_entry.get())

        # Reassign global variables with these entries.
        side_length = set_side_length
        grouping = set_group
        move_length = set_move
        increment_amount  = set_increment
        num_sides_min = set_sides_min
        num_sides_max = set_sides_max
        iterations = set_iterations
        golden_ratio_divisor = set_divisor
        angle1 = set_angle1
        angle2 = set_angle2
        modulation_strength = set_modulation
        lorenz_multiplier = set_multiplier
        start_x = set_start_x
        start_y = set_start_y

    except ValueError:
           print("Invalid input. Please enter numerical values.")
           return # Prevents drawing if input invalid.

    # We initialize the turtle inside this function so the starting x and y values are updated first.
    # We clear all prior turtle drawings first.
    turtle.clearscreen()
    initialize_turtle()
    draw_distorted_fractal(side_length, num_sides_min, num_sides_max, grouping, move_length, iterations, increment_amount)

# Tkinter Setup (GUI)
root = tk.Tk()
root.title("Fractal Art Generator")

## Create labels and entry fields. ##
# Polygon side length
side_length_label = ttk.Label(root, text="Side length of polygons:")
side_length_label.grid(row=0, column=0, padx=5, pady=5, sticky="e") #Right justified
side_length_entry = ttk.Entry(root)
side_length_entry.insert(0, "50")  # Default value
side_length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w") #left-justified

# Min and max number of sides of polygons.
num_sides_min_label = ttk.Label(root, text="Min polygon sides:")
num_sides_min_label.grid(row=1, column=0, padx=5, pady=5, sticky="e") #Rignum_sides_min
num_sides_min_entry = ttk.Entry(root)
num_sides_min_entry.insert(0, "3")  # Default value
num_sides_min_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w") #left-justified

num_sides_max_label = ttk.Label(root, text="Max polygon sides:")
num_sides_max_label.grid(row=2, column=0, padx=5, pady=5, sticky="e") #Right justified
num_sides_max_entry = ttk.Entry(root)
num_sides_max_entry.insert(0, "3")  # Default value
num_sides_max_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w") #left-justified

# Grouping
grouping_label = ttk.Label(root, text="Number of polygons in group:")
grouping_label.grid(row=3, column=0, padx=5, pady=5, sticky="e") #Right justified
grouping_entry = ttk.Entry(root)
grouping_entry.insert(0, "3")  # Default value
grouping_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w") #left-justified

# First angle
angle1_label = ttk.Label(root, text="The angle of turn after each polygon:")
angle1_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")  # Right justified
angle1_entry = ttk.Entry(root)
angle1_entry.insert(0, "160")  # Default value
angle1_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")  # left-justified

# Second angle
angle2_label = ttk.Label(root, text="The angle of turn after each group:")
angle2_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")  # Right justified
angle2_entry = ttk.Entry(root)
angle2_entry.insert(0, "150")  # Default value
angle2_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")  # left-justified

# Move length
move_length_label = ttk.Label(root, text="Distance moved between groups:")
move_length_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
move_length_entry = ttk.Entry(root)
move_length_entry.insert(0, "200")  # Default value
move_length_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w") #left-justified

# Number of iterations
iterations_label = ttk.Label(root, text="Number of groups (total iterations):")
iterations_label.grid(row=7, column=0, padx=5, pady=5, sticky="e") #Right justified
iterations_entry = ttk.Entry(root)
iterations_entry.insert(0, "43")  # Default value
iterations_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w") #left-justified

# Angle increment
increment_amount_label = ttk.Label(root, text="Increment amount (distorts polygon angle):")
increment_amount_label.grid(row=8, column=0, padx=5, pady=5, sticky="e") #Right justified
increment_amount_entry = ttk.Entry(root)
increment_amount_entry.insert(0, "0.1")  # Default value
increment_amount_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w") #left-justified

# Golden ratio divisor
golden_ratio_divisor_label = ttk.Label(root, text="Golden ratio divisor (reduces angle distortion):")
golden_ratio_divisor_label.grid(row=9, column=0, padx=5, pady=5, sticky="e") #Right justified
golden_ratio_divisor_entry = ttk.Entry(root)
golden_ratio_divisor_entry.insert(0, "100")  # Default value
golden_ratio_divisor_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w") #left-justified

# Modulation strength
modulation_strength_label = ttk.Label(root, text="Modulation strength (amplifies angle distortion):")
modulation_strength_label.grid(row=10, column=0, padx=5, pady=5, sticky="e") #Right justified
modulation_strength_entry = ttk.Entry(root)
modulation_strength_entry.insert(0, "1")  # Default value
modulation_strength_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w") #left-justified

# Lorenz multiplier
lorenz_multiplier_label = ttk.Label(root, text="Lorenz multiplier (decreases/increases distortion):")
lorenz_multiplier_label.grid(row=11, column=0, padx=5, pady=5, sticky="e") #Right justified
lorenz_multiplier_entry = ttk.Entry(root)
lorenz_multiplier_entry.insert(0, "0.01")  # Default value
lorenz_multiplier_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w") #left-justified

starting_x_label = ttk.Label(root, text="Initial x coordinate:")
starting_x_label.grid(row=12, column=0, padx=5, pady=5, sticky="e")
starting_x_entry = ttk.Entry(root)
starting_x_entry.insert(0, "0")  # Default value
starting_x_entry.grid(row=12, column=1, padx=5, pady=5, sticky="w")

starting_y_label = ttk.Label(root, text="Initial y coordinate:")
starting_y_label.grid(row=13, column=0, padx=5, pady=5, sticky="e")
starting_y_entry = ttk.Entry(root)
starting_y_entry.insert(0, "0")  # Default value
starting_y_entry.grid(row=13, column=1, padx=5, pady=5, sticky="w")

# Draw button
draw_button = ttk.Button(root, text="Draw Fractal", command=draw_fractal)
draw_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

root.mainloop() #Run event handler, needs to be last line
