from datetime import datetime
import time


class Autopilot(Tesla):
    def __init__(self):
        super().__init__()
        self.target_location = None
        self.current_location = None
        self.is_self_driving = False
        self.speed = 0
        self.route = []
        self.route_index = 0

    def set_target_location(self, location):
        if location:
            self.target_location = location
            self.route = self.generate_route(location)
            self.route_index = 0
            print(f"[{self.get_timestamp()}] Target location set: {self.target_location}.")
        else:
            print(f"[{self.get_timestamp()}] Invalid target location.")

    def generate_route(self, target_location):
        # Simulate a route with intermediate locations
        return [f"Location {i+1}" for i in range(random.randint(3, 7))] + [target_location]

    def start_self_driving(self):
        if self.target_location:
            self.is_self_driving = True
            self.speed = 60
            self.current_location = self.route[self.route_index]  # Start at the first location
            print(f"[{self.get_timestamp()}] 🚗 Car started driving at speed {self.speed} km/h.")
        else:
            print(f"[{self.get_timestamp()}] Cannot start driving. Target location not set.")

    def update_location(self):
        if self.is_self_driving:
            if self.route_index < len(self.route):
                self.current_location = self.route[self.route_index]
                print(f"[{self.get_timestamp()}] 🚀 Moving to {self.current_location}.")
                self.route_index += 1
                
                # Check if the current location is the target location
                if self.current_location == self.target_location:
                    print(f"[{self.get_timestamp()}] 🎉 Target location '{self.target_location}' has been reached.")
                    
                    # Prompt for a new target location or end self-driving
                    self.stop_car()
                    
                    # Optionally: Uncomment the following line to set a new target location automatically
                    # self.set_target_location("New Destination")  
                elif self.route_index >= len(self.route):
                    print(f"[{self.get_timestamp()}] 🚧 End of route reached. Please set a new target location.")
                    self.stop_car()
                    
                # Battery level decreases as long as the car is moving
                self.battery.battery_level -= 1
                if self.battery.battery_level <= 0:
                    print(f"[{self.get_timestamp()}] ⚠️ Battery used up. Car has stopped.")
                    self.stop_car()
            else:
                print(f"[{self.get_timestamp()}] 🚧 End of route reached. Please set a new target location.")
        else:
            print(f"[{self.get_timestamp()}] Car is not in self-driving mode.")

    def detect_objects(self):
        detected_object = self.object_detector.detect_objects()
        object_symbol = self.get_object_symbol(detected_object)
        print(f"[{self.get_timestamp()}] {object_symbol} Detected: {detected_object}")
        if detected_object.lower() == "pedestrian":
            self.stop_car()
        elif detected_object.lower() == "car":
            self.adjust_speed()

    def get_object_symbol(self, detected_object):
        symbols = {
            "Car": "🚗",
            "Tree": "🌳",
            "Road Sign": "🚧",
            "Pedestrian": "🚶"
        }
        return symbols.get(detected_object, "❓")

    def stop_car(self):
        print(f"[{self.get_timestamp()}] 🛑 Car stopped.")
        self.is_self_driving = False
        self.speed = 0

    def adjust_speed(self):
        self.speed = max(self.speed - 10, 20)  # Adjust speed more dynamically
        print(f"[{self.get_timestamp()}] ⚙️ Speed adjusted to {self.speed} km/h.")

    def show_battery_percentage(self):
        self.battery.show_battery_percentage()

    def detect_lane(self):
        lane = self.lane_detector.detect_lane()
        lane_symbol = self.get_lane_symbol(lane)
        print(f"[{self.get_timestamp()}] {lane_symbol} Detected Lane: {lane}")
        if lane == "Left":
            self.steer_left()
        elif lane == "Right":
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
            print(f"[{self.get_timestamp()}] ✅ Green light - continue driving!")

    def detect_weather(self):
        weather = self.weather_detector.detect_weather()
        print(f"[{self.get_timestamp()}] ☁️ Detected Weather: {weather}")
        if weather == "Rainy":
            print(f"[{self.get_timestamp()}] 🌧️ Slowing down due to rain.")
            self.adjust_speed()
        elif weather == "Sunny":
            print(f"[{self.get_timestamp()}] 🌞 No adjustments needed.")
        else:
            print(f"[{self.get_timestamp()}] 🌥️ Cloudy weather - drive carefully.")

    def get_timestamp(self):
        return datetime.now().strftime('%H:%M:%S')

# Example usage
car_obj = Autopilot()
car_obj.set_target_location("Home")
car_obj.start_self_driving()

while car_obj.is_self_driving:
    time.sleep(2)  # Simulate time passing
    car_obj.update_location()
    car_obj.detect_objects()
    car_obj.detect_lane()
    car_obj.detect_traffic_light()
    car_obj.detect_weather()
    car_obj.show_battery_percentage()
    print("\n****************************************************\n")
