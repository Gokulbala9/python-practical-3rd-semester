class CarParkingSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_full(self):
        return len(self.queue) >= self.capacity

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, car_number):
        if self.is_full():
            print(f"\n[Error] Parking full! Car {car_number} cannot enter.")
        else:
            self.queue.append(car_number)
            print(f"\n[Success] Car {car_number} entered the parking queue.")

    def dequeue(self):
        if self.is_empty():
            print("\n[Error] Parking empty! No cars to leave.")
        else:
            removed_car = self.queue.pop(0)
            print(f"\n[Success] Car {removed_car} left the parking queue.")

    def display(self):
        if self.is_empty():
            print("\n[Status] Parking lot is currently empty.")
        else:
            print("\n--- Current Parking Queue (Front to Rear) ---")
            for index, car in enumerate(self.queue, start=1):
                print(f"Position {index}: {car}")
            print(f"Total Spaces Occupied: {len(self.queue)}/{self.capacity}")


def main():
    print("=== Traffic Management: Car Parking System ===")
    
    while True:
        try:
            capacity = int(input("Enter maximum parking capacity: "))
            if capacity > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    parking_lot = CarParkingSystem(capacity)

    while True:
        print("\n==============================")
        print("         MAIN MENU            ")
        print("==============================")
        print("1. Enqueue (Car Entry)")
        print("2. Dequeue (Car Exit)")
        print("3. Display Parking Queue")
        print("4. Exit Program")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            car_num = input("Enter car license plate number: ").strip()
            if car_num:
                parking_lot.enqueue(car_num)
            else:
                print("Car number cannot be empty.")
                
        elif choice == '2':
            parking_lot.dequeue()
            
        elif choice == '3':
            parking_lot.display()
            
        elif choice == '4':
            print("\nExiting program. Thank you for using the Car Parking System!")
            break
            
        else:
            print("\nInvalid choice! Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
