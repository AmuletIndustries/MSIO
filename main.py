import settings
import inputs
import outputs

settings.init()

"""WARNING: the proceding functions are an infinite loop!
DO NOT CALL NON-TIMED FUNCTIONS IN THESE FUNCTIONS
"""


def inf_loop1():
    # This loop tests solely for the control key
    while True:
        inputs.start_key_check(settings.key, settings.keyChange)
        # Preceding function sleeps for 0.5
        inf_loop2()


def inf_loop2():
    # This loop tests for the three color selection buttons
    # while True:
    inputs.red_switch(settings.redSwitch)  # Function sleeps for 0.05
    # return redSwitch


def inf_loop3():
    # This loop turns on the lights
    while True:
        if settings.redSwitch:
            outputs.light_red_on()
            print("RED light function on was called")
        elif not settings.redSwitch:
            outputs.light_red_off()
            print("RED light function off was called")
        elif settings.greenSwitch:
            outputs.light_red_on()
            print("GREEN light function on was called")
        elif not settings.greenSwitch:
            outputs.light_red_off()
            print("GREEN light function off was called")


inf_loop1()
inf_loop2()
inf_loop3()
