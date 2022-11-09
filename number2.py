# Input a number. Reverse the number without using the reverse function. Note, truncate 0
# if the input ends in 0 and add 0 if one digit only.

num = input("Enter a number: ")


list_num = list(num)
reversed_list = list_num[::-1]
print("Reverse: ", end =''.join(reversed_list))


