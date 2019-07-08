def strip_e(st):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', st)

def make_data(fnames):
    import tarfile
    import os
    import codecs
    import json
    import re
    from collections import Counter
    tmp = 'temp'
    root = "TwitterSampled2"

    fpath = os.path.join(root,fname)
    ffiles = os.listdir(fpath)
    for ffname in ffiles:
        fullpath = os.path.join(fpath, ffname)
        tar = tarfile.open(fullpath, "r:gz")
        tar.extractall(tmp)
        tar.close()
        fullpath = os.path.join(tmp, "%s.txt" % ffname.split(".")[0])
        f = codecs.open(fullpath, 'r', encoding="utf-8")
        total = Counter()
        for i,line in enumerate(f.readlines()):
            print(i , ffname)
            try:
                tweet = json.loads(line)
                text = tweet['text']
                text = strip_e(text)
                rep = re.sub("RT @[A-z0-9]{2,}:", '', text)
                rep = re.sub("@[A-z0-9_]{2,} ", '', rep)
                rep = re.sub("http://[A-z0-9/.]{2,}", '', rep)
                rep = re.sub("[ㄱ-ㅎㅏ-ㅣ]", '', rep)
                token = ko.nouns(rep)
                total += Counter(token)
            except:
                print("error")
        f.close()
        os.remove(fullpath)
        ok = {'date': ffname[:8], 'data': dict(total)}
        with open('words.json', 'a', encoding='utf-8') as make_json:
            json.dump(ok, make_json, ensure_ascii=False)
            make_json.write('\n')

if __name__ == '__main__':
    import tarfile
    import os
    import codecs
    import json
    from konlpy.tag import Komoran
    import re
    from collections import Counter

    ko = Komoran()
    tmp = "temp"
    root = "TwitterSampled2"
    from multiprocessing import Process
    import numpy as np
    from threading import Thread

    files = os.listdir(root)
    # fname = files[1]
    #make_json = open('words.json', 'w', encoding='utf-8')
    #make_json = open('word2.json', 'w', encoding='utf-8')
    for fname in files[12:24]:
        make_data(fname)

