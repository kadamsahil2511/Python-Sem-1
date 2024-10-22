#Ques_9
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        return total_fare + maintenance_charge

# Example usage
bus = Bus(100)
print(bus.fare())
