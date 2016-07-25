import settings
import inputs
import outputs

settings.init()

"""WARNING: the proceding functions is an infinite loop!
DO NOT CALL NON-TIMED FUNCTIONS IN THIS FUNCTION
"""

inf_loop1(key)
inf_loop2(redSwitch, greenSwitch, blueSwitch)
inf_loop3(redSwitch, greenSwitch, blueSwitch)


def inf_loop1(key):
    # This loop tests solely for the control key
    while True:
        inputs.start_key_check(key)  # Function contains sleep of 0.5
        return key


def inf_loop2(redSwitch, greenSwitch, blueSwitch):
    # This loop tests for the three color selection buttons
    while True:
        inputs.red_switch(redSwitch)  # Function contains a sleep of 0.05
        return redSwitch


def inf_loop3(redSwitch, greenSwitch, blueSwitch):
    # This loop turns on the lights
    if redSwitch:
        outputs.light_red_on()
        print "RED lights turned on"
    elif not redSwitch:
        outputs.light_red_off()
        print "RED lights turned off"
