minutes = int(raw_input())
a = minutes % 60
if minutes < 60:
    print(str(0) + " hours")
    print(str(a) + " minutes")
else:
    print(str(minutes/60) + " hours")
    print(str(a) + " minutes")
