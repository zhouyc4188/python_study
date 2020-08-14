import random
x = ["1","2","3","4","5","6"]
keep_going = True
while keep_going:
    one_x = random.choice(x)
    two_x = random.choice(x)
    three_x = random.choice(x)
    
    print("one有这个",one_x)
    print("two有这个",two_x)
    print("three有这个",three_x)

    
    answer = input("按下[Enter]键可以再来一次，其他键退出:")
    keep_going = (answer == "")
