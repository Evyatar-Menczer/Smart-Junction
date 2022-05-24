import socket
import json
# import requests  # REST requests
from traffic_light import TrafficLight

# globals:
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

MAX_SIGNAL_DURATION = 15  # 15 seconds
STARVATION_THRESHOLD = 5
DURATION_FOR_SINGLE_CAR = 4 # 3 seconds for a single car to pass the junction (in avg)
STARVATION_NORMALIZATION_FACTOR = 4 # Coefficient for division of starvation

traffic_lights = []
# is_new_state = False

# Action Items:
# 1. Sending to Unity: {"direction": "north", "duration": "14.4"}

# TODO:
# 1. Detecting in a situation where there only few cars in a single direction and let them all pass.
# 2. Send minimum duration to pass the junction


def get_light_with_most_cars(trafic_lights):
    queue = [trafic_light for trafic_light in sorted(
        trafic_lights, key=lambda item: item.count)]
    return queue.pop()

# returns the next traffic light that should be green and the duration
def calculate():
    # which traffic light has the most cars?
    for tl in traffic_lights:
        print(tl.starvation, end=' ')
    print()
    light_with_most_cars = get_light_with_most_cars(traffic_lights)
    first_in_queue = update_first_by_starvation(light_with_most_cars)
    duration = calculate_green_light_duration(first_in_queue)
    update_starvations(first_in_queue)
   
    return [first_in_queue.direction, duration]

# Checks starvation of each direction. If starvation reach to the threshold,
# it becomes the first in queue.
def update_first_by_starvation(light_with_most_cars):
    global traffic_lights
    first_in_queue = light_with_most_cars
    lights_with_same_starvation = []
    
    for traffic_light in traffic_lights:
        if first_in_queue.direction == traffic_light.direction:
            continue
        # will not let other traffic lights starve
        if traffic_light.starvation >= STARVATION_THRESHOLD:
            lights_with_same_starvation.append(traffic_light)
            first_in_queue = traffic_light

    if len(lights_with_same_starvation) > 1:
        if lights_with_same_starvation[0].count > lights_with_same_starvation[1].count:
            first_in_queue = lights_with_same_starvation[0]
        else:
            first_in_queue = lights_with_same_starvation[1]
    
    return first_in_queue

def update_starvations(first_in_queue):
    global traffic_lights
    for traffic_light in traffic_lights:
        is_green = first_in_queue.direction == traffic_light.direction
        has_cars = traffic_light.count > 0
        if is_green:
            traffic_light.starvation = 1
        elif has_cars:
            traffic_light.starvation += 1
        # print(traffic_light.starvation, end=' ')
    # print('###')

def calculate_green_light_duration(first_in_queue) -> float:
    global traffic_lights
    # weights:
    # 1. relative_count - the current amount of cars /the total cars in all directions
    # 2. normalized_starvation - the current starvation / maximum starvation
    total_count = sum(tl.count for tl in traffic_lights)
    relative_count = first_in_queue.count / total_count
    normalized_starvation = first_in_queue.starvation / STARVATION_NORMALIZATION_FACTOR
    # formula: 
    duration = (first_in_queue.count / 2) * normalized_starvation * relative_count * DURATION_FOR_SINGLE_CAR 
    
    return duration

def init():
    global traffic_lights
    # traffic lights list maintains its order:
    traffic_lights = [TrafficLight(NORTH), TrafficLight(
        WEST), TrafficLight(EAST), TrafficLight(SOUTH)]
        
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 
    port = 8080
    # bind to the port
    serversocket.bind(("localhost", port))
    # queue up to 5 requests
    serversocket.listen(5)
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))

    while True:
        # establish a connection

        recievedData = clientsocket.recv(1024)
        counts = recievedData.decode()
        print('Data recieved => ', counts)
        countsArray = [int(x) for x in counts.split(",")]
        print("counts after split:", countsArray)
        res = main(countsArray)
        clientsocket.send(json.dumps(res).encode('ascii'))
        # clientsocket.close()



def main(counts):
    # recieving array with the amount of cars in each direction.
    # when the calculation completes, we need to update the number of cars in each direction and the starvations.
    for traffic_light, count in zip(traffic_lights, counts):
        traffic_light.set_count(count)
    duration_and_direction = calculate()
    print(duration_and_direction)
    return duration_and_direction

if __name__ == '__main__':
    init()

    while True:
        print(recv_data_from_unity())








