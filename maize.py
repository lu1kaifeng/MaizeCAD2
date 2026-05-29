import pyreadr as readr
from matplotlib import pyplot as plt

'''chr1 = readr.read_r(r'Bian/Parents26_chr1.RData')
chr1 = chr1['temp']
chr1.to_csv(r'Bian/Parents26_chr1.csv')
NAMGLS = readr.read_r(r'Bian/NAMGLS.RData')
NAMGLS = NAMGLS['NAMGLS']
NAMGLS.to_csv(r'Bian/NAMGLS.csv')'''
rel = readr.read_r(r'Bian/relMat.RData')
rel = rel['NAM']
rel
relMat = rel.to_numpy()
x = list(rel.columns)
y= list(rel.index)

fig,ax = plt.subplots()
im = ax.imshow(relMat)

'''ax.set_xticks(range(len(x)), labels=x,
              rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(range(len(y)), labels=y)'''

fig.tight_layout()
plt.show()