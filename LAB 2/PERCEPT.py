"""Reproducible thermostat percept sequence."""
def sample_percepts():
    return [
        {"temperature":29,"occupied":True,"label":"Initial cooling demand"},
        {"temperature":29,"occupied":True,"label":"Repeated same percept"},
        {"temperature":26,"occupied":True,"label":"Exact upper boundary"},
        {"temperature":17,"occupied":True,"label":"Transition to heating"},
        {"temperature":17,"occupied":True,"label":"Repeated heating demand"},
        {"temperature":18,"occupied":True,"label":"Exact lower boundary"},
        {"temperature":22,"occupied":False,"label":"Empty room priority"},
    ]
