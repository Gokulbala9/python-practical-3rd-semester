class Node:

  def __init__(self, enrollment_id, student_name, course_name):
    self.enrollment_id = enrollment_id
    self.student_name = student_name
    self.course_name = course_name
    self.height = 1
    self.left = None
    self.right = None


class AVLTree:

  def get_height(self, root):
    if not root:
      return 0
    return root.height

  def get_balance(self, root):
    if not root:
      return 0
    return self.get_height(root.left) - self.get_height(root.right)

  def right_rotate(self, y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
    x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
    return x

  def left_rotate(self, x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
    y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
    return y

  def insert(self, root, enrollment_id, student_name, course_name):
    if not root:
      return Node(enrollment_id, student_name, course_name)
    if enrollment_id < root.enrollment_id:
      root.left = self.insert(
          root.left, enrollment_id, student_name, course_name
      )
    elif enrollment_id > root.enrollment_id:
      root.right = self.insert(
          root.right, enrollment_id, student_name, course_name
      )
    else:
      return root

    root.height = (
        max(self.get_height(root.left), self.get_height(root.right)) + 1
    )
    balance = self.get_balance(root)

    if balance > 1 and enrollment_id < root.left.enrollment_id:
      return self.right_rotate(root)
    if balance < -1 and enrollment_id > root.right.enrollment_id:
      return self.left_rotate(root)
    if balance > 1 and enrollment_id > root.left.enrollment_id:
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)
    if balance < -1 and enrollment_id < root.right.enrollment_id:
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)

    return root

  def min_value_node(self, root):
    current = root
    while current.left is not None:
      current = current.left
    return current

  def delete(self, root, enrollment_id):
    if not root:
      return root
    if enrollment_id < root.enrollment_id:
      root.left = self.delete(root.left, enrollment_id)
    elif enrollment_id > root.enrollment_id:
      root.right = self.delete(root.right, enrollment_id)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return temp
      temp = self.min_value_node(root.right)
      root.enrollment_id = temp.enrollment_id
      root.student_name = temp.student_name
      root.course_name = temp.course_name
      root.right = self.delete(root.right, temp.enrollment_id)

    if not root:
      return root

    root.height = (
        max(self.get_height(root.left), self.get_height(root.right)) + 1
    )
    balance = self.get_balance(root)

    if balance > 1 and self.get_balance(root.left) >= 0:
      return self.right_rotate(root)
    if balance > 1 and self.get_balance(root.left) < 0:
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)
    if balance < -1 and self.get_balance(root.right) <= 0:
      return self.left_rotate(root)
    if balance < -1 and self.get_balance(root.right) > 0:
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)

    return root

  def search(self, root, enrollment_id):
    if not root or root.enrollment_id == enrollment_id:
      return root
    if root.enrollment_id < enrollment_id:
      return self.search(root.right, enrollment_id)
    return self.search(root.left, enrollment_id)

  def inorder(self, root):
    res = []
    if root:
      res = self.inorder(root.left)
      res.append((root.enrollment_id, root.student_name, root.course_name))
      res = res + self.inorder(root.right)
    return res

  def count(self, root):
    if not root:
      return 0
    return 1 + self.count(root.left) + self.count(root.right)


if __name__ == "__main__":
  avl = AVLTree()
  root = None
  while True:
    print("\n1. Insert Enrollment Record")
    print("2. Delete Enrollment Record")
    print("3. Search Enrollment Record")
    print("4. Display All Enrollment Records")
    print("5. Count Total Enrollments")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      eid = int(input("Enter Enrollment ID: "))
      name = input("Enter Student Name: ")
      course = input("Enter Course Name: ")
      root = avl.insert(root, eid, name, course)
      print("Enrollment record added successfully.")
    elif choice == "2":
      eid = int(input("Enter Enrollment ID to delete: "))
      root = avl.delete(root, eid)
      print("Enrollment record deleted if it existed.")
    elif choice == "3":
      eid = int(input("Enter Enrollment ID to search: "))
      res = avl.search(root, eid)
      if res:
        print(
            f"Found Record -> ID: {res.enrollment_id}, Name:"
            f" {res.student_name}, Course: {res.course_name}"
        )
      else:
        print("Enrollment record not found.")
    elif choice == "4":
      records = avl.inorder(root)
      if not records:
        print("No enrollment records found.")
      else:
        print("All Enrollment Records:")
        for r in records:
          print(
              f"Enrollment ID: {r[0]} | Student Name: {r[1]} | Course Name:"
              f" {r[2]}"
          )
    elif choice == "5":
      print(f"Total Enrollments: {avl.count(root)}")
    elif choice == "6":
      print("Exiting program.")
      break
    else:
      print("Invalid choice. Please try again.")
