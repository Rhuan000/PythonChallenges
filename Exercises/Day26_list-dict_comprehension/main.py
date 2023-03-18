with open('file1.txt') as file1:
    int_file1 = [int(number) for number in file1.readlines()]

with open('file2.txt') as file2:
    int_file2 = [int(number) for number in file2.readlines()]

commum_list = [number for number in int_file1 if number in int_file2]
print(commum_list)