from exceptions import InvalidAcceleraionState
from exceptions import InvalidHornState


class Car:
    def __init__(self, max_speed, acceleration, tyre_friction, color="Red"):
        self._color = color
        self._acceleration = acceleration
        self._is_engine_started = False
        self._current_speed = 0

        self._tyre_friction = tyre_friction
        if max_speed < 0:
            raise ValueError('Invalid value for max_speed')
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
            raise InvalidAcceleraionState("Start the engine to accelerate")
        elif self._is_engine_started and self.current_speed + self.acceleration <= self.max_speed:
            self._current_speed += self.acceleration

    def apply_brakes(self):
        if self._current_speed > self.tyre_friction:
            self._current_speed -= self.tyre_friction
        else:
            self._current_speed = 0

    def sound_horn(self):
        if self._is_engine_started:
            return "Beep Beep"
        else:
            raise InvalidHornState("Start the engine to sound_horn")


class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, nitro):
        super().__init__(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )
        self.nitro = nitro

    def accelerate(self):
        if self.nitro > 0:
            if self.is_engine_started:
                self.nitro -= 1
                super().accelerate()

    def sound_horn(self):
        if self.is_engine_started:
            return "Peep Peep\nBeep Beep"
        else:
            raise InvalidHornState("Start the engine to sound_horn")
