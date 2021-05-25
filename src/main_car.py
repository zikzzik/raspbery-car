from lib.CarController import CarController


if __name__ == "__main__":
    CarController(car_name="my_car", host="localhost", port=9345, action_time=1, speed=50).run()