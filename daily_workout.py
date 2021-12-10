import time, subprocess


class Tabata:
    """A simple attempt to create add free tabata timer."""

    def __init__(self):
        self.training_time = int
        self.rest_time = int

    def workout_time(self):
        """Timer for workout with the sound of gun on the beginning and
        boat horne when the rest time starts."""
        self.training_time = 20
        subprocess.Popen(["start", "gun_shot.MP3"], shell=True)
        while self.training_time > 0:
            print(self.training_time, end="\n")
            time.sleep(1)
            self.training_time -= 1
        subprocess.Popen(["start", "Boat-horn-sound-effect.MP3"], shell=True)

    def cooling_time(self):
        """Timer for rest period"""
        self.rest_time = 10
        while self.rest_time > 0:
            print(self.rest_time, end="\n")
            time.sleep(1)
            self.rest_time -= 1