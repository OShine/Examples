while True:
    x = int(raw_input("Enter the number: "))
    if x < 0:
        x = 0
        print 'The negative one, changed to zero'
    elif x == 0:
        print 'Zero'
    elif x == 1:
        print 'The One'
    else:
        print 'Overflow'