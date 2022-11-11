# Input a number. Reverse the number without using the reverse function. Note, truncate 0
# if the input ends in 0 and add 0 if one digit only.

num = input("Enter a number: ")


list_num = list(num)
reversed_list = list_num

if list_num[-1] == '0':
    new_list = reversed_list[:-1]
    reversed_list = new_list
    print("Reverse: ", end=''.join(reversed_list[::-1]))

elif '-' in list_num:
    if list_num[-1] == '0':
        remove_zero = reversed_list[:-1]
        retain_sign = remove_zero.insert(0,'-')
        print("Reverse: ", end=''.join(retain_sign))
    else:
        remove = list_num[1:]
        new_list = remove[::-1]
        new_list.insert(0, "-")
        print("Reverse: ", end=''.join(new_list))

elif len(reversed_list) == 1:
    reversed_list.append('0')
    print("Reverse: ", end=''.join(reversed_list))
else:
    reversed_list = list_num[::-1]
    print("Reverse: ", end=''.join(reversed_list))




