"""
CP1404 Practical
make a hex colour code dictionary
invalid option should not crash
entering '' should end loop
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"}

colour = (input("Enter colour: ")).lower()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "hex colour code is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = (input("Enter colour: ")).lower()