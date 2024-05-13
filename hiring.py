import random
candidates=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
randomize=[]
hired=[]

for i in range(len(candidates)):
    ran=random.choice(candidates)
    candidates.remove(ran)
    randomize.append(ran)

max=-1
for i in range(len(randomize)):
    if(randomize[i]>max):
        max=randomize[i]
        hired.append(randomize[i])

cost=len(hired)


print(f"Interviewed candidates: {randomize}")
print(f"Hired candiates: {hired}")
print(f"firing Cost: {cost-1}")
print(f"No of candidates: {len(hired)}")
