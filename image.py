import Image
import random

def createImage(points=None, colors=None):
    dim = 512
    im = Image.new("RGB", (dim,dim), "white")
    pix = im.load()
    if points is None:
        points = ((0,0),(256,256),(512,512))
    if colors is None:    
        colors = ((30,120,10),(230,120,50),(120,30,200))
    split = im.split()
    source = (split[0].load(), split[1].load(), split[2].load())
    for x in range(512):
        for y in range(512):
            ratio = ratios((x,y), points)
            for j in range(len(source)):
                source[j][x,y] = 0
                for i in range(len(colors)):
                    source[j][x,y] += int(colors[i][j]*ratio[i])
                    if source[j][x,y] > 256:
                        print "modulus used"
                source[j][x,y] /= len(ratio)               
    im = Image.merge(im.mode, split)   
    im.show()
def getPoints(n, side=512):
    points = []
    colors = []
    for i in range(n):
        pt = []
        color = []
        for i in range(2):
            pt.append(random.randint(0,side-1))
        for i in range(3):
            color.append(random.randint(0,255))
        points.append(pt)
        colors.append(color)
    return (points, colors)
def minDistance(cur, points):
    dist = 1000
    for point in points:
        curDst = distance(cur, point)
        if curDst < dist:
            dist = curDst
    return dist
def ratios(cur, points):
    distances = []
    output = []
    sum = 0    
    for point in points:
        length = distance(cur, point)
        distances.append(length)
        sum +=length
    for dist in distances:
        output.append(1-dist/sum)
    return output
def distance(pt1, pt2):
    return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**(0.5)
definition = getPoints(3)
createImage(definition[0], definition[1])