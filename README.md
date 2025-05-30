## Lorenz-Turtle-Fractal-Generator

A fractal generator with many parameters to draw polygons with chaotic distortion applied to angles. 

This is a major advancement from my original turtle fractal generator. 

I wanted to introduce an element of chaotic behavior to the fractal and I ended up get carried away with this idea.

The original source of chaos was derived from a set of Lorenz equations, which incrementally add to the angle of the polygons drawn.

Then I multiplied this by the golden ratio for fun, and then I divided that by a large scalar to keep the change manageable.

Then I added another variable that increments with each polygon and I fed that into a sine wave function.

Finally, I added these together and used modulo 180 on the sum to create an overall circular/spiral effect. 

# How it works
There's a function to draw polygons based on the number of sides. 

The original angle is calculated for an equilateral polygon of sides n.

There are a number of parameters to control the fractal that is made.

We use the Tkinter interface to accept customizable values for the parameters.

# Choose: 
    * Side length: length in pixels of the sides of polygons to be drawn.
    
    * Min sides: minimum number of sides of polygons drawn.
    
    * Max sides: maximum number of sides of polygons drawn, if different than min, 
    will create all polygons in the range min-max number of sides.
    
    * Grouping: how many polygons are drawn in a group 
    (there will be turns and movement between groups).
    
    * Angle 1: Angle of left turn made after each polygon is drawn, before drawing the next polygon.
    
    * Angle 2: Angle of left turn made after each group of polygons is drawn, before drawing the next group.
    
    * Movement length: distance moved between drawing groups of polygons.
    
    * Iterations: the number of groups drawn, effectively the total iterations. 
    
    * Increment amount: value of increment, which will accumulate,
    and is fed into a sine wave function to distort the angle. 
    
    * Golden ratio divisor: scalar value to reduce the magnitude of the golden ratio's effect on the Lorenz values.
    This is a divisor value, so you could enter a fraction to amplify instead. 
    
    * Modulation magnitude: another scalar value to amplify or reduce the effect of the incremented value on the angle. 
    
    * Lorenz multiplier: yet another scalar value to reduce the magnitude of the Lorenz effect on the angle 
    (or increase if you so choose). 
    

So basically what's going on is you have many different "angles" from which to go about distorting the angles of the polygons that are drawn.

You can adjust the scalar values on each type of distortion to single out one over the others.

For example, you can change the modulation magnitude to 0 and effectively remove the incremented sine wave distortion completely.

Or you could change the Lorenz multiplier to a tiny fraction like 0.000001 or make the golden ratio divisor really large like 100000 to cancel out the Lorenz effect.

Then you could increase the modulation magnitude to amplify the sine wave effect.

You can mix and match with different "concentrations of chaos" generated from these two main mechanisms. 

Adjusting grouping sizes and number of sides of polygons and ranges of polygons drawn and angles of turns made and distance traveled, etc., etc. can all have significant impacts on the resulting fractal. 

There's a ton of potential to make some crazy shapes  with subtle chaotic patterns that would be very hard to imitate. 

It's pretty fun! Enjoy!

I also added parameters to adjust the starting x, y positions of the turtle to recenter images that veer off in some direction. 

# Images

I added a bunch of images that I've generated. This program went through a lot of phases of development.

Some of the early images (low number) might not be easily or at all reproducible with the current version.

I like the current version, though, and I believe it provides the greatest scope for the possible shapes you can make. 


This was just a fun pet project. I'm releasing it under the MIT license. 
