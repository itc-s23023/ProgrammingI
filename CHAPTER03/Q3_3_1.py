my_li = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
save_li = []
for i in my_li:
    if len(i) >= 6:
        save_li.append(i)
print(save_li)


# save_li = [i for i in my_li if len(i) >= 6]
