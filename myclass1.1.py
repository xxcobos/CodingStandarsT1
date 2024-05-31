class VacationDestination:
    def __init__(self):
        self.popular_destinations = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, destination):
        return self.popular_destinations.get(destination, 0)
    
    def is_valid_destination(self, destination):
        return isinstance(destination, str)

class Passenger:
    def __init__(self, number_of_passengers):
        self.number_of_passengers = number_of_passengers
    
    def is_valid_number(self):
        return isinstance(self.number_of_passengers, int) and 0 < self.number_of_passengers <= 80

    def get_discount(self):
        if 4 < self.number_of_passengers < 10:
            return 0.1
        elif self.number_of_passengers >= 10:
            return 0.2
        else:
            return 0.0

class VacationDuration:
    def __init__(self, duration_in_days):
        self.duration_in_days = duration_in_days

    def is_valid_duration(self):
        return isinstance(self.duration_in_days, int) and self.duration_in_days > 0

    def get_penalty_fee(self):
        return 200 if self.duration_in_days < 7 else 0

    def get_promotion(self):
        if self.duration_in_days > 30 or self.duration_in_days == 2:
            return 200
        return 0

class VacationPackage:
    base_cost = 1000

    def __init__(self, destination, number_of_passengers, duration_in_days):
        self.vacation_destination = VacationDestination()
        self.passenger = Passenger(number_of_passengers)
        self.vacation_duration = VacationDuration(duration_in_days)
        self.destination = destination

    def calculate_total_cost(self):
        if not self.vacation_destination.is_valid_destination(self.destination) or not self.passenger.is_valid_number() or not self.vacation_duration.is_valid_duration():
            return -1
        
        total_cost = self.base_cost
        total_cost += self.vacation_destination.get_extra_cost(self.destination)

        total_cost += self.vacation_duration.get_penalty_fee()
        total_cost -= self.vacation_duration.get_promotion()

        discount = self.passenger.get_discount()
        total_cost -= total_cost * discount
        
        return max(int(total_cost), 0)

def main():
    destination = 'Paris'
    number_of_passengers = 5
    duration_in_days = 10

    vacation_calculator = VacationPackage(destination, number_of_passengers, duration_in_days)
    total_cost = vacation_calculator.calculate_total_cost()

    if total_cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${total_cost}")

if __name__ == "__main__":
    main()
