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
    vertical = self.img[::-1]
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for value in self.img:
    	horizontal.append(value[::-1])
    return Picture(horizontal)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    neg_img = []
    for row in self.img:
      neg_row = [self._invColor(pixel) for pixel in row]
      neg_img.append(neg_row)
    return Picture(neg_img)
    
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
    """ Devuelve una nueva figura poniendo la figura p bajo la figura actuaSl """
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
    repeated_img = [row * n for row in self.img]
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

