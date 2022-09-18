def bubble_sort(list):
    unsorted_until_index = len(list) -1 #keep track of up to which index is still unsorted (initially the final index in the array)
    sorted = False #keep track of whether the array is fully sorted.

    while not sorted: 
        sorted = True #we'll change this back to False as soon as we have to make any swaps. if we get through an entire passthrough without having to make any swaps, we'll know that the array is completely sorted.
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False #if we need to make a swap, i.e. if the two elements are not sorted.
                list[i], list[i+1] = list[i+1], list[i] #now we've completed another passthrough, and can safely assume that the value we've bbbled up to the right is now in its corect position.
        unsorted_until_index = unsorted_until_index -1 #decrement the index by 1 since the index it was already pointing to is now sorted.

    #each round of while loop represents a passthrough and we run it until we know that our array is fully sorted.

list = []
n = int(input("Enter number of elements: "))

for i in range(0, n): #this will run as many times as the number of elements provided by the user
    print("Now enter a number for the list and press enter after each number")
    ele = int(input())

    list.append(ele)

# input("Type in the list of numbers separated by a comma: ")
bubble_sort(list)
print(list)
