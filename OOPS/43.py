import random
import time
from datetime import datetime

class Battery:
    def __init__(self):
        self.battery_level = 100
        self.is_solar_charging = False

    def show_battery_percentage(self):
        print(f"[{self._timestamp()}] Battery Percentage: {self.battery_level}%")

    def solar_charge(self):
        self.is_solar_charging = True
        while self.is_solar_charging and self.battery_level < 100:
            self.charge()
            time.sleep(1)

    def stop_solar_charge(self):
        if self.battery_level >= 100:
            self.is_solar_charging = False
            print(f"[{self._timestamp()}] Battery Full!!!")

    def charge(self):
        if self.battery_level < 100:
            self.battery_level += 1
            print(f"[{self._timestamp()}] Battery is charging.....")
        else:
            self.stop_solar_charge()

    def _timestamp(self):
        """Get the current timestamp for display."""
        return datetime.now().strftime('%H:%M:%S')

class ObjectDetector:
    def __init__(self):
        self.detected_objects = []

    def detect_objects(self):
        objects = ["Car", "Tree", "Road Sign", "Pedestrian"]
        detected_object = random.choice(objects)
        self.detected_objects.append(detected_object)
        return detected_object

    def clear_detected_objects(self):
        self.detected_objects = []

class LaneDetector:
    def __init__(self):
        self.lane = None

    def detect_lane(self):
        lanes = ["Left", "Right", "Center"]
        self.lane = random.choice(lanes)
        return self.lane

class TrafficLightDetector:
    def __init__(self):
        self.traffic_light = None

    def detect_traffic_light(self):
        traffic_lights = ["Red", "Yellow", "Green"]
        self.traffic_light = random.choice(traffic_lights)
        return self.traffic_light

class WeatherDetector:
    def __init__(self):
        self.weather = None

    def detect_weather(self):
        weathers = ["Sunny", "Rainy", "Cloudy"]
        self.weather = random.choice(weathers)
        return self.weather

class Tesla:
    def __init__(self):
        self.battery = Battery()
        self.object_detector = ObjectDetector()
        self.lane_detector = LaneDetector()
        self.traffic_detector = TrafficLightDetector()
        self.weather_detector = WeatherDetector()

class Autopilot(Tesla):
    def __init__(self):
        super().__init__()
        self.target_location = None
        self.current_location = [0, 0]  # Starting coordinates
        self.is_self_driving = False
        self.speed = 0  # Speed in arbitrary units

    def set_target_location(self, location):
        if location:
            self.target_location = location
            print(f"[{self._timestamp()}] Target location set to: {location}")
        else:
            print("Invalid target location.")

    def start_self_driving(self):
        if self.target_location:
            self.is_self_driving = True
            self.speed = 5  # Set initial speed
            print(f"[{self._timestamp()}] Car started to move at speed {self.speed}.")
        else:
            print("Don't start the car.")

    def update_location(self):
        if self.is_self_driving and self.target_location:
            print(f"[{self._timestamp()}] Current Location: {self.current_location} Moving at speed: {self.speed}")
            
            x_diff = self.target_location[0] - self.current_location[0]
            y_diff = self.target_location[1] - self.current_location[1]
            
            if abs(x_diff) > abs(y_diff):
                self.current_location[0] += 1 if x_diff > 0 else -1
            else:
                self.current_location[1] += 1 if y_diff > 0 else -1

            if self.current_location == self.target_location:
                print(f"[{self._timestamp()}] 🎉 Target location reached!")
                self.is_self_driving = False
                self.speed = 0
            else:
                print(f"[{self._timestamp()}] Car is moving towards the target...")
                self.battery.battery_level -= 1
                if self.battery.battery_level <= 0:
                    print(f"[{self._timestamp()}] ⚠️ Battery depleted! Car has stopped.")
                    self.is_self_driving = False
                    self.speed = 0
        else:
            print(f"[{self._timestamp()}] Car is not in self-driving mode.")

    def detect_objects(self):
        detected_object = self.object_detector.detect_objects()
        print(f"[{self._timestamp()}] 🚗 Detected Object: {detected_object}")
        if detected_object.lower() == "pedestrian":
            self.stop_car()
        elif detected_object.lower() == "car":
            self.adjust_speed()

    def stop_car(self):
        print(f"[{self._timestamp()}] 🛑 Car Stopped.")
        self.is_self_driving = False
        self.speed = 0

    def adjust_speed(self):
        self.speed = max(self.speed - 1, 1)  # Slow down, but not below 1
        print(f"[{self._timestamp()}] ⚙️ Speed adjusted to {self.speed}.")

    def show_battery_percentage(self):
        self.battery.show_battery_percentage()

    def detect_lane(self):
        lane = self.lane_detector.detect_lane()
        print(f"[{self._timestamp()}] 📍 Detected Lane: {lane}")
        if lane.lower() == "left":
            self.steer_left()
        elif lane.lower() == "right":
            self.steer_right()

    def steer_left(self):
        print(f"[{self._timestamp()}] ↩️ Steering left.")

    def steer_right(self):
        print(f"[{self._timestamp()}] ↪️ Steering right.")

    def detect_traffic_light(self):
        traffic_light = self.traffic_detector.detect_traffic_light()
        print(f"[{self._timestamp()}] 🚦 Detected traffic light: {traffic_light}")
        if traffic_light == "Red":
            self.stop_car()
        elif traffic_light == "Yellow":
            self.adjust_speed()
        else:
            print(f"[{self._timestamp()}] ✅ Continue driving!")

    def detect_weather(self):
        weather = self.weather_detector.detect_weather()
        print(f"[{self._timestamp()}] ☁️ Detected Weather: {weather}")
        if weather == "Rainy":
            print(f"[{self._timestamp()}] 🌧️ Slowing down due to rain.")
            self.adjust_speed()
        elif weather == "Sunny":
            print(f"[{self._timestamp()}] 🌞 No adjustments needed.")
        else:
            print(f"[{self._timestamp()}] 🌥️ Cloudy weather, no adjustments needed.")

    def _timestamp(self):
        """Get the current timestamp for display."""
        return datetime.now().strftime('%H:%M:%S')

car_obj = Autopilot()
car_obj.set_target_location([5, 5])  # Example target location as coordinates (x, y)
car_obj.start_self_driving()

while car_obj.is_self_driving:
    time.sleep(1)
    car_obj.update_location()
    car_obj.detect_objects()
    car_obj.detect_lane()
    car_obj.detect_traffic_light()
    car_obj.detect_weather()
    car_obj.show_battery_percentage()
    print("\n****************************************************\n")
