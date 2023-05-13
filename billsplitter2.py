people_amount = int(input("Enter the number of friends joining (including you):\n"))
party = {}
def bill_splitter(amount, dict):
    if amount > 0:
        print("Enter the name of every friend (including you), each on a new line:\n")
        for i in range(amount):
            dict[input()] = None
        bill_value = int(input("Enter the total bill value:\n"))
        for j in range(amount):
            for key1 in dict:
                dict[key1] = round(bill_value / amount, 2)
        return dict
    else:
        return "No one is joining for the party"
print(bill_splitter(people_amount, party))