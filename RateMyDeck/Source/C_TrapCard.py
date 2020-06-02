from C_Card import Card

class TrapCard(Card):
   def __init__( self, name, cardType, trapType, isHandtrap):
      Card.__init__(self, name, cardType)      
      self.__trapType = trapType
      self.__isHandtrap = isHandtrap

   def __str__(self):
      return 'TrapCard Object'

#GETTERS
   @property
   def trapType( self):
      return self.__trapType

   @property
   def isHandtrap( self):
      return self.__isHandtrap

#SETTERS
   @trapType.setter
   def trapType( self, trapType):
      self.__trapType = trapType

   @isHandtrap.setter
   def isHandtrap( self, isHandtrap):
      self.__isHandtrap = isHandtrap

