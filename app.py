from random import randint


def choose_marker(marker1='', marker2=''):
    while marker1 != 'X' and marker1 != 'O':
        marker1 = input('Player 1 choose either X or O ').upper()
        if marker1 == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
    print(f'Player 1 : {marker1}\nPlayer 2 : {marker2}\n')
    return marker1, marker2


def turn_decider():
    turn = randint(1, 2)
    print(f'Player {turn} will go first ')
    return turn


def dummy_board():
    print(f'   7 | 8 | 9  ')
    print('---------------')
    print(f'   4 | 5 | 6  ')
    print('---------------')
    print(f'   1 | 2 | 3  ')


def move_player1(marker1, positions):
    pos = int(input(print('\nPlayer 1 choose position (1-9) : ')))
    if positions[pos - 1] == ' ':
        positions[pos - 1] = marker1
    else:
        print('\n Position already occupied, choose another one ')
        move_player2(marker1, positions)


def move_player2( marker2, positions):
    pos = int(input(print('\nPlayer 2 choose position (1-9) : ')))
    if positions[pos - 1] == ' ':
        positions[pos - 1] = marker2
    else:
        print('\n Position already occupied, choose another one ')
        move_player2(marker2, positions)


def marker_board(marker1, marker2, positions):
    print(f'   {positions[6]} | {positions[7]} | {positions[8]}  ')
    print('---------------')
    print(f'   {positions[3]} | {positions[4]} | {positions[5]}  ')
    print('---------------')
    print(f'   {positions[0]} | {positions[1]} | {positions[2]}  ')


def win_decider(marker1, marker2, positions):
    if (positions[0] == marker1 and positions[1] == marker1 and positions[2] == marker1) or (positions[3] == marker1 and positions[4] == marker1 and positions[5] == marker1) or (positions[6] == marker1 and positions[7] == marker1 and positions[8] == marker1) or (positions[0] == marker1 and positions[3] == marker1 and positions[6] == marker1) or (positions[1] == marker1 and positions[4] == marker1 and positions[7] == marker1) or (positions[2] == marker1 and positions[5] == marker1 and positions[8] == marker1) or (positions[2] == marker1 and positions[4] == marker1 and positions[6] == marker1) or (positions[0] == marker1 and positions[4] == marker1 and positions[8] == marker1):
        print('player 1 won. Hurray!')
        return True
    elif (positions[0] == marker2 and positions[1] == marker2 and positions[2] == marker2) or (positions[3] == marker2 and positions[4] == marker2 and positions[5] == marker2) or (positions[6] == marker2 and positions[7] == marker2 and positions[8] == marker2) or (positions[0] == marker2 and positions[3] == marker2 and positions[6] == marker2) or (positions[1] == marker2 and positions[4] == marker2 and positions[7] == marker2) or (positions[2] == marker2 and positions[5] == marker2 and positions[8] == marker2) or (positions[2] == marker2 and positions[4] == marker2 and positions[6] == marker2) or (positions[0] == marker2 and positions[4] == marker2 and positions[8] == marker2):
        print('player 2 won. Hurray!')
        return True
    else:
        return False


def game():
    marker1, marker2 = choose_marker()
    turn = turn_decider()
    dummy_board()

    positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    win = False
    move_number = 0
    if turn == 1:
        sign = 1
    else:
        sign = -1
    while not win and move_number < 9:
        if sign == 1:
            move_player1(marker1, positions)
        else:
            move_player2(marker2, positions)
        marker_board(marker1, marker2, positions)
        win = win_decider(marker1, marker2, positions)
        move_number += 1
        sign = sign*(-1)


playing_mood = True
while playing_mood:
    game()
    if input(print('\n Want to play more , Y or N :')).upper() == 'Y':
        playing_mood = True
    else:
        playing_mood = False
        print('\n Will meet soon ')




