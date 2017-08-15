number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    #新块从这里开始
    print('Congratulations, you guessed it')
    print('(but you do not win any prizes!)')
    #新块从这里结束
elif guess < number:
    #另一代码块
    print('No, it is a little higher than that')
    #你可以在此做任何你希望在该代码块内进行的事情
else:
    print('no, it is a lettle lower than that')
    #你必湎通过猜测一个大于（>）设置数的数字来到达这里
    input()
print('Done')
#这最后一句话将在
#if 语句执完毕后执行

if True:
    print(number)