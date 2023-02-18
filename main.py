#Write your code here.
n = input()
n = n.split()

f = []
for i in n:
    f = '{:,}'.format(int(i))
    f.append(i)

print(f)
