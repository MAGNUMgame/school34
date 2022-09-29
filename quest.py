b = input("What is your name? ")
while True:
    print("forward, left, right, fight, /kill")
    print("")
    try:
        a = input("What you want to do? ")
    except:
        print("писать только из предложеных.")
    else:
        if a == "forward":
            print("You moved forward.")

        elif a == "left":
            print("You turned left.")

        elif a == "right":
            print("You turned right.")

        elif a == "/kill":
            print("You killed your self(")
            print("Game over." + b)


