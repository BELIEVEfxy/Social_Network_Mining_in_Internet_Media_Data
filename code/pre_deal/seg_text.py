import re
import codecs
import jieba.posseg as pseg

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
stop_word = 'stop.dat'
stopword = codecs.open(stop_word, 'r', encoding='utf-8').readlines()
stopword = [w.strip() for w in stopword]

if __name__ == '__main__':
    
    news = open("news.txt", 'r', encoding='UTF-8')
    res = open('res.txt', 'w', encoding='UTF-8')
    
    i = 0
    for line in news:
        i = i + 1
        line_dict = eval(line)
        if zh_pattern.search(line_dict['content']):
            words = pseg.cut(line_dict['content'])
            name = []
            for word, flag in words:
                if flag == 'nr' and 1 < len(word) < 4 and word not in stopword:
                    name.append(word)
            name = set(name)
            if len(name) > 1:
                print(name, file=res)
