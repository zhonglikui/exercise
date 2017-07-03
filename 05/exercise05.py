filename = "Android.txt"
key = "Android"
file = open(filename)

text = file.read()
beg = 0
num = 0

while text.find(key) != -1:

    num = num + 1
    text = text.split(key,1)[1]
print(num)
file.close()