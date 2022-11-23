import datetime
Str1 = {"time": ("доброй ночи", "доброе утро", "добрый день", "добрый вечер", "Полночь")}

now = datetime.datetime.now()
# 0 <= now.hour <= 24
# greet: str = Str1["time"][5]
if 0 <= now.hour < 6:
    greet: str = Str1["time"][0]
if now.hour == 24:
    greet: str = Str1["time"][4]
if 6 <= now.hour < 12:
    greet: str = Str1["time"][1]
if 12 <= now.hour < 16:
    greet: str = Str1["time"][2]
if 16 <= now.hour < 24:
    greet: str = Str1["time"][3]


def talk(words): print(words)


talk(greet.title() + " ^_*_^ " + " - замечательное время суток!")


"""x = 0
print("x =", x)
y = 10
print("y =", y)"""


print("Hello World!")
X = 5
print("x =", X)
Y = 10
print("y =", Y)

Z = 10
print("z =", Z)
