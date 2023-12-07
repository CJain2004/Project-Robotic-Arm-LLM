class Rover:
    rover_geometry = {'l': 10, 'w': 5, 'h': 3}

    def __init__(self, swarm_id, rover_id, rover_location):
        self.swarm_id = swarm_id
        self.rover_id = rover_id
        self.rover_location = rover_location

    def print_rover_info(self):
        print(f"Rover {self.rover_id} in Swarm {self.swarm_id} is at {self.rover_location}")

    def receive_message(self, message_swarm_id, message_rover_id, move_by):
        if self.swarm_id == message_swarm_id and self.rover_id == message_rover_id:
            self.move_rover(move_by)

    def move_rover(self, move_by):
        self.rover_location += move_by


class DaughterRover(Rover):
    def __init__(self, swarm_id, rover_id, rover_location):
        super().__init__(swarm_id, rover_id, rover_location)
        self.rover_geometry = {k: v / 2 for k, v in self.rover_geometry.items()}

    def move_rover(self, move_by):
        super().move_rover(move_by / 2)


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.rovers_used = []

    def print_user_id(self):
        print(f"User ID: {self.user_id}")

    def add_rover(self, rover):
        self.rovers_used.append((rover.swarm_id, rover.rover_id))

    def remove_rover(self, rover):
        self.rovers_used.remove((rover.swarm_id, rover.rover_id))


class Scientist(User):
    def add_rover(self, rover):
        print("Scientists are not allowed to add/remove rovers.")

    def remove_rover(self, rover):
        print("Scientists are not allowed to add/remove rovers.")

    def print_rover_location(self, rover):
        rover.print_rover_info()


class Operator(User):
    def move_rover(self, rover, message_swarm_id, message_rover_id, move_by):
        rover.receive_message(message_swarm_id, message_rover_id, move_by)


class Manager(User):
    def move_rover(self, rover, message_swarm_id, message_rover_id, move_by):
        rover.receive_message(message_swarm_id, message_rover_id, move_by)

    def add_rover(self, rover):
        super().add_rover(rover)

    def remove_rover(self, rover):
        super().remove_rover(rover)
