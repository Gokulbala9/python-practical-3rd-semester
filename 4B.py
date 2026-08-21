class Node:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None

class ParkingQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, car_number):
        new_node = Node(car_number)
        if self.rear is None:
            self.front = self.rear = new_node
            print("Car " + str(car_number) + " entered the parking lot.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print("Car " + str(car_number) + " entered the parking lot.")

    def dequeue(self):
        if self.front is None:
            print("Parking lot is empty! No cars to remove.")
            return None
        
        removed_car = self.front.car_number
        self.front = self.front.next

        if self.front is None:
            self.rear = None
            
        print("Car " + str(removed_car) + " left the parking lot.")
        return removed_car

    def display(self):
        if self.front is None:
            print("Parking status: Empty.")
            return

        print("Current Parking Queue (Front to Rear):")
        current = self.front
        cars = []
        while current:
            cars.append("[" + str(current.car_number) + "]")
            current = current.next
        print(" -> ".join(cars))


def main():
    parking_lot = ParkingQueue()

    while True:
        print("\n--- Traffic Management System ---")
        print("1. Enqueue (Car Entry)")
        print("2. Dequeue (Car Exit)")
        print("3. Display Parking Status")
        print("4. Exit Program")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            car_num = input("Enter car plate number/ID: ").strip()
            if car_num:
                parking_lot.enqueue(car_num)
            else:
                print("Invalid input! Car number cannot be empty.")
                
        elif choice == '2':
            parking_lot.dequeue()
            
        elif choice == '3':
            parking_lot.display()
            
        elif choice == '4':
            print("Exiting Traffic Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
