# https://edabit.com/challenge/4AjWvJdZpFEMbGALd


def who_goes_free(n, k):
    if n < 1:
        raise TypeError("N must be bigger than 0")

    counter = 1
    temp_list = []
    prisoners = list(range(0, n, 1))
    while len(prisoners) > 1:
        for captive in prisoners:
            if counter >= k:
                counter = 1
            else:
                temp_list.append(captive)
                counter += 1
        prisoners = temp_list
        print("Round end", prisoners)
        temp_list = []
    return prisoners[0]

