class Tap:
    def __init__(self) -> None:
        pass

    def sensor(self, sensor:bool):
        if sensor == True:
            print("Tap opened.")
        else:
            print("Don't open the tap.")

tap_obj = Tap()
while True:
    tap_obj.sensor(sensor = True)
    break