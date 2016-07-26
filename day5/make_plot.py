from PIL import Image, ImageDraw
import math

# Returns a tuple corresponding to the given RGB values.
# Convenience function since we never really talked about tuples.
#
# Each of red, green, and blue should be between 0 and 255
def rgb(red, green, blue):
    return (red, green, blue)

# Takes a buffer filled with r,g,b tuples and draws it to the screen.
# 
# buf is a list of lists, where all lists are of equal length (similar to a 2D
# array). The value of each entry is the rgb value at that point in the resulting
# image so:
#
# drawImage([[rgb(255, 0, 0), rgb(0, 255, 0)],
#            [rgb(0, 0, 0),   rgb(0, 0, 255)]])
# 
# draws a 4-pixel image with a red pixel in the upper left corner, a green pixel
# in the upper right corner, a black pixel in the lower left corner, and a red
# pixel in a lower right corner.
#
# This will totally break if you pass it an empty buffer, a buffer whose rows
# are not all the same length, a buffer with invalid rgb values, and probably
# for some other reasons too.
def draw_buffer(buf):
    height = len(buf)
    width = len(buf[0])
    im = Image.new('RGBA', (width, height), (0, 0, 0, 0)) 
    draw = ImageDraw.Draw(im)
    
    for x in range(width):
        for y in range(height):
            draw.point([(x, y)], fill=buf[y][x])
    im.show()

#returns a buffer 2D list
def create_buffer():
	return [[mandelbrot_set_tester(i/1000.0 - 2,j/1000.0 - 1) for i in range(3000)] for j in range(2000)]


#	buff = [[]]
#	for y in range(0,100):
#		buff[y] = []
#		for x in range(0,100):
#			iterations = mandelbrot_set_tester(y/100.0, x/100.0)
#			if iterations > 0:
#				buff[y[x]] = rgb(255,255,255)
#			else:
#				buff[y[x]] = rgb(0,0,0)
#	return buff

#returns the number of iterations it takes to break out of the set
#returns -1 if the point is in the set
def mandelbrot_set_tester(a,b):
	iterations = 1
	c = complex(a,b)
	z = c
	if abs(z) >= 2:
		return rgb(51,102,255)
	while iterations < 100:
		iterations += 1
		z = pow(z,2) + c
		if abs(z) >= 2:
			if iterations < 2:
				return rgb(102,51,255)
			elif iterations < 3:
				return rgb(204,51,255)
			elif iterations < 4:
				return rgb(255,51,204)
			elif iterations < 5:
				return rgb(51,204,255)
			elif iterations < 6:
				return rgb(0,61,245)
			elif iterations < 7:
				return rgb(0, 46,184)
			elif iterations < 8:
				return rgb(255,51,102)
			elif iterations < 9:
				return rgb(51,255,204)
			elif iterations < 10:
				return rgb(184,138,0)
			elif iterations < 11:
				return rgb(245,184,0)
			elif iterations < 15:
				return rgb(255,102,51)
			elif iterations <20:
				return rgb(51,255,102)
			elif iterations < 30:
				return rgb(102,255,51)
			elif iterations < 40:
				return rgb(204,255,51)
			elif iterations < 50:
				return rgb(255,204,51)
			elif iterations < 60:
				return rgb(245,0,61)
			elif iterations < 80:
				return rgb(0,245,184)
			else:
				return rgb(184,0,245)

	return rgb(0,0,0)

# Build a buffer with RGB values (see docs on draw_buffer and rgb functions)
buf = create_buffer()

# Feed it to draw_buffer
draw_buffer(buf)
