import random

def main():
    try:
        num = int(input("Enter the number of elements in the array: "))
        if num <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            array = generate_random_list(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('Input array: ', array)
    num_of_elements = len(array)
    max_index = num_of_elements-1
    for index in range(0,max_index):
        if isEvenArray(array):
            if index == ((num_of_elements)//2):break
        else:
            if index == (num_of_elements-1)//2: break
        temp = array[index]
        array[index] = array[max_index-index]
        array[max_index-index] = temp
    print('Output array: ', array)

def generate_random_list(num):
    random_list = [random.randint(1, 100) for _ in range(num)]
    return random_list

def isEvenArray(array):
    num_of_elements = len(array)
    if num_of_elements%2==0:
        return True
    else:
        return False

if __name__== "__main__":
    main()