import pytest
from racecar import RaceCar
from exceptions import InvalidAcceleraionState
from exceptions import InvalidHornState


RACECAR_COLOR = "Red"
MAX_SPEED_VALUE = 2
ACCELERATION_VALUE = 1
TYRE_FRICTION = 1
NITRO_VALUE = 1


@pytest.fixture
def racecar():
    racecar_obj = RaceCar(
        color=RACECAR_COLOR,
        max_speed=MAX_SPEED_VALUE,
        acceleration=ACCELERATION_VALUE,
        tyre_friction=TYRE_FRICTION,
        nitro=NITRO_VALUE,
    )
    return racecar_obj


@pytest.mark.parametrize(
    ("color", "max_speed", "acceleration", "tyre_friction", "nitro"),
    (("Red", 250, 10, 20, 500), ("Blue", 300, 20, 50, 1000)),
)
def test_racecar_constructor_valid_inputs(
    color, max_speed, acceleration, tyre_friction, nitro
):
    racecar_obj = RaceCar(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        nitro=nitro,
    )

    assert racecar_obj.color == color
    assert racecar_obj.max_speed == max_speed
    assert racecar_obj.tyre_friction == tyre_friction
    assert racecar_obj.acceleration == acceleration
    assert racecar_obj.is_engine_started == False
    assert racecar_obj.current_speed == 0


def test_start_engine(racecar):
    racecar.start_engine()
    assert racecar.is_engine_started == True


def test_display_racecar_speed_when_accelerated(racecar):
    racecar.start_engine()
    racecar.accelerate()
    assert racecar.current_speed == ACCELERATION_VALUE


def test_acceleration_when_racecar_not_start(racecar):
    with pytest.raises(InvalidAcceleraionState) as e:
        assert racecar.accelerate()
    assert str(e.value) == "Start the engine to accelerate"

    assert racecar.current_speed == 0


def test_applying_break_when_already_stopped(racecar):
    racecar.apply_brakes()
    assert racecar.current_speed == 0


def test_applying_break(racecar):
    racecar.start_engine()
    racecar.accelerate()

    racecar.apply_brakes()
    assert racecar.current_speed == ACCELERATION_VALUE - TYRE_FRICTION


def test_sound_horn_when_racecar_engine_off(racecar):
    with pytest.raises(InvalidHornState) as e:
        assert racecar.sound_horn()
    assert str(e.value) == "Start the engine to sound_horn"


def test_sound_horn_when_racecar_engine_on(racecar):
    racecar.start_engine()
    assert racecar.sound_horn() == "Peep Peep\nBeep Beep"


def test_stop_engine(racecar):
    racecar.start_engine()
    racecar.stop_engine()
    assert racecar.is_engine_started == False
    assert racecar.current_speed == 0


def test_stop_engine_with_positive_current_speed(racecar):
    racecar.start_engine()
    racecar.accelerate()
    racecar.stop_engine()

    assert racecar.is_engine_started == False
    assert racecar.current_speed == 0


def test_setting_protected_variables(racecar):
    with pytest.raises(AttributeError) as e:
        racecar.is_engine_started = True
    assert str(e.value) == "can't set attribute 'is_engine_started'"
