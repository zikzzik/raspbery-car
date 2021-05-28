from lib.CommandController import CommandController


if __name__ == "__main__":
    CommandController("my_car", host="192.168.0.1", port=9001).run()