def wreid_sort(tab:list[str]):
    for j in range(1,len(tab)+3):
        for i in range(len(tab)-j):
            if int(tab[i][0]) < int(tab[i+1][0]):
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp

            elif int(tab[i][0]) == int(tab[i+1][0]):
                q = 1
                k = 0
                while (int(tab[i][k]) == int(tab[i+1][k])) and k < len(tab[i]):
                    k += 1
                    q *= -1

                if int(tab[i][k]) < int(tab[i+1][k]) * q:
                    temp = tab[i]
                    tab[i] = tab[i + 1]
                    tab[i + 1] = temp

    return tab


print(wreid_sort(['123','125','121','135','222']))