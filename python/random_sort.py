"""
Take an unsorted list of ints and sort it in the most inefficient way possible.
"""

import random


def return_int(n):
    return n


def random_swap(a, b):
    c = return_int(a)
    a = return_int(b)
    b = return_int(c)
    return a, b


if __name__ == '__main__':

    listToSort = [9, 10, 314, 0, 0, 1, 5, 99, 69, 420, 1, 2, 3, 4]
    # listToSort = [99, 1, 3, 80]



    isSorted = False
    attempt = 1

    # Do the sort thing
    while not isSorted:
        print('----------------------------------------------------------------------------------------------------------')
        print(f'Attempt Number {attempt:,d}')
        print('----------------------------------------------------------------------------------------------------------')

        size = 0  # A dumb variable

        # I forgot what this does
        for blah in listToSort:
            size = size + 1
            # print(f'The count is {size} uh uh uh...')
        theIi = 0

        # Do some magic and wee wee wee the numbers around
        while theIi < size - 1:
            foo = -1
            while True:
                foo = random.randint(0, size - 1)
                if foo != theIi:
                    break
                # print(f'My Foo: {foo}')
            # print(f'foo {foo} i {theIi}')
            a = listToSort[theIi]
            b = listToSort[foo]
            # print(f'a, b before swap: {a}, {b}')
            a, b = random_swap(a, b)
            # print(f'a, b after swap: {a}, {b}')

            listToSort[theIi] = a
            listToSort[foo] = b
            theIi += 1

        anotherDamnList = []
        anotheri = 0
        for foofoocachoo in listToSort:
            anotherDamnList.append(foofoocachoo)
            anotehri = anotheri + 1

        anotherDamnList.sort()

        yetAnotheri = 0
        isTheTHingsGood = True

        if anotherDamnList != listToSort:
            isTheTHingsGood = False

        if not isTheTHingsGood:
            print(f'{listToSort}\nWRONG! HAVE ANOTHER BEER AND TRY AGAIN!')
        else:
            print(f'{listToSort}\nTECHNICALLY CORRECT! DONE! Have ANOTHER BEER!')
            isSorted = True

        attempt = attempt + 1




