class Slot:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

    def move_left(self):
        if not self.left:
            slot = Slot()
            self.left = slot
            slot.right = self
            return slot
        else:
            return self.left

    def move_right(self):
        if not self.right:
            slot = Slot()
            self.right = slot
            slot.left = self
            return slot
        else:
            return self.right

    def __repr__(self):
        return f"[{self.value}]"

    def checksum(self):
        s = self.value
        current = self.left
        while current:
            s += current.value
            current = current.left
        current = self.right
        while current:
            s += current.value
            current = current.right
        return s


state = "A"
cursor = Slot()
for _ in range(12861455):
    if state == "A":
        if cursor.value == 0:
            cursor.value = 1
            cursor = cursor.move_right()
            state = "B"
        elif cursor.value == 1:
            cursor.value = 0
            cursor = cursor.move_left()
            state = "B"
    elif state == "B":
        if cursor.value == 0:
            cursor.value = 1
            cursor = cursor.move_left()
            state = "C"
        elif cursor.value == 1:
            cursor.value = 0
            cursor = cursor.move_right()
            state = "E"
    elif state == "C":
        if cursor.value == 0:
            cursor.value = 1
            cursor = cursor.move_right()
            state = "E"
        elif cursor.value == 1:
            cursor.value = 0
            cursor = cursor.move_left()
            state = "D"
    elif state == "D":
        if cursor.value == 0:
            cursor.value = 1
            cursor = cursor.move_left()
            state = "A"
        elif cursor.value == 1:
            cursor.value = 1
            cursor = cursor.move_left()
            state = "A"
    elif state == "E":
        if cursor.value == 0:
            cursor.value = 0
            cursor = cursor.move_right()
            state = "A"
        elif cursor.value == 1:
            cursor.value = 0
            cursor = cursor.move_right()
            state = "F"
    elif state == "F":
        if cursor.value == 0:
            cursor.value = 1
            cursor = cursor.move_right()
            state = "E"
        elif cursor.value == 1:
            cursor.value = 1
            cursor = cursor.move_right()
            state = "A"

print(cursor.checksum())

