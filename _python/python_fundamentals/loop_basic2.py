# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list1):
    for i in range(len(list1)):
        if list1[i] > 0:
            list1[i] = "big"
    return list1
print(biggie_size([-1,3,5,-5]))
# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(l1):
    count = 0
    for i in range(len(l1)):
        if l1[i] > 0:
            count += 1
    l1[len(l1)-1] = count
    return l1
print(count_positives([-1,1,1,1]))
# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(numl):
    sum = 0
    for i in range(len(numl)):
        sum += numl[i]
    return sum
print(sum_total([1,2,3,4])
# 4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(numl):
    sum = 0
    for i in range(len(numl)):
        sum += numl[i]
    ave = sum / len(numl)
    return ave
print(average([1,2,3,4]))
# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(num):
    return len(num)
print(length([37,2,1,-9]))
# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(num):
    if len(num) < 1:
        return "False"
    else:
        min_value = num[0]
        for i in range(len(num)):
            if num[i] < min_value:
                min_value = num[i]
    return min_value
    
print(minimum([37,2,1,-9]))         
# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(num):
    if len(num) < 1:
        return "False"
    else:
        max_value = num[0]
        for i in range(len(num)):
            if num[i] > max_value:
                max_value = num[i]
    return max_value
    
print(maximum([37,2,1,-9]))
# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(num):
    num_dict = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
        }
    if len(num) == 0:
        return num_dict
    else:
        num_dict['sum_total'] = 0
        num_dict['maximum'] = num[0]
        num_dict['minimum'] = num[0]
        for n in num:
            if n > num_dict['maximum']:
                num_dict['maximum'] = n
            elif n < num_dict['minimum']:
                num_dict['minimum'] = n
            num_dict['sum_total'] += n
            num_dict['length'] += 1
        num_dict['average'] = num_dict['sum_total'] / len(num)
        return num_dict
print(ultimate_analysis([37,2,1,-9]))
# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(num):
    half_len = int(len(num) /2);
    for i in range(half_len):
        num[i] , num[len(num) - 1 - i] = num[len(num) - 1 - i], num[i]
    return num

print(reverse_list([37,2,1,-9,5,8,7]))