correct_answer = [1,2,5]

while True:
 num = input("Input num or input 'q' to quit.:")
 if num == "q":
     break
 
 try:
     num = int(num)
 except ValueError:
     print("Input num or q")
 if num in correct_answer:
     print("Your answer is correct.")
 else:
     print("Your answer is not correct.")