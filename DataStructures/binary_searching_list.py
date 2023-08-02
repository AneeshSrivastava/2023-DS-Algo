import random
from time import perf_counter

def generate_random_list(num):
    random_list = [random.randint(1, 100) for _ in range(num)]
    random_list.sort()
    return random_list

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def find_element(lst, target):
    for element in lst:
        if element == target:
            return True
    return False

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of elements in the list: "))
        if num <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            random_list = generate_random_list(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        bs_t1 = perf_counter()
        print(binary_search(random_list, 55))
        bs_t2 = perf_counter()
        print(find_element(random_list, 55))
        fe_t2 = perf_counter()
        print('bs_t1: ', bs_t1)
        print('bs_t2: ', bs_t2)
        print('fe_t2: ', fe_t2)
        total_time_bs = round(bs_t2 - bs_t1, 3)
        total_time_fe = round(fe_t2 - bs_t2, 3)
        print("")
        print("BS time ", total_time_bs, "seconds")
        print("NS time ", total_time_fe, "seconds")

