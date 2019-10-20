import tqdm 

file = open("Results.txt","a+")
contents = file.read()

for i in range(len(contents)):
    temp = contents[i]
    if temp[2:] == 'x:':
        temp[:-2] += "\n"
    print(temp)


print("Complete")





