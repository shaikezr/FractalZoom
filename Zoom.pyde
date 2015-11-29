from Complex import *

C = Complex(0,0)

IMAX = 150
xmin = -2.5
xmax = 1.5
ymin = -2
ymax = 2
zoomFactor = 5
counter = 0

fractalList = []
initFrac = None

def setup():
    global C, IMAX, xmin, xmax, ymin, ymax,initFrac, fractalList, counter
    size(200,200)
    initFrac = createImage(width,height,RGB)
    initFrac.loadPixels()
    for i in range(width-1):
        for j in range(height-1):
            C.real = map(i,0,width-1,xmin,xmax)
            C.imag = map(j,0,height-1,ymax,ymin)
            x = iterate(C,2,IMAX)
            initFrac.pixels[i+j*width]=pixColor(x)
    initFrac.updatePixels()
    save("fractal{0}.png".format(str(counter)))
        
def f(x):
    return 1-(x**2)

def pixColor(x):
    return color(255*f(map(x,0,IMAX,-1,1)),50,90)


def iterate(C,L,nmax):
    z = Complex(0,0)
    n = 0
    while abs(z) <= L and n <= nmax-1:
        z = z*z + C
        n += 1
    return n

def draw():
    global zoomFactor, initFrac
    background(0)
    image(initFrac,0,0)
    fill(255,255,255,128) #White transparent rectangle that moves with mouse. the bigger the 4th arg, the more opaque (less transparent)
    stroke(255)
    rectMode(CENTER)
    rect(mouseX,mouseY,width/zoomFactor,height/zoomFactor)
    
 
def generateFractal(xmin,xmax,ymin,ymax):
    global C, IMAX, fractalList, initFrac, counter
    initFrac.loadPixels()
    for i in range(width-1):
        for j in range(height-1):
            C.real = map(i,0,width-1,xmin,xmax)
            C.imag = map(j,0,height-1,ymax,ymin)
            x = iterate(C,2,IMAX)
            initFrac.pixels[i+j*width]=pixColor(x)
    initFrac.updatePixels()
    save("fractal{0}.png".format(str(counter)))
    counter+=1

def mousePressed(): #get new min/max values, generate fractal (and in generate fractal update initFrac)
    global C, IMAX, xmin, xmax, ymin, ymax, zoomFactor
    dx = (float(xmax-xmin)/zoomFactor)
    dy = (float(ymax-ymin)/zoomFactor)
    x = map(mouseX,0,width-1,xmin,xmax)
    y = map(mouseY,0,height-1,ymax,ymin)
    xmin = x-(dx/2)
    xmax = x+(dx/2)
    ymin = y-(dy/2)
    ymax = y+(dy/2)
    print("xmin: " + str(xmin) + "\n" + "ymin: " + str(ymin) + "\n" + "xmax: " + str(xmax) + "\n" + "ymax: " + str(ymax))
    generateFractal(xmin,xmax,ymin,ymax)
    
def keyPressed():
    global fractalList, counter, initFrac
    if keyCode == LEFT:
        initFrac = loadImage("fractal{0}.png".format(str(counter-1)))
        counter-=1
