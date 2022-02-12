class TrafficLight:
    def __init__(self, direction) -> None:
        self.count = 0
        self.duration = 0
        self.direction = direction

    def set_count(self, count):
        self.count = count

    def set_duration(self, duration):
        self.duration = duration