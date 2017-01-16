from nanpy import (
    SerialManager,
    ArduinoApi
)


class Portal(object):
    def __init__(self):
        self.gate = None

    def open(self, fallback=None):
        try:
            connection = SerialManager()
            self.gate = ArduinoApi(connection=connection)
        except Exception as e:
            print("Failed to connect to Arduino. {}".format(e.message))
            fallback() if fallback else exit(0)

    def loop(self, run, fallback=None):
        try:
            while True:
                run()
        except:
            return fallback() if fallback else False


if __name__ == "__main__":
    portal = Portal()
    portal.open()
