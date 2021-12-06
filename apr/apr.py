def user_input():
    total_amount = float(input("Enter total amount to deposit: "))

    cont = "yes"
    list_pools = []

    while(cont != "no"):
        pool_name = input("Enter pool name: ")
        pool_size = float(input("Enter pool size: "))
        pool_apr = float(input("Enter pool apr: "))
        pool_deposit = 0
        list_pools.append([pool_name, pool_size, pool_apr, pool_deposit])
        cont = input("Do you want to enter another pool? (yes/no): ")

    return list_pools, total_amount

# Quicksort function based on the implementation proposed on 
# https://www.geeksforgeeks.org/python-program-for-quicksort/

def partition(arr, low, high):
	i = (low-1)		     # index of smaller element
	pivot = arr[high][2] # pivot

	for j in range(low, high):
		# If current element is greater than or equal to pivot
		if arr[j][2] >= pivot:
			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		# pi is partitioning index, arr[p] is now at right place
		pi = partition(arr, low, high)

		# Separately sort elements before partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


def apr_comparison(working_pools, other_pools):
    if working_pools[0][2] <= other_pools[0][2]:
        return False
    return True

def print_result(working_pools):
    print("")
    for [pool_name, pool_size, pool_apr, pool_deposit] in working_pools:
        print("In %s deposit %lf. New size: %f. New apr: %f" % (pool_name, pool_deposit, pool_size, pool_apr))
    return 0

def update_pools(working_pools, len_working_pools, total_size_working, deposit_amount):
    i = 0
    while (i < len_working_pools):
        pool_size = working_pools[i][1]
        pool_apr = working_pools[i][2]

        amount_inserted = deposit_amount*(pool_size/total_size_working)

        new_size = pool_size + amount_inserted
        change_index = new_size/pool_size
        new_apr = pool_apr/change_index

        working_pools[i][1] = new_size
        working_pools[i][2] = new_apr
        working_pools[i][3] += amount_inserted
        i+=1

def balance_max_apr_lending_strategies():
    list_pools, total_amount = user_input()
    
    # we order our pools from highest to lowest apr
    number_pools = len(list_pools)
    quickSort(list_pools,0,number_pools-1)

    # we start working with the pool of highest apr
    working_pools = [list_pools[0]]

    while (working_pools != list_pools):
        len_working_pools = len(working_pools)

        other_pools = list_pools[len_working_pools:]

        while(apr_comparison(working_pools, other_pools) and total_amount >= 1):
            total_size_working = 0
            for [_, pool_size, _, _] in working_pools:
                total_size_working+=pool_size

            # for every dollar we insert we do it proportionally in every working pool
            update_pools(working_pools, len_working_pools, total_size_working, 1)
            total_amount= total_amount - 1

        # if we stopped because we runned out of money, the program is over
        if (total_amount == 0):
            print_result(working_pools)
            return 0

        # if we stopped because we had less than a dollar, we distribute the
        # amount of money left propotionally between the working pools
        if (total_amount < 1):
            update_pools(working_pools, len_working_pools, total_size_working, total_amount)
            print_result(working_pools)
            return 0

        # if we stopped because the apr of the first element in other pools was reached, we
        # start working with that new pool
        working_pools = working_pools+[other_pools[0]]
        other_pools = other_pools[1:]

    # we are working with every pool there is so we deposit proportionally 
    # to mantain apr as equally high as possible
    total_size_working = 0
    len_working_pools = 0
    for [_, pool_size, _, _] in working_pools:
        total_size_working+=pool_size
        len_working_pools+=1
    
    update_pools(working_pools, len_working_pools, total_size_working, total_amount)

    print_result(working_pools)
    return 0

if __name__ == '__main__':
    balance_max_apr_lending_strategies()