from interpreter import draw
from chessPictures import *

squarenegative = square.negative() 
squarewhite = squarenegative.negative()
fila = squarewhite.join(squarenegative).horizontalRepeat(4)

draw(fila)   
