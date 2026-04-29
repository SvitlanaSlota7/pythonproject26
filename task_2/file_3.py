class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Створюємо список списків для зберігання пар ключ, значення
        self.table = [[] for _ in range(self.size)]
        self._count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self._count += 1

    def __len__(self):
        return self._count

    def __contains__(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

my_table = HashTable()
my_table.insert("apple", 5)
my_table.insert("banana", 10)
my_table.insert("orange", 15)

print(f"Кількість елементів (len): {len(my_table)}")

print(f"Чи є 'apple' у таблиці? {'apple' in my_table}")   # Виведе: True
print(f"Чи є 'grape' у таблиці? {'grape' in my_table}")   # Виведе: False