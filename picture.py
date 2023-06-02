from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal=self.img[::-1]
    return horizontal

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for value in self.img:
      value_n = [self._invColor(color) for color in value]
      negative.append(value_n)
    return negative

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joinRslt = []
    i = 0
    while i<len(self.img):
      joinRslt.append(self.img[i]+p.img[i])
      i+=1
    return Picture(joinRslt)
    
  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p bajo la figura actual """
    new_img = p.img + self.img
    return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    new_img = self.img + p.img
    return Picture(new_img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated_img = [pixel for pixel in self.img for _ in range(n)]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n"""
    repeated_img = self.img * n
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

