import random
suits = ["clubs","diamonds","hearts","spades"]
faces = ["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("我有这个",my_face,"of",my_suit)
    print("faces.index:",faces.index(my_face))
    print("你有这个",your_face,"of",your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("我赢了!")

    elif faces.index(my_face) < faces.index(your_face):
        print("你赢了!")

    else:
        print("平局!")

    answer = input("按下[Enter]键可以再来一次，其他键退出:")
    keep_going = (answer == "")






