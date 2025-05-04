import stdrandom
import stddraw
import random
import stdio

POINT_SIZE = 0.002
SHOW_PRODUCTION = True 
STAR_PROBABILITY = 0.01

def random_colour():
    return stddraw.color.Color(int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

def colour_avg(colours: list[stddraw.color.Color]):
    r,g,b = 0,0,0
    for colour in colours:
        r += colour.getRed()
        g += colour.getGreen()
        b += colour.getBlue()

    r = int(r / len(colours))
    g = int(g / len(colours))
    b = int(b / len(colours))

    return stddraw.color.Color(r,g,b)

def colour_add(colour, r, g, b):
    return stddraw.color.Color(
        min(255, max(0, int(colour.getRed() + r))),
        min(255, max(0, int(colour.getGreen() + g))),
        min(255, max(0, int(colour.getBlue() + b)))
    )

# c1 c2
# c3 c4
def plasma_cloud(x, y, size, spread, c1, c2, c3, c4, wc1 = True, wc2 = True, wc3 = True, wc4 = True):
    if size < POINT_SIZE:
        return
    
    if wc1:
        stddraw.setPenColor(c1)
        stddraw.filledSquare(x, y, POINT_SIZE)
    
    if wc2:
        stddraw.setPenColor(c2)
        stddraw.filledSquare(x + size, y, POINT_SIZE)

    if wc3:
        stddraw.setPenColor(c3)
        stddraw.filledSquare(x, y + size, POINT_SIZE)

    if wc4:
        stddraw.setPenColor(c4)
        stddraw.filledSquare(x + size, y + size, POINT_SIZE)

    dr, dg, db = stdrandom.gaussian(0, spread), stdrandom.gaussian(0, spread), stdrandom.gaussian(0, spread) 
    if random.random() < STAR_PROBABILITY:
        dr, dg, db = 255, 255, 255

    c1c2 = colour_avg([c1, c2])
    c1c3 = colour_avg([c1, c3])
    c2c4 = colour_avg([c2, c4])
    c3c4 = colour_avg([c3, c4])
    c1c2c3c4 = colour_add(colour_avg([c1, c2, c3, c4]), dr, dg, db)

    # c1   c1c2   c2
    # 
    # c1c3 c1234  c2c4
    #
    # c3   c3c4   c4
    
    plasma_cloud(x, y, size / 2, spread, c1, c1c2, c1c3, c1c2c3c4, False, True, True, True)
    plasma_cloud(x + size / 2, y, size / 2, spread, c1c2, c2, c1c2c3c4, c2c4, False, False, False, True)
    plasma_cloud(x, y + size / 2, size / 2, spread, c1c3, c1c2c3c4, c3, c3c4, False, False, False, True)
    plasma_cloud(x + size / 2, y + size / 2, size / 2, spread, c1c2c3c4, c2c4, c3c4, c4, False, False, False, False)

    if SHOW_PRODUCTION:
        stddraw.show(0)
    

def main():
    stddraw.setPenRadius(POINT_SIZE)
    stddraw.setCanvasSize(500, 500)
    plasma_cloud(0, 0, 1, 20,  stddraw.color.RED, stddraw.color.BLACK, stddraw.color.PINK, stddraw.color.BLUE)#random_colour(), random_colour(), random_colour(), random_colour()) 
    stddraw.show()

if __name__ == "__main__":
    main()
