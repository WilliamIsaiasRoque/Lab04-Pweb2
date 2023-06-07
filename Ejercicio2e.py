from interpreter import draw
from chessPictures import *

squarenegative = square.negative() 
fila = squarenegative.join(square).horizontalRepeat(4)
draw(fila)
