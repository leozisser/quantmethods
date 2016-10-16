__author__ = 'Leo'
import operator, re
from os import listdir
from os.path import isfile, join
from synch import getanswers
from reg_count import regcount
from collections import defaultdict
filesbyfolders = {}


def onlyfiles(dirr):
    files = []
    files1 = [f for f in listdir(join("C:\\coding\\expedition",dirr))[:15] if isfile(join("C:\\coding\\expedition", dirr, f))and len(f) > 12]
    files2 = [f for f in listdir(join("C:\\coding\\expedition",dirr))[16:] if isfile(join("C:\\coding\\expedition", dirr, f))and len(f) > 12]
    files.append(files1)
    files.append(files2)
    return files1, files2


def onlyfiles_1(dirr):
    files1 = [f for f in listdir(join("C:\\coding\\expedition",dirr))[:15] if isfile(join("C:\\coding\\expedition", dirr, f))]#and len(f) > 12]
    return files1


def onlyfiles_2(dirr):
    files2 = [f for f in listdir(join("C:\\coding\\expedition",dirr))[15:] if isfile(join("C:\\coding\\expedition", dirr, f))and len(f) > 12]
    return files2

for d in listdir("C:\coding\expedition")[0:3]:
    #print(d)
    filesbyfolders[str(d) + ".1"] = onlyfiles_1(d)
    filesbyfolders[str(d) + ".2"] = onlyfiles_2(d)

#repair
filesbyfolders["sample 1.1"].pop(6) #CROTCH WARNING! Escaping thumbs.db
# print (filesbyfolders)
# for i in filesbyfolders:
#     print( i, len(filesbyfolders[i]))
# print(filesbyfolders["sample 1.1"])
#end of repair

filesbyfolders_sorted = sorted(filesbyfolders.items())#, key=operator.itemgetter(0))
# print(filesbyfolders_sorted)

components_orange = re.compile("(?<=o_).{3,10}(?=_a)") #findall().replace('_', ';')
components_apple = re.compile("(?<=a_).{3,10}(?=_t)") #findall().replace('_', ';')
tilt = re.compile("(?<=t)\d{1,2}")


def normalorder(k): #groups stimuli in  general order of asking about a picture: first orange, then apple
    l = []
    comp_tilt = re.search(tilt, k).group(0)
    # l.append(comp_tilt)
    comp_or = re.search(components_orange, k).group(0).replace('_', ',') + ',' + comp_tilt
    l.append(comp_or)
    comp_ap = re.search(components_apple, k).group(0).replace('_', ',') + ',' + comp_tilt
    l.append(comp_ap)
    return l


def inverseorder(k): #inverse order of asking
    l = []
    comp_tilt = re.search(tilt, k).group(0)
    # l.append(comp_tilt)
    comp_or = re.search(components_orange, k).group(0).replace('_', ',') + ',' + comp_tilt

    comp_ap = re.search(components_apple, k).group(0).replace('_', ',') + ',' + comp_tilt
    l.append(comp_ap)
    l.append(comp_or)
    return l

for key, val in filesbyfolders_sorted: #we need this because for some pics the questions werein inverse order, first apple then orange
    for n, i in enumerate(val):
        if n in [1, 4, 6, 7, 8]:
            val[n] = inverseorder(i)
        else:
            val[n] = normalorder(i)

samples_list = [] #this block gives list of [[individual pics in fine order] by folder]
pictures_list = []
for i, j in filesbyfolders_sorted:
    samples_list.append(i)
    simplelist = []
    for k in j:
        for h in k:
            #print(h)
            simplelist.append(h)
    pictures_list.append(simplelist)
# print('pictures_list',pictures_list)
# finallist = list(zip(samples_list,pictures_list))
# print(finallist)

# answers = getanswers()  #this is important for renewing answer base, uncomment this after changing answer files
# # print(answers)
# thelist = []
# for i,j in enumerate(pictures_list):
#     # print(i)
#     sublist = list(zip(j, answers[i]))
#     # print(sublist)
#     for l in sublist:
#         thelist.append(l)
# print(thelist)

lastdict = [] #somehow packs coordinartes of a stimulus as elements of a single list into a general list
for j in pictures_list:
    # print(len(j))
    for i in j:
        k = re.findall("[^,]{1,4}", i)
        # print(k)
        lastdict.append(k)
# print('lastdict', lastdict)
print('piclist',pictures_list)


normlist = regcount()
# print('normlist',normlist)
# print(len(normlist))


def dsum(dicts):
    ret = defaultdict(float)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)


#temporarily blocked
# k = open('features.txt', 'w', encoding='utf-8')
f = (list(zip(lastdict, normlist)))
print('f', f)
# print(len(f))
# k.write(str(f))
'''
you shall also have to even them by degree, tilt and radius so as to plot them via any of those coordinates
'''

dict_c1 = {}
for i, j in f:  #sorts normalized(?) answers by component 1 of the stimuli, returns dict {value of comp1 : list of  all dicts(keyword : normalized count)}
    if i[1] not in dict_c1:
        dict_c1[i[1]] = []
        dict_c1[i[1]].append(j)
    else:
        dict_c1[i[1]].append(j)
# print('dict_c1',dict_c1)

dictc1 = {}
for i in dict_c1: #normalizes values in dicts yet again, dividing them by length of every list of dicts by component n
    le = len(dict_c1[i])
    # print(len(dict_c1['0']))
    sublist = []
    for dic in dict_c1[i]:
        n = {k: v / le for k, v in dic.items()}
        sublist.append(n)
    dictc1[i]=sublist
print('dictc1',dictc1)

dictforplot = {} #sums all dicts which are values for a key (component n)
for i in dictc1:
    # print('i',i)
    kk = dsum(dictc1[i])
    if int(i) >= 0:
        dictforplot[i] = kk
    elif int(i) < 0:
        dictforplot[str(360 + int(i))] = kk
print('dictforplot',dictforplot)

plotme = [(k, dictforplot[k]) for k in sorted(dictforplot, key=int)]
print (plotme)
# for i,j in plotme:
    # print(i)
# plotme = []
# for i in dictforplot:
#     k = list(zip(i,dictforplot[i]))
#     print(k)
#     plotme.append(k)
complist = []
for i in dictforplot:
    complist.append(i)
print(complist)