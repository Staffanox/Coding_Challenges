# https://edabit.com/challenge/jgpfraMtc9nrrPZkL


def switch_gravity_on(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            y_pos = len(lst) - 1
            if lst[i][j] == '#':
                lst[i][j] = '-'
                while True:
                    if lst[y_pos][j] == '#':
                        y_pos -= 1
                        if y_pos < 0:
                            lst[0][j] = '#'
                            break
                    else:
                        lst[y_pos][j] = '#'
                        break
    return lst
