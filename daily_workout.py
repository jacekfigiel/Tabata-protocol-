import time, subprocess

workout_time = 20
rest_time = 10
exercise_circuit = 40

while workout_time > 0:
    print(workout_time, end="\n")
    time.sleep(1)
    workout_time -= 1

subprocess.Popen(["start", "Boat-horn-sound-effect.MP3"], shell=True)
