import datetime
Str1 = {"time": ("доброй ночи", "доброе утро", "добрый день", "добрый вечер")}

now = datetime.datetime.now()

if 0 <= now.hour < 6:
    pass
else:
    greet: str = Str1["time"][0]
if 6 <= now.hour < 12:
    pass
else:
    greet: str = Str1["time"][1]
if 12 <= now.hour < 16:
    pass
else:
    greet: str = Str1["time"][2]
if 16 <= now.hour < 0:
    greet: str = Str1["time"][3]
else:
    pass


def talk(words): print(words)


talk(greet.title() + " ^_*_^ " + " - замечательное время суток!")


"""x = 0
print("x =", x)
y = 10
print("y =", y)"""
