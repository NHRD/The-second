answer = input("What is your name?:")

with open("answer.txt","w") as docu:
    docu.write(answer)