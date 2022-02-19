import requests  # REST requests
from traffic_light import TrafficLight

# globals:
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

MAX_SIGNAL_DURATION = 15  # 15 seconds
STARVATION_THRESHOLD = 3

# is_new_state = False


def get_directions_queue(trafic_lights):
    queue = [trafic_light for trafic_light in sorted(
        trafic_lights, key=lambda item: item.count)]
    return queue.pop()


def calculate(traffic_lights):
    # which traffic light has the most cars?
    first_in_queue = get_directions_queue(traffic_lights)
    for traffic_light in traffic_lights:
        if first_in_queue.direction == traffic_light.direction:
            continue
        # will not let other traffic lights starve
        if traffic_light.starvation >= STARVATION_THRESHOLD:
            first_in_queue = traffic_light

    new_traffic_queue = []
    # Sets the boolean array for the unity.
    for traffic_light in traffic_lights:
        is_green = first_in_queue.direction == traffic_light.direction
        if is_green:
            traffic_light.starvation = 0
        else:
            traffic_light.starvation += 1
        new_traffic_queue.append(traffic_light.starvation)

    return new_traffic_queue


# [1,1,20,20]

# [0,0,0,0]
# [1,1,1,0]
# [2,2,0,1]
# [3,3,1,0]

#  0 0 0 0
#  1 1 1 0
#  2 2 0 1
#  3 0 1 2

def init():
    global traffic_lights
    # traffic lights list maintains its order:
    traffic_lights = [TrafficLight(NORTH), TrafficLight(
        WEST), TrafficLight(EAST), TrafficLight(SOUTH)]

# counts: north, west, east, south


def main(counts):
    # recieving array with the amount of cars in each direction.
    # when the calculation completes, we need to update the number of cars in each direction and the starvations.
    for traffic_light, count in zip(traffic_lights, counts):
        traffic_light.set_count(count)
    current_queue = calculate(traffic_lights)
    print(current_queue)


if __name__ == '__main__':
    init()
    main([23, 14, 5, 18])  # -> [0,1,1,1]
    main([14, 18, 8, 18])  # ->[1,2,2,0]
    main([19, 18, 8, 4])  # ->[0,3,3,1]
    main([9, 19, 9, 19]) #-> [1,4,0,2]
    main([16, 19, 0, 27])  

    # main([13, 7, 7, 5])
