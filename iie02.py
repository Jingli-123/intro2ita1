import sys
lists = []
sys.stdout.write("What's your name?\n")
str_name = sys.stdin.readline().strip()
name = str_name.title()
lists.append(name)

sys.stdout.write(f"{name},tell your age:\n")
age = int(sys.stdin.readline().strip())
lists.append(age)

sys.stdout.write(f"{name},tell us your weigh(kg):\n")
weigh = float(sys.stdin.readline().strip())
lists.append(weigh)


sys.stdout.write(str(lists))