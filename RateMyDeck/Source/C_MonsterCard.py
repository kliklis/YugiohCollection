from C_Card import Card

class MonsterCard(Card):
   def __init__( self, name, cardType , hasEffect, level, monsterType, attribute, isTuner, isHandtrap):
      Card.__init__(self, name, cardType)
      self.__hasEffect = hasEffect
      self.__level = level
      self.__monsterType = monsterType
      self.__attribute = attribute
      self.__isTuner = isTuner
      self.__isHandtrap = isHandtrap

   def __str__(self):
      return 'MonsterCard Object'

#GETTERS
   @property
   def hasEffect( self):
      return self.__hasEffect

   @property
   def level( self):
      return self.__level

   @property
   def monsterType( self):
      return self.__monsterType

   @property
   def attribute( self):
      return self.__attribute

   @property
   def hasEffect( self):
      return self.__hasEffect

   @property
   def isTuner( self):
      return self.__isTuner

   @property
   def isHandtrap( self):
      return self.__isHandtrap

#SETTERS
   @hasEffect.setter
   def hasEffect( self, hasEffect):
      self.__hasEffect = hasEffect

   @level.setter
   def level( self, level):
      self.__level = level

   @monsterType.setter
   def monsterType( self, monsterType):
      self.__monsterType = monsterType

   @attribute.setter
   def attribute( self, attribute):
      self.__attribute = attribute

   @hasEffect.setter
   def hasEffect( self, hasEffect):
      self.__hasEffect = hasEffect

   @isTuner.setter
   def isTuner( self, isTuner):
      self.__isTuner = isTuner

   @isHandtrap.setter
   def isHandtrap( self, isHandtrap):
      self.__isHandtrap = isHandtrap

