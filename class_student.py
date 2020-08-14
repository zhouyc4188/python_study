class Student(object):
    math = 100
    chinese = 90
    english = 99
    
    def __init__(self, math,chi,eng):
        self.math = math
        self.chinese = chi
        self.english = eng

    def totalscore(self):
        return self.math + self.chinese + self.english
        
    def averagescore(self):
        return (self.math + self.chinese + self.english)/3


    def say(self, content):
        print(self.totalscore)
        print(self.averagescore)

    def set_score(self,math,chi,eng):
        self.math = math
        self.chinese = chi
        self.english = eng


class Student_Node(object):
    math = 100
    chinese = 90
    english = 99
    
    def __init__(self, math,chi,eng):
        self.math = math
        self.chinese = chi
        self.english = eng
        self.next = None

   
    def set_next(self,next):
        self.next = next

    def totalscore(self):
        return self.math + self.chinese + self.english
        
    def averagescore(self):
        return (self.math + self.chinese + self.english)/3


    def say(self, content):
        print(self.totalscore)
        print(self.averagescore)

    def set_score(self,math,chi,eng):
        self.math = math
        self.chinese = chi
        self.english = eng

zhangsan1 = Student(100,98,96)
lisi1 = Student(50,60,70)
xiaoming1 = Student(90,68,94)
xiaowang1 = Student(100,100,100)
xiaobing1 = Student(9990,6,2)

zhangsan2 = Student_Node(100,98,96)
lisi2 = Student_Node(50,60,70)
xiaoming2 = Student_Node(90,68,94)
xiaowang2 = Student_Node(100,100,100)
xiaobing2 = Student_Node(9990,6,2)
Student_end = Student_Node(100000,100000,100000)

print(zhangsan1.totalscore())
print(zhangsan1.averagescore())


print(lisi1.totalscore())
print(lisi1.averagescore())

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
    def set_next(self,next):
        self.next = next


def get_all_totalscore_and_averagescore_one(nd,subject):
    totalscore = 0
    averagescore = 0
    count = 0
    node = nd
    while node.next != None:
        st = node.data
        count += 1
        if subject == "math":
            totalscore+=st.math
        elif subject == "chinese":
            totalscore = totalscore + st.chinese
        elif subject == "english":
            totalscore = totalscore + st.english
        node = node.next
        
    return totalscore,totalscore/count
        

def get_all_totalscore_and_averagescore_two(st_nd,subject):
    totalscore = 0
    averagescore = 0
    count = 0
    st = st_nd
    while st.next != None:
        
        count += 1
        if subject == "math":
            totalscore+=st.math
        elif subject == "chinese":
            totalscore = totalscore + st.chinese
        elif subject == "english":
            totalscore = totalscore + st.english
        st = st.next
        
    return totalscore,totalscore/count

node1 = Node(data=zhangsan1)
node2 = Node(data=lisi1)
node3 = Node(data=xiaoming1)
node4 = Node(data=xiaowang1)
node5 = Node(data=xiaobing1)
node_end = Node(data=None)

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node_end)

print(get_all_totalscore_and_averagescore_one(node1,"math"))
print(get_all_totalscore_and_averagescore_one(node1,"english"))
print(get_all_totalscore_and_averagescore_one(node1,"chinese"))


zhangsan2.set_next(lisi2)
lisi2.set_next(xiaoming2)
xiaoming2.set_next(xiaowang2)
xiaowang2.set_next(xiaobing2)
xiaobing2.set_next(Student_end)

print(get_all_totalscore_and_averagescore_two(zhangsan2,"math"))
print(get_all_totalscore_and_averagescore_two(zhangsan2,"english"))
print(get_all_totalscore_and_averagescore_two(zhangsan2,"chinese"))


