from random import randint
friends_amount = int(input("Enter the number of friends joining (including you):\n"))
lucky_list = []
try:
    if friends_amount > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(friends_amount):
            name = input()
            lucky_list.append(name)
        bill_value = int(input("Enter the total bill value:\n"))
        choice = input('Do you want to use the "Who the lucky?" feature? Write Yes/No:\n')
        if choice == 'Yes':
            print(f"{lucky_list[randint(0, len(lucky_list))]} is the lucky one!")
        else:
            print("No one is going to be lucky")
    else:
        print("No one is joining for the party")
except:
    print("No one is joining for the party")

