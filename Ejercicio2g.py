from interpreter import draw
from chessPictures import *

squareN=square.negative()

#Reutilizando la filax4 para imprimir squares vacios para el tablero
fila = square.join(squareN).horizontalRepeat(4)
filax4=fila.negative().up(fila).verticalRepeat(2)

#Creando "attack" este contiene el torre,caballo,alfil,rey,reina con su square
attack = squareN.under(rock)
attack = attack.join(square.under(knight)) 
attack = attack.join(squareN.under(bishop))
attack = attack.join(square.under(queen))
attack = attack.join(squareN.under(king))
attack = attack.join(square.under(bishop))
attack = attack.join(squareN.under(knight))
attack = attack.join(square.under(rock))

#creando "pawns" este contiene los 8 peones con su respectivo square
pawns = square.under(pawn)
i=0
while(i<7):
    if i%2==0:
        pawns = pawns.join(squareN.under(pawn))
    else:
        pawns = pawns.join(square.under(pawn))
    i+=1    

#creando los equipos 
whitePawns = pawns
whiteAttack = attack
whiteTeam = whiteAttack.up(whitePawns)
blackTeam= whitePawns.negative().up(whiteAttack.negative())

#creando chesstable y agregando whiteTeam, filax4 y blackTeam
chessTable = whiteTeam.up(filax4).up(blackTeam)
draw(chessTable)



