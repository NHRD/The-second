name = input("Input a word: ")
serch = input("Input a character to serch: ")
start_point = int(input("Input start point: "))
end_point = start_point + len(name)
try:
    first_index = name.index(serch,start_point,end_point)
    result = "The position of first index is {}.".format(first_index)
    print(result)
   
except ValueError:
    print("String not found")
