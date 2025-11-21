
T = int(input(""))
for i in range(T):
    S = input()
    rev = S[::-1]
    if S==rev:
        print(1)
    else:
        print(0)
