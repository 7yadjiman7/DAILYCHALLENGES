# Exercice 1: Birthday Look-up

birthdays = {"dodo":"1999/11/27",
             "pheno":"2002/04/19",
             "pato":"1993/05/20",
             "navigue":"1990/09/17",
             "Lavieille": "1986/03/07"}

name_user = input("Give me a person's name in this list: ")

resultat = birthdays.get(name_user)

if resultat:
        print(name_user," birthdays is ",resultat )
else:
    print("Name not exist on our dictionary")


# Exercice 2: Birthdays Advanced

print("You can look up the birthdays of the people in the list!\n",birthdays.keys())

if name_user in birthdays.keys():
      print(name_user," is in our dictionary")
else:
      print(name_user," isn't in our dictionary")


# Exercice 3: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("please enter one name: ")

for i in range(len(names)):
    if name == names[i]:
        print(name," indice is ",i)
        break
else:
     print("Name not in list!")


# Exercice 4: Double Dice

import random
def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    throws = 0
    while True:
        throws += 1
        first_die = throw_dice()
        second_die = throw_dice()
        if first_die == second_die:
            return throws


def main():
    results = []
    for _ in range(100):
        results.append(throw_until_doubles())

    total_throws = sum(results)
    average_throws = total_throws / len(results)

    print(f"It took {total_throws} throws in total to reach 100 doubles.")
    print(
        f"The average number of throws to reach doubles was {average_throws:.2f}.")


if __name__ == "__main__":
    main()
