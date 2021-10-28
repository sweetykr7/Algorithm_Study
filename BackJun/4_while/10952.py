import sys



while True:
    try:
        a, b = sys.stdin.readline().rstrip().split()
        d = int(a) + int(b)
        print(d)
    except:
        break
