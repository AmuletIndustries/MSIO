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
        inputs.start_key_check()
        # Preceding function sleeps for 0.05
        ctrl()


def ctrl():
    # This loop turns on the lights
    # while True:
    print("inf_loop3 running")
    if inputs.red_switch():
        print("RED light function on was called")
        outputs.light_red_on(inputs.key)
    else:
        print("RED light function off was called")
        outputs.light_red_off(inputs.key)
    if inputs.green_switch():
        print("GREEN light function on was called")
        outputs.light_green_on(inputs.key)
    else:
        print("GREEN light function off was called")
        outputs.light_green_off(inputs.key)
    if inputs.blue_switch():
        print("BLUE light function on was called")
        outputs.light_blue_on(inputs.key)
    else:
        print("BLUE light function off was called")
        outputs.light_blue_off(inputs.key)


inf_loop1()
