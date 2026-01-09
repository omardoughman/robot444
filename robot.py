class Robot:
    def __init__(self):
        print("Robot initialised")

    def start(self):
        print("Robot started")
        self.loop()

    def loop(self):
        while True:
            print("Robot running...")
            break  # remove this later
