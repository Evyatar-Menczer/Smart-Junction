import requests
from traffic_light import TrafficLight

# inputs 12,100,2,4
# output [boolean , boolean, boolean, boolean]

# globals:

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MAX_SIGNAL_DURATION = 15  # 15 seconds
STARVATION_THRESHOLD = 3

is_new_state = False

def get_directions_queue(trafic_lights):
    return [trafic_light for trafic_light in sorted(trafic_lights, key=lambda item: item.count)]
    

# STARVATION_THRESHOLD = 3
# trafic_lights = [tNorth,tSouth,tEast,tWest]
# amount, direction = get_direction_and_amount()
# x = {"north":2, "west": 4, "south": 6, "east" :8}
# print(x)
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# print(x)

# for trafic_light in trafic_lights:
#     pass


# returns [boolean , boolean, boolean, boolean]
def calculate(traffic_lights):
    [12,23,34,7]
    lights_queue = get_directions_queue(traffic_lights)
    for light in lights_queue:
        pass
    pass
    
def main():
    # recieving array with the amount of cars in each direction.
    # when the calculation completes, we need to update the number of cars in each direction and the starvations.
    tl_north = TrafficLight(NORTH)
    tl_west = TrafficLight(WEST)
    tl_east = TrafficLight(EAST)
    tl_south = TrafficLight(SOUTH)
    traffic_lights = [tl_north,tl_west, tl_east, tl_south]
    calculate(traffic_lights)
    # response = requests.get("http://api.open-notify.org/astros.json")
    # print(response.json())
    # print(response)

if __name__ == '__main__':

    x = {"north":2, "west": 8, "south": 6, "east" :1}
    print(x)
    
    print(x)
    # main()
