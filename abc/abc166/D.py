def main():
    x = int(input())
    d = {}
    for a in range(-200, 201):
        d[a ** 5] = a

    for a5, a in d.items():
        b5 = a5 - x
        b = d.get(b5, None)
        if not b is None:
            print(a, b)
            return

if __name__ == "__main__":
    main()