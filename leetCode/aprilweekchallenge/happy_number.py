def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    numbers = set()
    while True:
        if n in numbers:
            return False
        elif n == 1:
            return True
        else:
            numbers.add(n)
            n= sum([int(x) ** 2 for x in str(n)])

print(isHappy(130))
