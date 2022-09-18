def bubble_sort(list):
    unsorted_until_index = len(list) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        unsorted_until_index = unsorted_until_index -1

list = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input())

    list.append(ele)

# input("Type in the list of numbers separated by a comma: ")
bubble_sort(list)
print(l)