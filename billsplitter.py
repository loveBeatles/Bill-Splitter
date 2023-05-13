people_amount = int(input("Enter the number of friends joining (including you):\n"))
def party_calculator(peoples):
    party = {}
    if people_amount > 0:
        friend = str(input("Enter the name of every friend (including you), each on\n"))
        party[friend] = 0
        for i in range(people_amount - 1):
            friend = str(input())
            party[friend] = 0
        return party
    else:
        return "No one is joining for the party"
print(party_calculator(people_amount))
