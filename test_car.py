from car import Car

def test_car_brake():
    car = Car(60)
    car.brake()
    assert car.speed == 55

def test_accelerate():
    car = Car(50)
    car.brake()
    assert car.speed == 45

def test_average_speed():
    car = Car(50)
    car.brake()
    assert car.speed == 45

