from Day12 import logo, end_logo_off
import random

easy = 10
hard = 5

print('*** My dear friend, welcome to Sajjad  number guessing game *** ')
print('This game is for guessing numbers between 1 and 100 ... ')


def Random_selection():
    """
           این تابع یک عدد رندوم بین 1 تا صد را اختصاص می دهد
    """
    num = range(1, 100)
    x = random.choice(num)
    return x


computer_num = Random_selection()
print(computer_num)

# پیادهسازی عملیات حدس عدد توسط کاربر
user_input = True


def easy():
    global user_input
    for x in range(1, 11):
        guess = int(input('make to guess :'))
        if guess == computer_num:
            # print پیغام افرین درست حدس زدید
            print('*** Well done, your guess is correct ...! ***')
            break
        elif guess > computer_num:
            # پیغام انتخاب شما بزرگتر است
            print('The number is larger')

        elif guess < computer_num:
            # پیغام عدد وارد شده کوچکتر است
            print('The number is smaller')
        else:
            print('sorry you lost in this hand...***')


def hard():
    global user_input
    for x in range(1, 6):
        guess = int(input('make to guess :'))
        if guess == computer_num:
            # print پیغام افرین درست حدس زدید
            print('*** Well done, your guess is correct ...! ***')
            break
        elif guess > computer_num:
            # پیغام انتخاب شما بزرگتر است
            print('The number is larger')
        elif guess < computer_num:
            # پیغام عدد وارد شده کوچکتر است
            print('The number is smaller')
        else:
            print('sorry you lost in this hand...***')


message_user_level = input('Dear user, what level do you want to play, hard or easy for hard enter hard for easy also '
                           'enter easy :')
if message_user_level == 'easy':
    easy()
    print(logo.logo_guess_number)

elif message_user_level == 'hard':
    hard()
    print(logo.logo_guess_number)
else:
    print(end_logo_off.end_logo)

