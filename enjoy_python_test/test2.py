# Author:Mr浩

bonus=100000
bonus1=bonus+bonus*0.1
bonus2=bonus1+bonus*0.075
bonus4=bonus2+bonus*0.05*2
bonus6=bonus4+bonus*0.03*2
bonus10=bonus6+bonus*0.015*4
prafit=input("请输入月利润")
if prafit.isdigit():
    prafit=int(prafit)
    if prafit<=bonus:
        print(bonus1)
    elif prafit<=bonus*2:
        print(bonus1+(prafit-bonus)*0.075)
    elif prafit<=bonus*4:
        print(bonus1+(prafit-bonus)*0.075)
    elif prafit<=bonus*6:
        print(bonus6)
    else:
        print(bonus10)