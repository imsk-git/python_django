import random
import time
from colorama import Fore, Style

class Airdefence:
    def __init__(self, enemy_rocket, angle, speed):
        self.enemy_rocket = enemy_rocket
        self.angle = angle
        self.speed = speed
        self.threat_level = None

class Radar(Airdefence):
    def __init__(self, enemy_rocket, angle, speed):
        super().__init__(enemy_rocket, angle, speed)

    def signal(self, signal:bool):
        if signal: 
            print(f"\n{Fore.GREEN}**INCOMING ENEMY ROCKET DETECTED!!** \nAngle:{self.angle} degree \nSpeed:{self.speed} km/hr.\n{Style.RESET_ALL}")
            return True
        else:
            print(f"\n{Fore.RED}No enemy rockets detected.{Style.RESET_ALL}")
            return False

class Control(Airdefence):
    def __init__(self, enemy_rocket, angle, speed):
        super().__init__(enemy_rocket, angle, speed)

    def control_system(self):
        print(f"{Fore.CYAN}**CONTROL SYSTEM ACTIVATED** \nAccessing threat level.....\n{Style.RESET_ALL}")
        if self.speed > 3000 and (self.angle > 45 and self.angle < 135) :
            self.threat_level = 'critical'
            print(f"{Fore.LIGHTGREEN_EX}Threat level: {self.threat_level}\nEnemy rocket is closing in fast!\n{Style.RESET_ALL}")
        elif self.speed > 1500 and (self.angle > 135 and self.angle < 225):
            self.threat_level = 'high'
            print(f"{Fore.YELLOW}Threat level: {self.threat_level}\nEnemy Rocket is approaching.\n{Style.RESET_ALL}")
        else:
            self.threat_level = 'low'
            print(f"{Fore.LIGHTRED_EX}Threat level: {self.threat_level}\n{Style.RESET_ALL}")

class Missile(Control):
    def __init__(self, enemy_rocket, angle, speed):
        super().__init__(enemy_rocket, angle, speed)
        
    def missile_system(self):
        print(f"{Fore.MAGENTA}**MISSILE SYSTEM ACTIVATED**\nLaunching missiles...\n{Style.RESET_ALL}")
        if self.threat_level == 'critical':
            print(f"{Fore.LIGHTGREEN_EX}**LAUNCHING MULTIPLE MISSILES**\n Enemy rocket will be intercepted!{Style.RESET_ALL}")
        elif self.threat_level == 'high':
            print(f"{Fore.YELLOW}**LAUNCHING SINGLE MISSILE**\n Enemy rocket will be engaged.{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTRED_EX}**MISSILE LAUNCH ABORTED**\n Enemy rocket is not a significant threat.{Style.RESET_ALL}")

while True:
    time.sleep(2)
    radar_obj = Radar('enemy_rocket',random.randint(0, 360),random.randint(0, 5000))
    signal = random.choice([True, False])
    if radar_obj.signal(signal):
        control_obj = Control(radar_obj.enemy_rocket, radar_obj.angle, radar_obj.speed)
        control_obj.control_system()
        missile_obj = Missile(control_obj.enemy_rocket, control_obj.angle, control_obj.speed)
        missile_obj.missile_system()
    print(f"\n{Fore.BLUE}********************************************************************************{Style.RESET_ALL}")
 