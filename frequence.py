test ={ "jhon": 2,
        "rahul": 2 ,
        "david": 2,
        "alice": 2 ,
        "drake": 1}

count=0

for key in test:
    if test[key]== 2:
        count += 1
print(count)