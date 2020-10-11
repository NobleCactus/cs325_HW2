#Andrew Eppinger
#CS 325 Fall 2020
#Homework 2 Problem #5


output = ''                         #Var to store the sorted lines at to be output to insert.out
content_list = []                   #Var to store the each line of the data.text file
numbers_to_be_sorted = []           #Var to store the numbers from each line after they're converted to ints
text_file = open('data.txt', 'r')

for line in text_file:              #Iterates through each line of the text file, storing each line in a list
    line = line.split(' ')
    content_list.append(line)

for line in content_list:           #Iterates through the list of lines, converts each number from a str to an int
    for i in range(len(line)):
        line[i] = int(line[i])
    numbers_to_be_sorted.append(line[1:])   #Gets rid of the first number in each list, as that is just an indicator
                                            #of the number of numbers to be sorted.

def stoogeSort(arr,floor=0,ceiling=None):
    '''
    This is a function called stoogeSort. It is a notably inefficient sorting algorithm that takes
    an unsorted array as input and returns a sorted one.
    '''
    if ceiling == None:             #The first time stoogeSort is run, the ceiling has to be quantified. It is set
        ceiling = len(arr) - 1      #to be the length of the list - 1 to avoid index out of range errors.

    if arr[floor] > arr[ceiling]:   #This checks if the first and last elements are out of order.
        temp = arr[floor]           #If they are, a temporary variable is used as a place-holder in order to facilitate
        arr[floor] = arr[ceiling]   #the swap.
        arr[ceiling] = temp

    if ceiling - floor + 1 > 2:                     #If the array is still larger than size 2, it is divided by 3 again
        third = (ceiling - floor + 1) // 3
        stoogeSort(arr, floor, (ceiling - third))    #Calls stoogeSort on the first 2/3 of the array
        stoogeSort(arr, floor + third,ceiling)       #Calls stoogeSort on the second 2/3 of the array
        stoogeSort(arr, floor, (ceiling - third))    #Calls stoogeSort on the first 2/3 of the array

    return arr  #Returns the sorted list


for line in numbers_to_be_sorted:           #Calls insertionSort on each line
    stoogeSort(line)

for line in numbers_to_be_sorted:           #outputs the now-sorted numbers to a new text file
    for num in line:
        num = str(num)
        output = output + num + ' '
    output = output + '\n'

stooge_out = open('stooge.out','w')
stooge_out.write(output)
stooge_out.close()
text_file.close()

