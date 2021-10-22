class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_except(self):
        print("User defined Exception: ", self.msg)


try:
    raise Accident("Crash bw 2 cars")
except Accident as e:
    e.print_except()
