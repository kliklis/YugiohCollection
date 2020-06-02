class Combo:
   def __init__( self, comboName, cardsRequired, description):
      self.__comboName = comboName
      self.__cardsRequired = cardsRequired
      self.__description = description

   def __str__(self):
      return 'Combo Object'

#GETTERS
   @property
   def comboName( self):
      return self.__comboName

   @property
   def cardsRequired( self):
      return self.__cardsRequired

   @property
   def description( self):
      return self.__description

#SETTERS
   @comboName.setter
   def comboName( self, comboName):
      self.__comboName = comboName

   @cardsRequired.setter
   def cardsRequired( self, cardsRequired):
      self.__cardsRequired = cardsRequired

   @description.setter
   def description( self, description):
      self.__description = description

