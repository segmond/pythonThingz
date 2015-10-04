def countdown(n):
    print "Counting down from ", n
    while n > 0:
        yield n
        n -= 1
    print "Done counting down"

for i in countdown(10):
    print i
