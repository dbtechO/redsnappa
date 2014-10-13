import Image

def createImage():
    dim = 512
    im = Image.new("RGB", (dim,dim), "white")
    pix = im.load()
    points = ((0,0),(256,256),(512,512))
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
            
    im = Image.merge(im.mode, split)   
    for color in colors:
        Image.new("RGB", im.size, color).show()
    im.show()
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
createImage()