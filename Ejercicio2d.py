from interpreter import draw
from chessPictures import *

squarenegative = square.negative() 
fila = square.join(squarenegative).horizontalRepeat(4)
draw(fila)   
