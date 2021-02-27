print("Heyyaa!! Use your brain to bring out some really funny content...")
a = int(input("Enter your choice(Food/Game/Tourism)(1/2/3): "))
if a==1:
    f = open('M.Content_Food')
elif a==2:
    f = open('M.Content_Game')
else:
    f = open('M.Content_Tourism')
allLines = f.readline()
#print(allLines)
halves = allLines.split("#")
madbText = halves[1]
inputs = halves[0].split(",")
inputStore = [""]
for item in inputs:
    inputStore.append(input("Enter a "+item+":"))
for i in range(len(inputStore)):
    madbText = madbText.replace("%"+str(i), inputStore[i])
madbText = madbText.strip()
print(madbText)

