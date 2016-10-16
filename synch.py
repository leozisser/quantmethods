def getanswers():
    from os.path import join
    from os import listdir
    import pandas as pd
    import re
    text = open("listbycolumn.txt", 'w', encoding='utf-8')
    listbycol_all = []
    for i in listdir("C:\\coding\\expedition\\text"):
        with open(join("C:\\coding\\expedition\\text", i), 'r', encoding='utf-8') as curfile:
            data = pd.read_csv(curfile)
            df = pd.DataFrame(data)
            listbycol = []
            cnt = 0
            for l in df:
                print(l)
                cnt += 1
            print(cnt)
            for j in range(1,cnt):
                col = df.iloc[:,j]
                print('col',col)
                col_list = []
                for h in col:

                    col_list.append(h)
                text.write(str(col_list)+ str(len(col_list))+'\n')
                listbycol.append(col_list)
            # print(listbycol[1])
            listbycol_all.append(listbycol)
    # print(listbycol_all)

    return listbycol_all


if __name__ == '__main__':
    getanswers()
