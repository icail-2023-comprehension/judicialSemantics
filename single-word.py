import time
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from gensim.models import Word2Vec,KeyedVectors
from numpy import dot
from numpy.linalg import norm
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import numpy as np 
import os
import os.path
import math
import sys
import scipy.stats as stats
from multiprocessing import Pool,Value    # multi-core support




plotSet = set(sys.argv[1:])

print("Set of words to plot")
print(plotSet)



#%matplotlib inline


time_start = time.time()
print("Loading german model")
german = KeyedVectors.load("deutsch.vector",mmap='r')
print("Loading law model")
model = KeyedVectors.load("urteile.vector",mmap='r')
print('Models loaded! Time elapsed: {} seconds'.format(time.time()-time_start))


time_start = time.time()
file = codecs.open("deutsch.counter", 'r', 'utf-8')
text = file.read()
file.close()

wikicount = dict()
for textline in text.split("\n"): #[:2000]:
    if textline.strip().isspace() or len(textline.strip()) == 0: continue
    count,word = textline.strip().split(" ")
    wikicount[word] = int(count)

file = codecs.open("urteile.counter", 'r', 'utf-8')
text = file.read()
file.close()
print('Count file loaded. Time elapsed: {} seconds'.format(time.time()-time_start))


time_start = time.time()
wortliste = list()
common_words = list()

for textline in text.split("\n"): #[:2000]:
    if textline.strip().isspace() or len(textline.strip()) == 0: continue
    count,word = textline.strip().split(" ")

    if word in model and word in german:
        wortliste.append(word)
        common_words.append((int(count) >= 100) and wikicount.get(word,0) >= 100)

print('Wortliste computed. Time elapsed: {} seconds'.format(time.time()-time_start))


print(len(wortliste))
wortset = set(wortliste)

uvecs = list()
gvecs = list()


time_start = time.time()
for wort in wortliste:
    uvecs.append(model[wort])
    gvecs.append(german[wort])

print('Vectors computed. Time elapsed: {} seconds'.format(time.time()-time_start))

###############################################################################################


