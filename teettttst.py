# coding: utf-8
def isequal(chance, continueindex, num1, num2):
    """
    chance for the number of chances to guess;
    continueindex==True, goes on;
    continueindex==False, stops;
    """
    if num1 < num2:
        chance -= 1
        print "%d is too small, you have %d chances left, negative input to stop the game" % (answer, chance)
        return chance, continueindex
    elif num1 > num2:
        chance -= 1
        print "%d is too big, you have %d chances left, negative input to stop the game" % (answer, chance)
        return chance, continueindex
    else:
        print "Bingo, %d is the right answer!" % answer
        continueindex = False
        return chance, continueindex


while continueindex and chance != 0:
    answer = input()
    while not isinstance(answer, int):
        print answer, "is not a required integer:\n"
        answer = input()
    if answer < 0:
        print('SeeYa!')
        break
    chance, continueindex = isequal(chance, continueindex, answer, num)
