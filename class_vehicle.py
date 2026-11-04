class vehicle:
    def __init__(self,milage,speed):
        self.milage = milage
        self.speed = speed

vehicle1 = vehicle(20, 100)

print("The milage of the vehicle is: ", vehicle1.milage)
print("The speed of the vehicle is: ", vehicle1.speed)