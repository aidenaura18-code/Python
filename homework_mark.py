mark=["Aiden=90","Ben=85","Cathy=95","David=80","Eva=88"]
print(mark)
print(len(mark))
mark[0]
mark[-1]
print(mark[0])
print(mark[-1])

mark[0:3]
mark[::-1]


def total_marks(mark):
    total=0
    for i in mark:
        score=int(i.split("=")[1])
        total+=score
    return total


def average_marks(mark):
    total=total_marks(mark)
    average=total/len(mark)
    return average