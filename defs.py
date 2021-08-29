from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from generate_mat import *
word_mat = np.genfromtxt('word_mat.csv', delimiter=',', dtype=None)
samples = np.array(word_mat)
varieties= key_words_list
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

def hierarchy_analysis(samples,method='single'):
    mergings = linkage(samples, method=method)

    dendrogram(mergings,
              labels=varieties,
              leaf_rotation=0,
              leaf_font_size=10)
    plt.title(method)
    plt.savefig('cluster_fig/'+method+'.png')
    plt.show()
# import matplotlib as mpl
# from matplotlib.pyplot import cm
# from scipy.cluster import hierarchy

# cmap = cm.rainbow(np.linspace(0.5, 1, 1000))
# hierarchy.set_link_color_palette([mpl.colors.rgb2hex(rgb[:3]) for rgb in cmap])
 
# Create a color palette with 3 colors for the 3 cyl possibilities
my_palette = plt.cm.get_cmap("Accent", 3)
 
print(my_palette)


single_method = hierarchy_analysis(samples,method='single')
complete_method = hierarchy_analysis(samples,method='complete')
average_method = hierarchy_analysis(samples,method='average')
# hierarchy_analysis(samples,method='centroid')
# hierarchy_analysis(samples,method='median')
ward_method = hierarchy_analysis(samples,method='ward')
# hierarchy_analysis(samples,method='weighted')


