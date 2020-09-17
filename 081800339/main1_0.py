import re# 正则包
import jieba# 自然语言处理包
import jieba.analyse
import sys
import html
# 数据集处理包
from datasketch import MinHash


class MinHashSimilarity(object):
    
    
    def __init__(self, content_x1, content_y2):
        self.orig_1 = content_x1
        self.text_2 = content_y2

        
    def main(self):
        # MinHash计算
        text1, text2 = MinHash(), MinHash()
        # 提取关键词
        orig_1 = self.extract_keyword(self.orig_1)
        text_2 = self.extract_keyword(self.text_2)

        for data in orig_1:
            text1.update(data.encode('utf8'))#字典s1的键/值对更新到m1里面
        for data in text_2:
            text2.update(data.encode('utf8'))#字典s2的键/值对更新到m2里面

        return text2.jaccard(text1)  #返回相似度

    @staticmethod
    def extract_keyword(content):  # 提取关键词
        re_exp = re.compile(r'(<style>.*?</style>)|(<[^>]+>)', re.S)#编译成正则表达式对象
        content = re_exp.sub(' ', content) #使用空格替换所有正则表达式字符串中出现的位置
        content = html.unescape(content)
        # 切割
        words= [i for i in jieba.cut(content, cut_all=True) if i != '']
        # 提取关键词
        keywords = jieba.analyse.extract_tags("|".join(words), topK=250, withWeight=False)
        print(keywords)
        return keywords


if __name__ == '__main__':
    orig, com, ans = sys.argv[1:]
    orig_text=r''+orig
    com_text=r''+com
    ans_text=r''+ans
    with open(orig_text, 'r',encoding='UTF-8') as x, open(com_text, 'r',encoding='UTF-8') as y:
        orig_doc = x.read()
        text_doc = y.read()
        similarity = MinHashSimilarity(orig_doc, text_doc)
        similarity = similarity.main()
        f=open(ans_text,"a")
        f.write(str(round(similarity,2)))
        f.close()       
        print('相似度: %.2f%%' % (similarity*100))

