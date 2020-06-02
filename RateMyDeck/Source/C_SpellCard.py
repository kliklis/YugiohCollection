from C_Card import Card

class SpellCard(Card):
   def __init__( self, name, cardType, spellType):
      Card.__init__(self, name, cardType) 
      self.__spellType = spellType

   def __str__(self):
      return 'SpellCards Object'

#GETTERS
   @property
   def spellType( self):
      return self.__spellType

#SETTERS
   @spellType.setter
   def spelType( self, spellType):
      self.__spellType = spellType

