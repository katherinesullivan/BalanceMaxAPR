# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high][2]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j][2] >= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

'''
# Driver code to test above
arr = [(10,2,3), (7,3,4), (8, 2, 5), (9, 1, 1)]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
	print(arr[i])
    '''

def apr_comparison(working_pools, other_pools):
    if working_pools[0][2] <= other_pools[0][2]:
        return False
    return True

def print_result(working_pools):
    for (pool_name, pool_size, pool_apr, pool_deposit) in working_pools:
        print("In %s deposit %d" % (pool_name, pool_deposit))
    return 0


def balance_max_apr_lending_strategies():
    cont = "yes"
    list_pools = []

    total_amount = float(input("Enter total amount to deposit: "))

    while(cont != "no"):
        pool_name = input("Enter pool name: ")
        pool_size = float(input("Enter pool size: "))
        pool_apr = float(input("Enter pool apr: "))
        pool_deposit = 0
        list_pools.append([pool_name, pool_size, pool_apr, pool_deposit])
        cont = input("Do you want to enter another pool? (yes/no): ")
    
    # we order our pools from highest apr to lowest apr
    number_pools = len(list_pools)
    quickSort(list_pools,0,number_pools-1)

    '''for element in list_pools:
        print(element)
        print(list_pools[0])'''

    # we start working with the pool of highest apr
    working_pools = []
    working_pools.append(list_pools[0])

    while (working_pools != list_pools):
        len_working_pools = len(working_pools)

        other_pools = list_pools[len_working_pools:]

        while(apr_comparison(working_pools, other_pools) and total_amount >= 1):
            total_size_working = 0
            for (pool_name, pool_size, pool_apr, pool_deposit) in working_pools:
                total_size_working+=pool_size

            i = 0
            while (i < len_working_pools):
                pool_size = working_pools[i][1]
                pool_apr = working_pools[i][2]

                # for every dollar we insert we do it proportionally in every working pool
                amount_inserted = pool_size/total_size_working

                # we actualize the pool data
                new_size = pool_size + amount_inserted
                change_index = new_size/pool_size
                new_apr = pool_apr/change_index

                working_pools[i][1] = new_size
                working_pools[i][2] = new_apr
                working_pools[i][3] += amount_inserted
                i+=1
            total_amount= total_amount - 1

        # if we stopped because we runned out of money, the program is over
        if (total_amount == 0):
            print_result(working_pools)
            return 0
        
        # if we stopped because the apr of the first element in other pools was reached, we
        # start working with that new pool
        working_pools = working_pools+[other_pools[0]]
        other_pools = other_pools[1:]

    # we are working with every pool there is so we deposit proportionally to mantain apr as equally high as possible
    total_size_working = 0
    len_working_pools = 0
    for (pool_name, pool_size, pool_apr, pool_deposit) in working_pools:
        total_size_working+=pool_size
        len_working_pools+=1
    
    i = 0
    while (i < len_working_pools):
        pool_size = working_pools[i][1]
        pool_apr = working_pools[i][2]

        amount_inserted = total_amount*(pool_size/total_size_working)

        new_size = pool_size + amount_inserted
        change_index = new_size/pool_size
        new_apr = pool_apr/change_index

        working_pools[i][1] = new_size
        working_pools[i][2] = new_apr
        working_pools[i][3] += amount_inserted
        i+=1

    print_result(working_pools)
    return 0


balance_max_apr_lending_strategies()