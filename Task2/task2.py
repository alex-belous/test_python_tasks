from CircularBufferList import CircularBufferList
from CircularBufferLinkedArray import CircularBufferLinkedArray
import time

capacity = 10_000_000

listBuffer = CircularBufferList(capacity)
linkedBuffer = CircularBufferLinkedArray(capacity)


print(F"Время добавления ({capacity})")

start_time = time.time()
for i in range(capacity):
    listBuffer.push(i)
list_push_time = time.time() - start_time
print(f"\tБуфер на базе массива:\n\t{list_push_time} сек")


start_time = time.time()
for i in range(capacity):
    linkedBuffer.push(i)
linked_push_time = time.time() - start_time
print(f"\tБуфер на базе связанного списка:\n\t{linked_push_time} сек")


print(F"Время взятия ({capacity})")

start_time = time.time()
for _ in range(capacity):
    listBuffer.take()
list_take_time = time.time() - start_time
print(f"\tБуфер на базе массива:\n\t{list_take_time} сек")

start_time = time.time()
for _ in range(capacity):
    linkedBuffer.take()
linked_take_time = time.time() - start_time
print(f"\tБуфер на базе связанного списка:\n\t{linked_take_time} сек")