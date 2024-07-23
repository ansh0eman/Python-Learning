def isModest(N, M):
    modest_nums = []
    for num in range(N, M+1):
        if modest(num):
            modest_nums.append(num)
    print(modest_nums)

def modest(num):
    num_str = str(num)
    length = len(num_str)

    for i in range(1, length):
        left_part = int(num_str[: i])
        right_part = int(num_str[i :])
        if right_part != 0 and num % right_part == left_part:
            return True
    return False

def main():
    X,Y = map(int, input().split())
    isModest(X, Y)

main()