#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return (number**2)**0.5


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    li = []
    for c in prefixes:
        li.append(c+suffixe)
    return li


def prime_integer_summation() -> int:
    sum = 2
    nb = 1
    current = 3
    while(nb < 100):
        if prime(current):
            sum += current
            nb += 1
        current += 2
    return sum

def prime(n):
    if(n < 2):
        return False
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    return True

def factorial(number: int) -> int:
    if(number == 0):
        return 1
    return number*factorial(number-1)


def use_continue() -> None:
    for i in range(1, 11):
        if(i == 5):
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return [testgroup(group) for group in groups]
        

def testgroup(ages):
    if len(ages) > 10 or len(ages) < 3:
            return False
    if 25 in ages:
        return True
    
    over70 = False
    for age in ages:
        if (age < 18):
            return False
        over70 = over70 or age > 70
    if 50 in ages and over70:
        return False


        


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
