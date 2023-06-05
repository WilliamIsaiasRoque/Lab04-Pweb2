from interpreter import draw
from chessPictures import *

attack = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
pawns = pawn.horizontalRepeat(8)
squarenegative = square.negative() 
squarewhite = squarenegative.negative()

fila = squarewhite.join(squarenegative).horizontalRepeat(4)
filax4=fila.negative().up(fila).verticalRepeat(2)

filax8=fila.negative().up(fila).verticalRepeat(4)

super=square.under(rock)
draw(super)




