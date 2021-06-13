import math
import numpy
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    i = []
    length = 3

    iambient = calculate_ambient(alight, areflect)
    idiffuse = calculate_diffuse(light, dreflect, normal)
    ispecular = calculate_specular(light, sreflect, view, normal)

    for x in range(length):
        i.append(iambient[x] + idiffuse[x] + ispecular[x]))
    limit_color(i)
    
    return i

def calculate_ambient(alight, areflect):
    iambient = []
    length = 3

    for x in range(length):
        iambient.append(alight[x] * areflect[x])

    return iambient

def calculate_diffuse(light, dreflect, normal):
    dvector = light[0]
    dlight = light[1]
    normalize(dvector)
    normalize(normal)
    product = dot_product(normal, dvector)

    idiffuse = []
    length = 3

    for x in range(length):
        idiffuse.append(dlight[x] * dreflect[x] * product[x])

    return idiffuse

def calculate_specular(light, sreflect, view, normal):
    svector = light[0]
    slight = light[1]
    normalize(svector)
    normalize(normal)
    product = dot_product(normal, svector)
    
    ispecular = []
    model = []
    length = 3
    exponent = 2

    for x in range(length):
        model.append(((2 * normal[x] * product[x]) - svector[x]) * view[x])

    for x in range(length):
        ispecular.append(slight[x] * sreflect[x] * pow(model[x], exponent))

    return ispecular 

def limit_color(color):
    output = numpy.clip(color, 0, 255)
    return output

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
