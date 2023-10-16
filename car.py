from exceptions import InvalidAcceleraionState
from exceptions import InvalidHornState

INVALID_ACCELERATION_STATE_MESSAGE = "Start the engine to accelerate"
INVALID_HORN_STATE_MESSAGE = "Start the engine to sound_horn" 
INVALID_MAX_SPEED_VALUE_MESSAGE = "Invalid value for max_speed"
HORN_SOUND_MESSAGE = "Beep Beep"

class Car:
    def __init__(self, max_speed, acceleration, tyre_friction, color="Red"):
        self._color = color
        self._acceleration = acceleration
        self._is_engine_started = False
        self._current_speed = 0

        self._tyre_friction = tyre_friction
        if max_speed < 0:
            raise ValueError(INVALID_MAX_SPEED_VALUE_MESSAGE)
        else:
            self._max_speed = max_speed

    @property
    def current_speed(self):
        return self._current_speed
    
    @property
    def color(self):
        return self._color
    
    @property
    def acceleration(self):
        return self._acceleration

    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    @property
    def tyre_friction(self):
        return self._tyre_friction

    @property
    def max_speed(self):
        return self._max_speed
    
    def start_engine(self):
        self._is_engine_started = True

    def stop_engine(self):
        self._current_speed = 0
        self._is_engine_started = False

    def accelerate(self):
        if not self.is_engine_started:
            raise InvalidAcceleraionState(INVALID_ACCELERATION_STATE_MESSAGE)
        elif self.current_speed + self.acceleration <= self.max_speed:
            self._current_speed += self.acceleration
    
    def apply_brakes(self):
        if self._current_speed > self.tyre_friction:
            self._current_speed -= self.tyre_friction
        else:
            self._current_speed = 0

    def sound_horn(self):
        if self._is_engine_started:
            return HORN_SOUND_MESSAGE
        else:
            raise InvalidHornState(INVALID_HORN_STATE_MESSAGE)
