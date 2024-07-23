def winRound(yourCards, opponentCards):
    my_biggest = biggest(yourCards)
    opp_biggest = biggest(opponentCards)
    print(my_biggest)
    print(opp_biggest)

    if(my_biggest > opp_biggest):
        print('true')
    else:
        print('fasle')


def biggest(array):
    
    first = second = 0

    for num in array:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    return int(f"{first}{second}")

def main():
    yourCards = list(map(int, input().strip().split()))
    opponentCards = list(map(int, input().strip().split()))

    winRound(yourCards, opponentCards)

main()
