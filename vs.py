def sum_of_list(my_list):
    
    sum=0

    for number in my_list:
        sum+=number

    return sum

print(sum_of_list([10 ,20, 50, 10, 40]) == 130)