def plotDataset(df,mainI,highlight,highlight2,highlight3,namex,namey,out):
    df['wordtype'] = [x == wortliste[mainI] for x in df.label];
    
    plt.figure(figsize=(20,10))
    plt.rc('text', usetex=True)
    p1 = sns.scatterplot(x=namex, # Horizontal axis
           y=namey, # Vertical axis
           data=df, # Data source
           size = 8,
           style="wordtype",
           legend=False)  
    
    plt.xlabel('')
    plt.ylabel('')

    ma = df.loc[:,namex].max()
    mi = df.loc[:,namex].min()
    rlenX = ma - mi
    ma = df.loc[:,namey].max()
    mi = df.loc[:,namey].min()
    rlenY = ma - mi
    #print("X %f Y %f" % (rlenX,rlenY))

    printed = list()
    for line in range(0,len(df.index)):
        if not(df.label[line] in highlight): continue
        
        col = 'green'
        if df.label[line] == wortliste[mainI]: col = 'red'

        p1.text(df.loc[line,namex]+0.01, df.loc[line,namey], 
        r'\Large{' + df.label[line] + '}', horizontalalignment='left', 
        size='x-large'
        #, color=col
        , weight='bold'
        ,bbox=dict(facecolor='grey',alpha=0.5)
        )
        printed.append((df.loc[line,namex], df.loc[line,namey], len(df.label[line])))

    
    for run in range(0,3):
        for line in range(0,len(df.index)):
            if df.label[line] in highlight: continue
            if (run == 0 and df.label[line] in highlight2) or (run == 1 and df.label[line] in highlight3) or (run == 2 and not(df.label[line] in highlight2) and not(df.label[line] in highlight3)):
                collision = False
                downCollision = False
                upCollision = False
                #charWidth = 0.0053
                charWidth = 0.008
                #minYDist = 0.015
                minYDist = 0.019
                for (x,y,wlen) in printed:
                    xDist = x - df.loc[line,namex]
                    yDist = abs(y - df.loc[line,namey])
                    yDistDown = abs(y - df.loc[line,namey] + 0.015*rlenY)
                    yDistUp = abs(y - df.loc[line,namey] - 0.015*rlenY )
                    xDist = xDist / rlenX
                    yDist = yDist / rlenY
                    yDistDown = yDistDown / rlenY
                    yDistUp = yDistUp / rlenY
                    if ((xDist > 0 and abs(xDist) < charWidth * len(df.label[line])) or
                            (xDist < 0 and abs(xDist) < charWidth * wlen)) and yDist < minYDist:
                        collision = True
                    if ((xDist > 0 and abs(xDist) < charWidth * len(df.label[line])) or
                            (xDist < 0 and abs(xDist) < charWidth * wlen)) and yDistDown < minYDist:
                        downCollision = True
                    if ((xDist > 0 and abs(xDist) < charWidth * len(df.label[line])) or
                            (xDist < 0 and abs(xDist) < charWidth * wlen)) and yDistUp < minYDist:
                        upCollision = True
    
                if run == 0:
                    if collision and downCollision and upCollision: collision = False

                txt = df.label[line]

                wei = 'normal'
                col = 'black'
                sty = 'normal'
                if df.label[line] in highlight2:
                    txt = r'\Large{\textbf{' + txt + '}}'
                    col = 'blue'; wei = 'semibold' ; sty = 'normal'
                if df.label[line] in highlight3:
                    col = 'orange'; wei = 'normal' ; sty = 'italic'
                    txt = r'\Large{\underline{' + txt + '}}'

                col = 'black'
    
                if not collision: 
                    p1.text(df.loc[line,namex]+0.005*rlenX, df.loc[line,namey], 
                    txt, horizontalalignment='left', 
                    size='x-large', color=col, weight=wei,style=sty)
                    printed.append((df.loc[line,namex], df.loc[line,namey], len(df.label[line])))
                elif not downCollision: 
                    p1.text(df.loc[line,namex]+0.005*rlenX, df.loc[line,namey] - 0.015 * rlenY, 
                    txt, horizontalalignment='left', 
                    size='x-large', color=col, weight=wei,style=sty)
                    printed.append((df.loc[line,namex], df.loc[line,namey] - 0.015 * rlenY, len(df.label[line])))
                elif not upCollision: 
                    p1.text(df.loc[line,namex]+0.005*rlenX, df.loc[line,namey] + 0.01 * rlenY, 
                    txt, horizontalalignment='left', 
                    size='x-large', color=col, weight=wei,style=sty)
                    printed.append((df.loc[line,namex], df.loc[line,namey] + 0.01 * rlenY, len(df.label[line])))
            #else:
            #    p1.text(df.loc[line,namex]+0.005*rlenX, df.loc[line,namey], 
            #    df.label[line], horizontalalignment='left', 
            #    size='medium', color='red', weight='semibold')

    #plt.show()
    p1.get_figure().savefig(out)




