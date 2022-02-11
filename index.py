import requests

# inputs 12,100,2,4

#output [boolean , boolean, boolean, boolean]

# globals:

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MAX_SIGNAL_DURATION = 15  # 15 seconds

lights_queue = []
is_new_state = False


class TrafficLight:
    def __init__(self, direction) -> None:
        self.count = 0
        self.duration = 0
        self.direction = direction

    def set_count(self, count):
        self.count = count

    def set_duration(self, duration):
        self.duration = duration



# returns [boolean , boolean, boolean, boolean]
def calculate(north, east, south, west):
    for i in range(4):
        lights_queue.insert(0, lights_queue.pop())
        print(lights_queue)

    result = max(north, east, south, west)
    return [result == north, result == east, result == south, result == west]


def main():
    tl = TrafficLight(NORTH)
    print(calculate(12, 23, 2, 4))
    # response = requests.get("http://api.open-notify.org/astros.json")
    # print(response.json())
    # print(response)


if __name__ == '__main__':
    main()
