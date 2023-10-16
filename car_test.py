import pytest
from car import Car
from car import InvalidAcceleraionState
from car import InvalidHornState


CAR_COLOR = 'Red'
MAX_SPEED_VALUE = 250
ACCELERATION_VALUE = 10
TYRE_FRICTION = 3

@pytest.fixture
def car():
    car_obj = Car(color=CAR_COLOR, 
                  max_speed=MAX_SPEED_VALUE, 
                  acceleration=ACCELERATION_VALUE,
                  tyre_friction=TYRE_FRICTION
                )
    return car_obj

@pytest.mark.parametrize(
        ('color','max_speed','acceleration','tyre_friction'), (
            ('Red',250,10,20),
            ("Blue",300,20,50)
        )
)
def test_car_constructor_valid_inputs(color,max_speed, acceleration, tyre_friction):
    car_obj = Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    assert car_obj.color == color
    assert car_obj.max_speed == max_speed
    assert car_obj.tyre_friction == tyre_friction
    assert car_obj.acceleration == acceleration
    assert car_obj.is_engine_started == False
    assert car_obj.current_speed == 0

def test_start_engine(car):
    car.start_engine()
    assert car.is_engine_started == True

def test_display_car_speed_when_accelerated(car):
    car.start_engine()
    car.accelerate()
    assert car.current_speed == ACCELERATION_VALUE

def test_acceleration_when_car_not_start(car):
    with pytest.raises(InvalidAcceleraionState) as e:
        assert(car.accelerate())
    assert str(e.value) == "Start the engine to accelerate"

    assert car.current_speed == 0

def test_applying_break_when_already_stopped(car):
    car.apply_brakes()
    assert car.current_speed == 0

def test_applying_break(car):
    car.start_engine()
    car.accelerate()

    car.apply_brakes()
    assert car.current_speed == ACCELERATION_VALUE - TYRE_FRICTION

def test_sound_horn_when_car_engine_off(car):
    with pytest.raises(InvalidHornState) as e:
        assert(car.sound_horn())
    assert str(e.value) == "Start the engine to sound_horn"

def test_sound_horn_when_car_engine_on(car):
    car.start_engine()
    assert car.sound_horn() == "Beep Beep"

def test_stop_engine(car):
    car.start_engine()
    car.stop_engine()
    assert car.is_engine_started == False
    assert car.current_speed == 0

def test_stop_engine_with_positive_current_speed(car):
    car.start_engine()
    car.accelerate()
    car.stop_engine()

    assert car.is_engine_started == False
    assert car.current_speed == 0

def test_setting_protected_variables(car):
    with pytest.raises(AttributeError) as e:
        car.is_engine_started = True
    assert str(e.value) == "can't set attribute 'is_engine_started'"



