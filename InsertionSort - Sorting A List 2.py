#Insertion sort / Mitchell Docherty
import time

Numlist = ['45', '63', '73', '23', '81', '18']


def InsertionSort(Numlist):

    for j in range(1, len(Numlist)):

        print("***************** LOOP", j, "*********************\n")

        key = Numlist[j]
        i = j - 1
        print("i:", i, " |  A[i]:", Numlist[i], " |  key:", key, "\n")
        print("IS i:", i, ">= 0 and", Numlist[i], ">", key, "?", "\n")

        while i >= 0 and Numlist[i] > key:

            print("TRUE:", i, ">= 0 and", Numlist[i], ">", key, "\n")

            Numlist[i + 1] = Numlist[i]  # left cell switches places with right cell
            i = i - 1
            print(Numlist)
            print("\n")
            time.sleep(1)
        Numlist[i + 1] = key

    print("\n\n")
    print("=================== END =====================")


InsertionSort(Numlist)
