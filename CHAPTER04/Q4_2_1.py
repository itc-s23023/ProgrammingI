
#  textbook_question
def number_to_day(num=0):
    """任意の整数が与えられたら今日、昨日、明日、それ以外を判定して返す関数"""
    if num == 0:
        day = "today"
    elif num == 1:
        day = "tomorrow"
    elif num == -1:
        day = "yesterday"
    else:
        day = "over_one_day"
    return day



