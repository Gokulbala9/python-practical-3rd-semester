class Job:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class MaxHeapJobScheduler:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def insert_job(self, name, priority):
        new_job = Job(name, priority)
        self.heap.append(new_job)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index].priority > self.heap[self._parent(index)].priority:
            parent_idx = self._parent(index)
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_job = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_job

    def _heapify_down(self, index):
        max_index = index
        left = self._left_child(index)
        right = self._right_child(index)
        if left < len(self.heap) and self.heap[left].priority > self.heap[max_index].priority:
            max_index = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[max_index].priority:
            max_index = right
        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self._heapify_down(max_index)

    def peek_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def display_heap(self):
        return self.heap


if __name__ == "__main__":
    scheduler = MaxHeapJobScheduler()
    while True:
        print("\n1. Insert Job\n2. Delete Highest Priority Job\n3. Peek Highest Priority Job\n4. Display All Jobs\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter job name: ")
            priority = int(input("Enter job priority: "))
            scheduler.insert_job(name, priority)
        elif choice == "2":
            job = scheduler.extract_max()
            if job:
                print(f"Processed: {job.name} (Priority: {job.priority})")
            else:
                print("Queue is empty")
        elif choice == "3":
            job = scheduler.peek_max()
            if job:
                print(f"Highest Priority: {job.name} (Priority: {job.priority})")
            else:
                print("Queue is empty")
        elif choice == "4":
            jobs = scheduler.display_heap()
            if jobs:
                for idx, job in enumerate(jobs):
                    print(f"[{idx}] {job.name}: {job.priority}")
            else:
                print("Queue is empty")
        elif choice == "5":
            break
        else:
            print("Invalid choice")
