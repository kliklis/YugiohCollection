class Card:
   def __init__( self, name, cardType):
      self.__name = name
      self.__cardType = cardType

   def __str__(self):
      return 'Card Object'

#GETTERS
   @property
   def name( self):
      return self.__name

   @property
   def cardType( self):
      return self.__cardType

#SETTERS
   @name.setter
   def name( self, name):
      self.__name = name

   @cardType.setter
   def cardType( self, cardType):
      self.__cardType = cardType

