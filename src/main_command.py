from lib.CommandController import CommandController


if __name__ == "__main__":
    CommandController("my_car", host="192.168.1.26", port=9000).run()