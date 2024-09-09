import random
import time
from datetime import datetime

class Battery:
    def __init__(self):
        self.battery_level = 100
        self.is_solar_charging = False

    def show_battery_percentage(self):
        print(f"[{self.timestamp()}] Battery Percentage: {self.battery_level}% ")

    def solar_charge(self):
        self.is_solar_charging = True
        while self.is_solar_charging and self.battery_level < 100:
            self.charge()
            time.sleep(1)
        self.is_solar_charging = False
    
    def stop_solar_charge(self):
        if self.battery_level >= 100:
            self.stop_solar_charging = False
            print(f"[{self.timestamp()}] Battery Full!!!")
    
    def charge(self):
        if self.battery_level < 100:
            self.battery_level += 1
            print(f"[{self.timestamp()}] Battery is charging.....")
        else:
            self.stop_solar_charge()

    def timestamp(self):
        return datetime.now().strftime('%H:%M:%S')

class ObjectDetector:
    def __init__(self):
        self.detected_objects = []

    def detect_objects(self):
        objects = ["Car","Tree","Road Sign","Pedestrian"]
        detected_object = random.choice(objects)
        self.detected_objects.append(detected_object)
        return detected_object
    
    def clear_detected_objects(self):
        self.detected_objects = []

class LaneDetector:
    def __init__(self):
        self.lane = None

    def detect_lane(self):
        lanes = ["Left","Right","Center"]
        self.lane = random.choice(lanes)
        return self.lane
    
class TrafficLightDetector:
    def __init__(self):
        self.traffic = None

    def detect_traffic_light(self):
        traffic_lights = ["Red","Yellow","Green"]
        self.traffic_light = random.choice(traffic_lights)
        return self.traffic_light
    
class WeatherDetector:
    def __init__(self):
        self.weather = None

    def detect_weather(self):
        weather = ["Sunny","Rainy","Cloudy"]
        self.weather = random.choice(weather)
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
        self.current_location = None
        self.is_self_driving = False
        self.speed = 0
        self.route = []
        self.route_index = 0
        self.starting_location = None

    def set_target_location(self, location):
        if location:
            self.target_location = location
            self.route = self.generate_route(location)
            self.route_index = 0
            print(f"[{self.get_timestamp()}] Target location set: {self.target_location}.")
        else:
            print(f"[{self.get_timestamp()}] Invalid target location.")

    def generate_route(self,target_location):
        return [f"Location {i + 1}" for i in range(random.randint(3,7))] + [target_location]

    def start_self_driving(self):
        if self.target_location:
            self.is_self_driving = True
            self.speed = 60
            self.starting_location = "Starting Location"
            self.current_location = self.starting_location
            print(f"[{self.get_timestamp()}] 🚗 Car started driving from {self.starting_location} to {self.target_location} at speed {self.speed} km/h.")
        else:
            print(f"[{self.get_timestamp()}] Cannot start driving. Target location not set.")

    def update_location(self):
        if self.is_self_driving:
            if self.route_index < len(self.route):
                self.current_location = self.route[self.route_index]
                print(f"[{self.get_timestamp()}] 🚀 Moving to {self.current_location}.")
                self.route_index += 1

                if self.current_location == self.target_location:
                    print(f"[{self.get_timestamp()}] 🎉 Target location '{self.target_location}' has been reached.")
                    self.stop_car()
                    self.set_target_location("New Destination") 

                elif self.route_index >= len(self.route):
                    print(f"[{self.get_timestamp()}] 🚧 End of route reached. Please set a new target location.")
                    self.stop_car()

                self.battery.battery_level -= 1
                if self.battery.battery_level <= 0:
                    print(f"[{self.timestamp()}] ⚠️ Battery used up. Car has stopped.")
                    self.stop_car()
            else:
                print(f"[{self.get_timestamp()}] 🚧 End of route reached. Please set a new target location.")
        else:
            print(f"[{self.get_timestamp()}] Car is not in self-driving mode.")

    def detect_objects(self):
        detected_object = self.object_detector.detect_objects()
        object_symbol = self.get_object_symbol(detected_object)
        print(f"[{self.get_timestamp()}] {object_symbol} Detected Objects: {detected_object}")
        if detected_object.lower() == "pedestrian":
            self.stop_car()
        elif detected_object.lower() == "car":
            self.adjust_speed()

    def get_object_symbol(self,detected_objects):
        symbols = {
            "Car": "🚗",
            "Tree": "🌳",
            "Road Sign": "🚧",
            "Pedestrian": "🚶"
        }
        return symbols.get(detected_objects, "❓")

    def stop_car(self):
        print(f"[{self.get_timestamp()}] 🛑 Car Stopped.")
        self.is_self_driving = False
        self.speed = 0

    def adjust_speed(self):
        self.speed = max(self.speed -10, 20)
        print(f"[{self.get_timestamp()}] ⚙️  Speed adjusted to {self.speed}.")

    def show_battery_percentage(self):
        self.battery.show_battery_percentage()

    def detect_lane(self):
        lane = self.lane_detector.detect_lane()
        lane_symbol = self.get_lane_symbol(lane)
        print(f"[{self.get_timestamp()}] {lane_symbol}  Detected Lane: {lane}")
        if lane == "left":
            self.steer_left()
        elif lane == "right":
            self.steer_right()

    def get_lane_symbol(self, lane):
        symbols = {
            "Left": "↩️",
            "Right": "↪️",
            "Center": "⏺️"
        }
        return symbols.get(lane, "❓")

    def steer_left(self):
        print(f"[{self.get_timestamp()}] ↩️ Steering left.")

    def steer_right(self):
        print(f"[{self.get_timestamp()}] ↪️ Steering right.")

    def detect_traffic_light(self):
        traffic_light = self.traffic_detector.detect_traffic_light()
        print(f"[{self.get_timestamp()}] 🚦 Detected traffic light: {traffic_light}")
        if traffic_light == "Red":
            self.stop_car()
        elif traffic_light == "Yellow":
            self.adjust_speed()
        else:
            print(f"[{self.get_timestamp()}] ✅ Continue driving! ") 

    def detect_weather(self):
        weather = self.weather_detector.detect_weather()
        print(f"[{self.get_timestamp()}] ☁️  Detected Weather: {weather}")
        if weather == "Rainy":
            print(f"[{self.get_timestamp()}] 🌧️  Slowing down due to rain.")
            self.adjust_speed()
        elif weather == "Sunny":
            print(f"[{self.get_timestamp()}] 🌞 NO adjustments needed.")
        else:
            print(f"[{self.get_timestamp()}] 🌥️  Cloudy weather, no adjustments needed.")

    def get_timestamp(self):
        return datetime.now().strftime('%H:%M:%S')

car_obj = Autopilot()
car_obj.set_target_location("Home")
car_obj.start_self_driving()

while car_obj.is_self_driving:
    time.sleep(2)
    car_obj.update_location()
    car_obj.detect_objects()
    car_obj.detect_lane()
    car_obj.detect_traffic_light()
    car_obj.detect_weather()
    car_obj.show_battery_percentage()
    print("\n****************************************************\n")
