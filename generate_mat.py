import os
root_path = R'C:\Users\zgj_t\Desktop\SummerCourse'
root_path_local = R'C:\Users\zgj_t\Desktop\SummerCourse\北大法宝地方法规库批量下载2021.08.21. 12.05.11'
root_path_center = R'C:\Users\zgj_t\Desktop\SummerCourse\北大法宝中央法规库批量下载2021.08.21. 12.07.31' 
root_path_local_list = os.listdir(root_path_local)
root_path_center_list = os.listdir(root_path_center)

import numpy as np
path_name_pairs = [[root_path_center, root_path_center_list]]
num_keywords = 15
num_papers = len(root_path_center_list)
excludes = {} # 定义例外的词

import jieba
def solve(path_name_pairs):
    full_word_list = []
    for pair in path_name_pairs:
        root_path = pair[0]
        name_list = pair[1]
        for name in name_list:
            txt_name = name
            txt_path = os.path.join(root_path, txt_name)
            txt = open(txt_path, "r", encoding='utf-8').read()
            words = jieba.lcut(txt)
            full_word_list.append(words)

    counts = {}
    for words in full_word_list:
        for word in words:
            if len(word) == 1 or (word in excludes):  # 排除单个字符的分词结果
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    freq_dict = {}
    word_list = []
    for i in range(num_keywords*10):
        word, count = items[i]
        word_list.append(word)
        freq_dict[word] = count
        # print("{:*<10}{:->5}".format(word, count))
    return full_word_list, freq_dict, word_list

full_word_list, f, w = solve(path_name_pairs)
words_dict_list = []
for words in full_word_list:
    single_counts = {}
    for word in words:
        if len(word) == 1 or (word in excludes):  # 排除单个字符的分词结果
            continue
        else:
            single_counts[word] = single_counts.get(word, 0) + 1
    words_dict_list.append(single_counts)
len(words_dict_list)

key_words_list = w[:num_keywords]

word_mat = np.zeros((num_keywords, num_papers))
for i in range(num_papers):
    tem_word_dict = words_dict_list[i]
    for j, keyword in enumerate(key_words_list):
        if keyword in tem_word_dict.keys():
            word_mat[j, i] = tem_word_dict[keyword]

np.savetxt('word_mat.csv', word_mat,delimiter=',')