import random as r
import math as m

posx = [float(0)]
posy = [float(0)]
posz = [float(0)]
iteration = [int(1)]

def randompos(scale):
    anglex = 2 * m.pi * r.random()
    angley = 0.6 * r.random()
    outputx = scale * m.cos(anglex) * m.cos(angley)
    outputy = scale * m.cos(anglex) * m.sin(angley)
    outputz = scale * m.sin(angley)
    return(outputx, outputy, outputz)

branchesmade = 0

while branchesmade < 100:
    branchesmade +=1
    

output = open(__file__[0:__file__.rfind('\\')+1] + 'Output.obj','w')

for b in range(len(iteration)):
    output.write('v ' + str(posx[b]) + ' ' + str(posy[b]) + ' ' + str(posz[b]) + '\n')
    output.write('v ' + str(posx[b] + 0.1) + ' ' + str(posy[b]) + ' ' + str(posz[b]) + '\n')
    output.write('v ' + str(posx[b]) + ' ' + str(posy[b] + 0.1) + ' ' + str(posz[b]) + '\n')
    output.write('f ' + str(1 + 3 * b) + ' ' + str(2 + 3 * b) + ' ' + str(3 + 3 * b) + '\n')