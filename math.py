def MinecraftDays(days):
    x = 0
    days *= 20
    while days > 60:
        days -= 60
        x += 1
    print(x,"hours and",days,"minutes")