def tsne(woerter,vektoren):
    PCA_dims = 50
    woerter = sorted(set(woerter))
    pca_german = PCA(n_components=PCA_dims)
    if vektoren == 'german':
        pc_german = pca_german.fit_transform([german[x] for x in woerter])
    else:
        pc_german = pca_german.fit_transform([model[x] for x in woerter])

    print('Explained variation per principal component: {}'.format(pca_german.explained_variance_ratio_))
    print('Total explained variation %f' % sum(pca_german.explained_variance_ratio_))

    feat_cols = ['dim'+str(i) for i in range(0,PCA_dims)]
    df = pd.DataFrame(pc_german,columns=feat_cols)
    df['label'] = woerter


    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=30, n_iter=5000,metric="cosine")
    tsne_results = tsne.fit_transform(pc_german)

    print('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))

    df['tsne1'] = tsne_results[:,0]
    df['tsne2'] = tsne_results[:,1]

    return df

def cosine_similarity(a,b):
    return dot(a,b) / (norm(a) * norm(b))



################################################ MAIN





def getWordDef(j,gModel = 7, uModel = 7):
    print("  Getting Word Def for %-20s %d %d" % (wortliste[j],gModel,uModel))
    similars = list()
    for (w,sc) in german.most_similar(wortliste[j],topn=50):
        if w in wortliste:
            similars.append((sc,wortliste.index(w),'g'))
    for (w,sc) in model.most_similar(wortliste[j],topn=50):
        if w in wortliste:
            similars.append((sc,wortliste.index(w),'u'))

    takeSet = set()
    similars.sort(reverse = True)
    gTake=0
    uTake=0
    for (sc,w,t) in similars:
        maxSimI = -1
        idxI = 0
        for k in takeSet:
            udiff = cosine_similarity(uvecs[w], uvecs[k])
            gdiff = cosine_similarity(gvecs[w], gvecs[k])
            if udiff > maxSimI: maxSimI = udiff; idxI = k
            if gdiff > maxSimI: maxSimI = gdiff; idxI = k
        if ((t == 'g' and gTake < gModel) or (t == 'u' and uTake < uModel)) and maxSimI < 0.8:
            takeSet.add(w)
            if t == 'g': gTake += 1
            else: uTake += 1
            print("\t%-30s %0.7f %s\t\t %0.7f %-30s" % (wortliste[w],sc,t,maxSimI,wortliste[idxI]))

    return takeSet


def handleWord(i):
    diffList = list()
    dissimilarList = list() 
    a = uvecs[i]
    b = gvecs[i]
    for j in range(0,len(wortliste)):
        if not common_words[j]: continue
        udiff = cosine_similarity(a, uvecs[j])
        gdiff = cosine_similarity(b, gvecs[j])
        diff = udiff - gdiff
        #diffList.append((diff*diff,j,udiff,gdiff))
        diffList.append((abs(diff),j,udiff,gdiff))
        dissimilarList.append((min(udiff,gdiff),j))
        #print("%s %f %f %f" % (wortliste[j],udiff,gdiff,diff*diff))

    diffList.sort(reverse = True)
    dissimilarList.sort(reverse = False)

    diffSet = set()
    firstSet1 = set()
    firstSet2 = set()
    nearSet = set()


    gSet = german.most_similar(wortliste[i],topn=5000)
    uSet = model.most_similar(wortliste[i],topn=5000)
    
    num = 50
    gsim = set()
    for (ww,sc) in gSet:
        if ww in wortset:
            gsim.add(ww)
        if len(gsim) == num: break
    
    usim = set()
    for (ww,sc) in uSet:
        if ww in wortset:
            usim.add(ww)
        if len(usim) == num: break

    inter = gsim.intersection(usim)

    print(gsim)
    print(usim)
    print(inter)


    uInter = [(sc,ww) for (ww,sc) in uSet if ww in inter]
    uInter.sort(reverse = True)
    gInter = [(sc,ww) for (ww,sc) in gSet if ww in inter]
    gInter.sort(reverse = True)


    for (sc,w) in uInter:
        j = wortliste.index(w)

        maxSim = -1
        idx = 0
        for k in diffSet:
            udiff = cosine_similarity(uvecs[j], uvecs[k])
            gdiff = cosine_similarity(gvecs[j], gvecs[k])
            if udiff > maxSim: maxSim = udiff; idx = k
            if gdiff > maxSim: maxSim = gdiff; idx = k

        if maxSim < 0.9 and len(nearSet) < 5:
            print("Intersection:     %-30s %.7f" % (w,maxSim))
            nearSet.add(j)
            diffSet.add(j)
        #else:
        #    print("Reject:           %-30s %.7f" % (w,maxSim))

        if len(nearSet) == 5: break

    for (sc,w) in gInter:
        j = wortliste.index(w)

        maxSim = -1
        idx = 0
        for k in diffSet:
            udiff = cosine_similarity(uvecs[j], uvecs[k])
            gdiff = cosine_similarity(gvecs[j], gvecs[k])
            if udiff > maxSim: maxSim = udiff; idx = k
            if gdiff > maxSim: maxSim = gdiff; idx = k

        if maxSim < 0.9 and len(nearSet) < 10:
            print("Intersection:     %-30s %.7f" % (w,maxSim))
            nearSet.add(j)
            diffSet.add(j)
        #else:
        #    print("Reject:           %-30s %.7f" % (w,maxSim))

        if len(nearSet) == 10: break

    gn = gsim - inter
    un = usim - inter

    uNInter = [(sc,ww) for (ww,sc) in uSet if ww in un]
    uNInter.sort(reverse = True)
    gNInter = [(sc,ww) for (ww,sc) in gSet if ww in gn]
    gNInter.sort(reverse = True)


    ### German near, but not Urteil
    for w in gn:
        j = wortliste.index(w)
        maxSim = -1
        idx = 0
        for k in diffSet:
            udiff = cosine_similarity(uvecs[j], uvecs[k])
            gdiff = cosine_similarity(gvecs[j], gvecs[k])
            if udiff > maxSim: maxSim = udiff; idx = k
            if gdiff > maxSim: maxSim = gdiff; idx = k

        if maxSim < 0.9 and len(firstSet1) < 10:
            print("Non-Intersection: %-30s %.7f" % (w,maxSim))
            firstSet1.add(j)
            diffSet.add(j)
        #else:
        #    print("Reject:           %-30s %.7f" % (w,maxSim))

        if len(firstSet1) == 10: break

    ### Urteile near, but not German
    for w in un:
        j = wortliste.index(w)
        maxSim = -1
        idx = 0
        for k in diffSet:
            udiff = cosine_similarity(uvecs[j], uvecs[k])
            gdiff = cosine_similarity(gvecs[j], gvecs[k])
            if udiff > maxSim: maxSim = udiff; idx = k
            if gdiff > maxSim: maxSim = gdiff; idx = k

        if maxSim < 0.9 and len(firstSet2) < 10:
            print("Non-Intersection: %-30s %.7f" % (w,maxSim))
            firstSet2.add(j)
            diffSet.add(j)
        #else:
        #    print("Reject:           %-30s %.7f" % (w,maxSim))

        if len(firstSet2) == 10: break


    toAdd = list(diffSet)
    for w in toAdd:
        #diffSet.add(w)
        #nearSet.add(w)

        for ww in getWordDef(w,4,4):
            diffSet.add(ww)


    diffSet.add(i)
    nearSet.add(i)
    return (diffSet,firstSet1,firstSet2,nearSet)






time_start = time.time()
i = 0
for word in plotSet:
    i+=1
    print("\n\n\n\n\n\n\n===============================================================\n%s" % word)
    mainI = wortliste.index(word)

    #if os.path.isfile('plots/plot-'+word+'-urteile-tsne.png'): continue

    (plotSet,plotFirst1,plotFirst2,plotNear) = handleWord(mainI)
    
    plotList = [wortliste[i] for i in plotSet]
    plotHighlight2 = set([wortliste[i] for i in plotFirst1])
    plotHighlight3 = set([wortliste[i] for i in plotFirst2])
    plotHighlight1 = set([wortliste[i] for i in plotNear])
    
    tsne_data = tsne(plotList, 'urteile')
    plotDataset(tsne_data,mainI,plotHighlight1,plotHighlight2,plotHighlight3,'tsne1','tsne2','plot-'+word+'-urteile-tsne.png')
    plotDataset(tsne_data,mainI,plotHighlight1,plotHighlight2,plotHighlight3,'dim0','dim1','plot-'+word+'-urteile-pca.png')
    tsne_data = tsne(plotList, 'german')
    plotDataset(tsne_data,mainI,plotHighlight1,plotHighlight2,plotHighlight3,'tsne1','tsne2','plot-'+word+'-german-tsne.png')
    plotDataset(tsne_data,mainI,plotHighlight1,plotHighlight2,plotHighlight3,'dim0','dim1','plot-'+word+'-german-pca.png')


    curTime = time.time()-time_start
    eta = int(curTime/i * len(plotSet))
    print('In Round %3d : %d min %d sec ETA %d h %d min %d sec' % (i,int(curTime/60), int(curTime) % 60, int(eta/3600), int((eta % 3600)/60), int(eta % 60)))

### blue =   near in german,  not in Urteile
### orange = near in urteile, not in german
## green = near in both
