import os


def getWords(filePath):
    words=[]
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words

if __name__=='__main__':
    path=os.getcwd()+os.path.sep+'filter_words.txt'
    words=getWords(path)
    print(str(len(words)),words)
    text=input('please input text: ').strip()
    if text in words:
        print("*")
    else:
        print(text)
