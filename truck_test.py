import pytest
from truck import Truck
from exceptions import InvalidAcceleraionState
from exceptions import InvalidHornState


TRUCK_COLOR = "Red"
MAX_SPEED_VALUE = 2
ACCELERATION_VALUE = 1
TYRE_FRICTION = 1
MAX_CARGO_WEIGHT = 1


@pytest.fixture
def truck():
    truck_obj = Truck(
        color=TRUCK_COLOR,
        max_speed=MAX_SPEED_VALUE,
        acceleration=ACCELERATION_VALUE,
        tyre_friction=TYRE_FRICTION,
        max_cargo_weight=MAX_CARGO_WEIGHT,
    )
    return truck_obj


@pytest.mark.parametrize(
    ("color", "max_speed", "acceleration", "tyre_friction", "max_cargo_weight"),
    (("Red", 250, 10, 20, 500), ("Blue", 300, 20, 50, 1000)),
)
def test_truck_constructor_valid_inputs(
    color, max_speed, acceleration, tyre_friction, max_cargo_weight
):
    truck_obj = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight,
    )

    assert truck_obj.color == color
    assert truck_obj.max_speed == max_speed
    assert truck_obj.tyre_friction == tyre_friction
    assert truck_obj.acceleration == acceleration
    assert truck_obj.is_engine_started == False
    assert truck_obj.current_speed == 0


def test_start_engine(truck):
    truck.start_engine()
    assert truck.is_engine_started == True


def test_display_truck_speed_when_accelerated(truck):
    truck.start_engine()
    truck.accelerate()
    assert truck.current_speed == ACCELERATION_VALUE


def test_acceleration_when_truck_not_start(truck):
    with pytest.raises(InvalidAcceleraionState) as e:
        assert truck.accelerate()
    assert str(e.value) == "Start the engine to accelerate"

    assert truck.current_speed == 0


def test_applying_break_when_already_stopped(truck):
    truck.apply_brakes()
    assert truck.current_speed == 0


def test_applying_break(truck):
    truck.start_engine()
    truck.accelerate()

    truck.apply_brakes()
    assert truck.current_speed == ACCELERATION_VALUE - TYRE_FRICTION


def test_sound_horn_when_truck_engine_off(truck):
    with pytest.raises(InvalidHornState) as e:
        assert truck.sound_horn()
    assert str(e.value) == "Start the engine to sound_horn"


def test_sound_horn_when_truck_engine_on(truck):
    truck.start_engine()
    assert truck.sound_horn() == "Beep Beep"


def test_stop_engine(truck):
    truck.start_engine()
    truck.stop_engine()
    assert truck.is_engine_started == False
    assert truck.current_speed == 0


def test_stop_engine_with_positive_current_speed(truck):
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()

    assert truck.is_engine_started == False
    assert truck.current_speed == 0


def test_setting_protected_variables(truck):
    with pytest.raises(AttributeError) as e:
        truck.is_engine_started = True
    assert str(e.value) == "can't set attribute 'is_engine_started'"
