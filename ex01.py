# Libraries
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
 
# Data set
url = R'C:\Users\zgj_t\Desktop\SummerCourse\word_mat.csv'
df = pd.read_csv(url)
varieties=['艺术', '教育', '学校', '高校', '体育', '工作', '发展', '学生', '课程', '教学']

# Calculate the distance between each sample
Z = linkage(df, 'ward')
print(Z)
# Make the dendrogram
dendrogram(Z, labels=varieties, leaf_rotation=0, color_threshold=240, above_threshold_color='grey')
 
# Create a color palette with 3 colors for the 3 cyl possibilities
my_palette = plt.cm.get_cmap("Accent", 3)
 
 
# Apply the right color to each label
ax = plt.gca()
xlbls = ax.get_ymajorticklabels()
num=-1
for lbl in xlbls:
    num+=1
    lbl.set_color(my_palette(1))

# Show the graph
plt.show()