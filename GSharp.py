def menu():
    print("Welcome to GSharp! What would you like to do?")
    user = input("1. Shell")
    if user == "1":
        gsharpshell()
    else:
        menu()
def gsharpshell():
    print("Type cmds for the cmd list.")
    run = input("GSharp>")
    if run == "cmds":
        print("CMD LIST: cmds, verison, add, exit")
        gsharpshell()
    if run == "verison":
        print("GSharp 1.0, made by the GSharp dev.")
        gsharpshell()
    if run == "add":
        number1 = int(input(" Number to add to?"))
        number2 = int(input(" Number to add?"))
        print(str(number1) + "plus" + str(number2) + "equals" + number1+number2)
        gsharpshell()
    if run == "exit":
        menu()
    
    gsharpshell()
menu()
