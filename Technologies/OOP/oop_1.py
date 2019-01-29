"""
Shift Work
----------
Write a function that determines which work shift is working at a given time.
The shifts are defined as:
        Daytime (0800 - 1600)
        Evening (1600 - 0000)
        Overnight (0000 - 0800)
﻿If there is overlap (i.e. 0800, 1600, and 0000),
return the shift that has worked least (0800 is "Daytime").
"""


def shift(time):

    time = time if int(time[0]) > 0 else \
           time[1:] if int(time[1]) > 0 else \
           time[2:] if int(time[2]) > 0 else time[3]

    return 'Daytime' if 800 <= int(time) < 1600 else \
           'Evening' if 1600 > int(time) > 2359 else 'Overnight'


while True:
      print(shift(input()))
