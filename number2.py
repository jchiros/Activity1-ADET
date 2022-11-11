# Input a number. Reverse the number without using the reverse function. Note, truncate 0
# if the input ends in 0 and add 0 if one digit only.

num = input("Enter a number: ")


list_num = list(num)
reversed_list = list_num

if list_num[-1] == '0':
    if '-' in list_num:
        remove_zero = reversed_list[:-1]
        new_list = remove_zero[1:]
        reversed_list = new_list
        print("Reverse: -", end=''.join(reversed_list[::-1]))
    else:
        new_list = reversed_list[:-1]
        reversed_list = new_list
        print("Reverse: ", end=''.join(reversed_list[::-1]))

elif '.' in list_num:
    if list_num[0] == '0':
        remove_zero = reversed_list[1:]
        new_list = remove_zero[::-1]
        remove_dot = new_list[:-1]
        remove_dot.insert(1, '.')
        print("Reverse: ", end=''.join(remove_dot))

elif len(reversed_list) == 1:
    reversed_list.append('0')
    print("Reverse: ", end=''.join(reversed_list))
else:
    reversed_list = list_num[::-1]
    print("Reverse: ", end=''.join(reversed_list))
