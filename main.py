"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.0 # charge for sign
numChars = int(input("Enter the number of characters on the sign: ")) # type number of characters in sign 
color = input("Enter the color of the text/characters: ").lower() # color of text/characters
woodType = input("Enter the type of wood: ").lower() # type of wood


# Charge for this sign.
charge = 35.00 # minimum charge


# Write assignment and if statements here as appropriate.

if numChars > 5: # if more than 5 characters, add $4 for each character over 5
    charge += (numChars - 5) * 4 # $4 for each character over 5

if woodType == "oak": # if wood type is oak, add $20
    charge += 20.00 # add $20 for oak wood

if color == "gold": # if color is gold, add $15
    charge += 15.00 # add $15 for gold color


# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
