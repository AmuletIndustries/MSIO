import settings
import inputs

settings.init()

"""WARNING: the proceding function will be a infinite loop!
DO NOT CALL NON-TIMED FUNCTIONS IN THIS FUNCTION
"""

def inf_loop():
    while True:
        inputs.start_key_check(key) #Function contains sleep of 0.1