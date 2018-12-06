'''
Name:Jorge Quinoenz
#Professor: Diego Aguirre
#Assignment Lab#5
#Purpose of Assignment: The purpose of this assignment is to implement a min heap
'''


class Heap:

    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)
        self.percolate_up()

    def extract_min(self):  # Extracting the smallest number from the heap array
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            self.percolate_down(0)
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0

    def percolate_up(self):
        node_index = len(self.heap_array) - 1
        if node_index == 0:
            return
        while node_index > 0:
            parent_index = (node_index-1)//2  # Compute the parent node's index
            if self.heap_array[node_index] < self.heap_array[parent_index]:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                node_index = parent_index

            else:  # No violation, percolate up is finished
                break

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]
        while child_index < len(self.heap_array):
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i+child_index]
                    min_index = i + child_index
                i = i + 1

            if min_value == value:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp

                node_index = min_index
                child_index = 2 * node_index + 1

    def heap_sort(self):  # This function receives a min-heap and returns a sorted array
        result = []
        while not self.is_empty():
            result.append(self.extract_min())
        return result

    def print_heap(self):  # Function to print min-heap
        for i in range(len(self.heap_array)):
            print(self.heap_array[i])


def main():
    my_min_heap = Heap()
    file_name = input("Enter the name of the file whose numbers you want to place in the heap:\n")
    file = open(file_name, "r")
    for line in file:
        curr = line.split(",")
        for number in curr:
            my_min_heap.insert(int(number))
    print("Unsorted:")
    my_min_heap.print_heap()
    sorted_min_heap = my_min_heap.heap_sort()
    print(sorted_min_heap)

main()