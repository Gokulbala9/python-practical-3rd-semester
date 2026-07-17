class p:
    def __init__(self, song):
        self.song = song
        self.next = None
p1 = p("a")
p2 = p("b")
p3 = p("c")
p4 = p("d")
p5 = p("e")
p6 = p("f")
p7 = p("g")
p8 = p("h")
p9 = p("i")
p10 = p("j")
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8
p8.next = p9
p9.next = p10
head = p1
print("Original List:")
temp = head
while temp is not None:
    print(temp.song, end=" => ")
    temp = temp.next
print(None)
slow = head
fast = head
prev = None
while fast is not None and fast.next is not None:
    prev = slow
    slow = slow.next
    fast = fast.next.next
p11 = p("add")
if prev is not None:
    p11.next = prev.next
    prev.next = p11
print("\nList After Insertion:")
temp = head
while temp is not None:
    print(temp.song, end=" => ")
    temp = temp.next
print(None)
