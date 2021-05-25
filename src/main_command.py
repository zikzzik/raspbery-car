from lib.CommandController import CommandController


if __name__ == "__main__":
    CommandController("my_car", host="localhost", port=9345).run()