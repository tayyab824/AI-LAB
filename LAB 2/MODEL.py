"""Stateful thermostat. Assumed inclusive comfort band: 18-26 C."""
MIN_TEMP=18
MAX_TEMP=26
class ThermostatAgent:
    def __init__(self):
        self.previous_target_mode=None
    def choose_target(self,percept):
        if not percept["occupied"]:
            return "OFF"                 # occupancy priority
        if percept["temperature"] < MIN_TEMP:
            return "HEAT"
        if percept["temperature"] > MAX_TEMP:
            return "COOL"
        return "OFF"
    def step(self,percept):
        previous=self.previous_target_mode
        target=self.choose_target(percept)
        should_send=(target != previous)
        self.previous_target_mode=target
        return target,should_send,previous
