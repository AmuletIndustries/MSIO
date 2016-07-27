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
        # Preceding function sleeps for 0.05
        inf_loop2(settings.redSwitch)
        inf_loop3(redSwitch)


def inf_loop2(redSwitch):
    # This loop tests for the three color selection buttons
    # while True:
    inputs.red_switch(redSwitch)  # Function sleeps for 0.05
    return redSwitch


def inf_loop3(redSwitch):
    # This loop turns on the lights
    # while True:
    print("inf_loop3 running")
    if redSwitch:
        print("RED light function on was called")
        outputs.light_red_on(settings.key)
    else:
        print("RED light function off was called")
        outputs.light_red_off(settings.key)
    """if settings.greenSwitch:
        outputs.light_red_on()
        print("GREEN light function on was called")
    else:
        outputs.light_red_off()
        print("GREEN light function off was called")"""


inf_loop1()
