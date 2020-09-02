# def exps(x, y, z):
#     """From the README.md

#     Args:
#         x (int): input as large as 150
#         x (int): input as large as 400
#         x (int): input as large as 800

#     Returns:
#         [int]
#     """
#     if x <= 0:
#         return y + z
#     if x > 0:
#         exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)


# Gonna phone a friend
webster = {}


def expensive_seq(x, y, z):
    """
    Args:
        x (int): input as large as 150
        y (int): input as large as 400
        z (int): input as large as 800
    Returns:
        [int]: ex. 2 3 4 = 73
    """
    if (x, y, z) not in webster:
        if x <= 0:
            webster[x, y, z] = y + z
        elif x > 0:
            webster[(x, y, z)] = (
                expensive_seq(x - 1, y + 1, z)
                + expensive_seq(x - 2, y + 2, z * 2)
                + expensive_seq(x - 3, y + 3, z * 3)
            )

    return webster[x, y, z]


##############################################################################
if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
