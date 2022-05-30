while True:
    try:
        N = int(input())
        if N >= 1 and N <= 100:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break
