# https://edabit.com/challenge/xbjDMxzpFcsAWKp97

import numpy as np


def can_see_stage(seats):
    # could be done without, but numpy's performance is far better
    np_seats = np.array(seats).transpose()
    np_seats = np.array_split(np_seats, len(np_seats))

    for i in range(len(np_seats)):
        # first compared seat must always be bigger than actual first seat
        temp = float('inf')
        for j in (np_seats[i][0][::-1]):
            if j >= temp:
                return False
            else:
                temp = j

    return True
