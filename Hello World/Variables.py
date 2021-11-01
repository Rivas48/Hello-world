life = int(5)
answer = '';
response = input('What phrase are we playing with today? ')
print(response);

while (life >= 0):
    guess = input('Player two please guess a phrase ');
    print(guess);
    search = response.find(guess)
    print(str(search))

    if( search >= 0):
        print('please remove letter ' + guess)
        answer + str(response[guess])
    elif(search < 0):
        life -= 1
        print('loser you now have ' + str(life))
    else:
        print('game over');
