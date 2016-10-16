def regcount():
    # -*- coding: utf-8 -*-
    import re

    left = ("[Лл]ев")
    right = ("[Пп]рав")
    front = ("[Пп]еред[^н]")
    frontpart = ("передн")
    behind_szadi = ("зади") #сзади, позади
    behind_za = ("[Зз]а ")
    behind_gen = ("зади|[Зз]а ")
    hindpart = ("задн")
    against = ("[Пп]ротив")
    near1 = ("[Оо]коло")
    near2 = ("[Бб]ли[жз]")
    near3 = re.compile("[Рр]яд[о|ы]")
    near4 = re.compile("[Вв]озле")
    near_gen = re.compile("([Оо]коло|[Бб]ли[жз]|[Рр]яд[о|ы]|[Вв]озле)")
    far = re.compile(" [Дд]ал[ье]")#подальше, поодаль, далеко, дальше
    edge = re.compile("кра[юея]")
    aside = re.compile ("[Сс]бок")
    side = re.compile("сторон")
    up = re.compile("верх")
    down = re.compile("[Нн]и[зж]")
    between = re.compile("[Мм]еж")
    center = re.compile("(центр|серед)")
    table = "стол"

    regnames = ['left','right', 'front', 'frontpart', 'behind_gen', 'hindpart', 'near_gen','far','edge','aside','side','up','down','center']
    regvalues = ["[Лл]ев","[Пп]рав" ,"[Пп]еред[^н]","передн", "зади|[Зз]а ", "задн",  "([Оо]коло|[Бб]ли[жз]|[Рр]яд[о|ы]|[Вв]озле)|[Нн]едал" ," [Дд]ал[ье]" ,"кра[юея]" ,
                 "бок", "сторон","верх","[Нн]и[зж]", "(центр|серед)",]



    regs = list(zip(regnames,regvalues))
    # print(regs)

    # def counter(reg, text):
    #     cntr = 0
    #     t = {}
    #     for line in text:
    #         cntr += len(re.findall(re.compile(reg), line))
    #         # print (cntr, reg)
    #     t[reg]= cntr
    #     # print(t)
    #     return cntr

    def counter(regg, text):
        line_list = []
        line_numbers = []
        totdict = {}
        d = {}
        cnt = 0
        for j,k in regg:
            totdict[j]= 0
            d[j] = 0
        for i, line in enumerate(text):
            ans = len(re.findall("\'", line))/2
            # print('answers: in line' ,i, ':',ans)
            line_numbers.append(i)
            # line_list = []
            for j, k in regg:
                # d = {}
                cntr = len(re.findall(re.compile(k), line))/ans
                d[j] = cntr
                totdict[j]+=cntr
            # print(d)
            line_list.append(d.copy())
        numerated = list(zip(line_numbers,line_list))
        # print(totdict)
        # print(len(line_list))
        return line_list

    '''
    thoughts about normalize: maybe divide not by total amount of items found, but by the length of the list\.
    this will be not totally normalized, but nevertheless would give a better quality. Later you might wanna make this
    into a properly normalized set of values
    '''

    def normalize(numerated):
        norm = []
        # numbers = []
        for dic in numerated:
            total = sum(dic.values())
            n = {k: v / total for k,v in dic.items()}
            norm.append(n)
        # k = list(zip(numbers, norm))
        return norm


    text = open('listbycolumn.txt', 'r', encoding='utf-8')

    a = counter(regs, text)
    # print(a)
    # print(len(a))
    # print(a[5])
    # print(normalize(a))
    return a #normalize(a)

if __name__ == '__main__':
    regcount()
