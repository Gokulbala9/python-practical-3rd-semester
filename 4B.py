class CarNode:
   
    def __init__(self, plate_number, car_details):
        self.plate_number = plate_number
        self.car_details = car_details
        self.next = None

class ParkingQueue:
  
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, plate_number, car_details):
       
        new_car = CarNode(plate_number, car_details)
        
        if self.rear is None:
            self.front = self.rear = new_car
        else:
            self.rear.next = new_car
            self.rear = new_car
            
        self.count += 1
        print(f"\n[ENTRY] Car '{plate_number}' successfully added to the queue.")

    def dequeue(self):
      
        if self.is_empty():
            print("\n[EMPTY] No cars in the queue to remove.")
            return None

        removed_car = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        print(f"\n[EXIT] Car '{removed_car.plate_number}' ({removed_car.car_details}) has exited.")
        return removed_car

    def display_queue(self):
        """Display all cars currently waiting in the queue."""
        if self.is_empty():
            print("\n[STATUS] Parking queue is currently empty.")
            return

        print(f"\n--- Current Parking Queue ({self.count} Cars Waiting) ---")
        current = self.front
        position = 1
        while current:
            print(f"Position {position}: Plate: {current.plate_number} | Details: {current.car_details}")
            current = current.next
            position += 1
        print("-" * 40)

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None


def main():
    parking_lot = ParkingQueue()

    while True:
        print("\n=== CAR PARKING MANAGEMENT SYSTEM ===")
        print("1. Car Arrival (Enqueue)")
        print("2. Car Departure (Dequeue)")
        print("3. View Parking Queue")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            print("\n--- Enter Car Details ---")
            plate = input("Enter License Plate Number: ").strip().upper()
            if not plate:
                print("Plate number cannot be empty!")
                continue
            details = input("Enter Car Model & Color (e.g., Red Toyota): ").strip()
            parking_lot.enqueue(plate, details)

        elif choice == '2':
            parking_lot.dequeue()

        elif choice == '3':
            parking_lot.display_queue()

        elif choice == '4':
            print("\nExiting system. Have a great day!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
