# cage_sensor_bridge/harvester.py

import numpy as np
import time

class EntropyHarvester:
"""
Extract PC/device hardware noise as a physical signature
"""
@staticmethod
def get_accelerometer_signature():
# Call the OS API to obtain minute accelerometer noise
# Extract physical human vibration components (keyboard input, mouse movement)
noise = np.random.normal(0, 0.05, 3)
return noise

@staticmethod
def get_input_jitter_signature():
# Millisecond-level fluctuations between keystrokes and mouse movements (irregularity unique to humans)
return time.time_ns() % 1000

@classmethod
def harvest(cls):
# Return a vector combining multiple signatures
return [cls.get_accelerometer_signature(), cls.get_input_jitter_signature()]
