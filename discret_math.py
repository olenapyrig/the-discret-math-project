Настя Уку, [09.01.18 23:21]
def main():
    """
    The main function. Displays a data entry request and
    displays the result of the program
    """
    print("Welcome!/ Ласкаво просимо!")
    n =int(input("Please enter a length (n)/ Будь ласка введіть довжину (n): "))
    len_lst = n**2
    lst = [0 for i in range(len_lst)]
    count = 0
    for i in range(0, 2*(len_lst)):
        #create new row
        for m in range(len_lst - 1, -1, -1):
            if lst[m] != 1:
                for j in range(m + 1, len_lst):
                    lst[j] = 0
                lst[m] = 1
                break
        #check this row
        if check(lst,n) == True:
            for j in range(0, len_lst, n):
                print(lst[j:j+n])
            print("---------")
            count +=1
        else:
            break

    print("Ammount of transitive/Кількість транзитивних відношень = ", count)
    second_v(n)

def check(lst, n):
    """
    Checks whether the list is a transitive relation or not
    >>>check([0, 0, 1, 0, 0, 0, 0, 1, 0],3)
    True
    >>>check([0, 0, 1, 0, 0, 0, 0, 0, 0],3)
    True
    """
    for i in range(n**2):
        r = i // n
        col = i - (r * n)
        if lst[i] != 0:
            for k in range(col * n, (col * n)+n):
                a = (r - col) * n + k
                if lst[a] != 1 and lst[k] == 1 :
                    return (False)
                else:
                    return (True)

def second_v(n):
    """
    Shows another version of the relationship
    """
    lst = []
    for i in range (1, n+1):
        lst.append(i)
    m_lst = []
    for i in lst:
        for j in range(1, n+1):
            lst1 = [i, j]
            m_lst.append(lst1)
    print("\n")
    print ("Also, the transitive relation can be written as/\
    \nТакож транзитивні відношення можно записати таким чином:")
    print("\n", m_lst, "\n")

main()
