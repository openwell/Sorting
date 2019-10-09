# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    
    # loop through n-1 elements
    for i in range(0, len(arr)):
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i+1, len(arr)):
            if arr[x] < arr[i]:
                mix = arr[x]
                arr[x] = arr[i]
                arr[i] = mix 
        # TO-DO: swap

    return arr
#  it two time loop.
#  the first is the base while the other is forward
#  so at all time the first loop is loop for min then jumps to the next index
#  to get an understanding print print(i, x)
# print(selection_sort([7, 5, 4, 1, 2]))
# TO-DO:  implement the Bubble Sort function below

# def bubble_sort( arr ):
#     for i in range(0, len(arr)):
#         for x in range(i+1, len(arr)):
#             current = i
#             if arr[current] > arr[x]:
#                 a = arr[x]
#                 arr[x] = arr[current]
#                 arr[current] = a
#                 current = x
#     return arr
def bubble_sort( arr ):
    lastSorted = len(arr) - 1 
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(0, lastSorted):
            if arr[i] > arr[i+1]:
                a = arr[i]
                b = arr[i+1]
                arr[i] = b
                arr[i+1] = a
                isSorted = False
        --lastSorted
    return arr
print(bubble_sort([7, 5, 4, 1, 2]))
# for bubble you are working with the highest and trying to push it to the right end
# you also have to keep the state if the current you swap it
# then it change when the upper iteration changes  

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr

