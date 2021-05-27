from lib.CarController import CarController


if __name__ == "__main__":
    CarController(car_name="my_car", host="192.168.0.1", port=9000, action_time=0.5, speed=50).run()