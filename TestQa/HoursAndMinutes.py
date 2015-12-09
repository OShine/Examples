while True:
    try:
        print 'Please, enter the value of time as integer'
        minutes = int(raw_input())
    except ValueError:
         print 'The entered value should be an integer. Please, try again.'
    else:
        a = minutes % 60
        if minutes < 60:
            print(str(0) + " hours")
            print(str(a) + " minutes")
        else:
            print(str(minutes/60) + " hour")
            print(str(a) + " minutes")
