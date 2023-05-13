from random import choice
friends_amount = int(input("Enter the number of friends joining (including you):\n"))
print()
party = {}

def inputting(n):
    1 / friends_amount
    name = []
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(n):
        name.append(input())
    print()
    return name
def bill_splitter(friends_list, dict, amount):
    bill_value = int(input("Enter the total bill value:\n"))
    print()
    select = input('Do you watn to use the "Who is lucky?" feature? Write Yes/No:\n')
    print()
    if select == 'Yes':
        dict = {key: round(bill_value / (amount - 1), 2) for key in friends_list}
        lucky = choice(friends_list)
        dict[lucky] = 0
        print(f"{lucky} is the lucky one!\n")
    else:
        print("No one is going to be lucky\n")
        dict = {key: round(bill_value / amount, 2) for key in friends_list}
    return dict

if friends_amount > 0:
    print(bill_splitter(inputting(friends_amount), party, friends_amount))
else:
    print("No one is joining for the party")