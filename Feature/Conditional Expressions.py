"""
Shift Work
----------
Write a function that determines which work shift is working at a given time.
The shifts are defined as:
        Morning (0600 - 1200)
        Daytime (1200 - 1800)
        Evening (1800 - 0000)
        Overnight (0000 - 0600)
﻿If there is overlap (i.e. 0800, 1600, and 0000),
return the shift that has worked least (0800 is "Daytime").
"""

def shift(time):
    # time 1234 is mean 12:34
    return 'Morning' if 600 <= int(time) < 1200 else \
           'Daytime' if 1200 <= int(time) < 1800 else \
           'Evening' if 1800 <= int(time) < 2359 else \
           'Overnight'

while True:
    print(shift(input('try...')))

# Without else ternary operator would be
# if <condition>: result
