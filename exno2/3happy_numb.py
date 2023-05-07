# happy number using user define function

def happy(n):
    track = set()
    while n != 1:
        n = sum(int(digit)**2 for digit in str(n))
        if n in track:
            print("IT IS NOT A HAPPY NUMBER")
        track.add(n)
    print("IT IS A HAPPY NUMBER")

inp=input("ENTER THE NUMBER:")
happy(inp)
