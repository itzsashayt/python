import math

def time_to_travel_around_planet(robot_speed, planet_diameter):

    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    
    circumference = math.pi * planet_diameter
    
    time = circumference / robot_speed
    
    return time


def print_robot_travel_info(robot_name, robot_speed, planet_name, planet_diameter):
    calculation_1 = time_to_travel_around_planet(robot_speed, planet_diameter)
    
    if isinstance(calculation_1, str):
        print(calculation_1)
    else:
        print(f"Роботу {robot_name} необходимо {calculation_1:.2f} часов, "
              f"чтобы объехать вокруг планеты {planet_name}.")


print_robot_travel_info("Igor_bot V.2.0", 10, "Земля", 12742)

print_robot_travel_info("Rover-1", 15, "Марс", 6779)
print_robot_travel_info("Bot-2024", 0, "Луна", 3474)
print_robot_travel_info("Explorer", 20, "Венера", -12104)