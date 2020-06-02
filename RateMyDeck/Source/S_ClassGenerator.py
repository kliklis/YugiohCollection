#Card name tokens attack defence speed ability

input_string = input("Give: \n[CLASS_NAME ATTR_1 ATTR_2 etc.]\n").strip().split(" ")

NUM_OF_ATTR = len(input_string)-1

CLASS_NAME = input_string[0]
input_string.remove(input_string[0])

ATTRIBUTES_NAMES = []
for i in input_string:
    ATTRIBUTES_NAMES.append(i)

output_string = "class "+CLASS_NAME+":\n   def __init__( self"

for i in ATTRIBUTES_NAMES:
    output_string = output_string + ", " + i
output_string = output_string + "):\n"


for i in ATTRIBUTES_NAMES:
    output_string = output_string + "      self.__"+i+" = "+i+"\n"
output_string = output_string + "\n"

output_string = output_string + "   def __str__(self):\n"
output_string = output_string + "      return '"+CLASS_NAME+" Object'\n\n"

output_string = output_string + "#GETTERS\n"
for i in ATTRIBUTES_NAMES:
    output_string = output_string + "   @property\n"
    output_string = output_string + "   def "+i+"( self):\n"
    output_string = output_string + "      return self.__"+i+"\n\n"
output_string = output_string + "#SETTERS\n"
for i in ATTRIBUTES_NAMES:
    output_string = output_string + "   @"+i+".setter\n"
    output_string = output_string + "   def "+i+"( self, "+i+"):\n"
    output_string = output_string + "      self.__"+i+" = "+i+"\n\n"


output_file = open("C_"+CLASS_NAME+".py","w")
output_file.write(output_string)
output_file.close()

print(output_string)
