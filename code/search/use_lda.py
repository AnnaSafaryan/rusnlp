import sys
from os import path, listdir
import logging
from gensim import similarities
import gensim
from gensim import corpora
import pickle
sys.path.insert(0, '../database/')
from bd import DBaseRusNLP
from db_reader import ReaderDBase

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

bd_m = DBaseRusNLP(path.join('..', '..', '..', 'database', 'rus_nlp_withouttexts.db'),
                   path.join('..', '..', '..', 'database', 'database_metadata.json'))
reader = ReaderDBase(bd_m)

lemmasfile = sys.argv[1]
modelfile = sys.argv[2]
testdir = sys.argv[3]

with open(lemmasfile, 'rb') as handle:
    all_texts_dict = pickle.load(handle)
order = list(all_texts_dict.keys())

def byName_key(topic):
    return topic[1]


data = list(all_texts_dict.values())
ldamodel = gensim.models.ldamodel.LdaModel.load(modelfile)
dictionary = corpora.Dictionary(data)
dictionary.filter_n_most_frequent(20)
corpus = [dictionary.doc2bow(doc) for doc in data]
index = similarities.MatrixSimilarity(ldamodel[corpus])


with open("result_lda_10.tsv", "w", encoding="utf-8") as wri:
    print('Rank\tTitle\tAuthors\tID\tSimilarity')
    wri.write('Rank\tTitle\tAuthors\tID\tSimilarity\n')
    testfiles = [f.split('.')[0] for f in listdir(testdir) if path.isfile(path.join(testdir, f))]
    for name in testfiles:
        print('==========================\n')
        wri.write('==========================\n')
        wri.write(name+"\n")
        doc = all_texts_dict[name + '.conll']
        
        vec_bow = dictionary.doc2bow(doc)
        vec_lda = ldamodel[vec_bow]
        position = order.index(name + '.conll')
    
        counter = 0
        for sim in index:
            if counter == position:
                sims = sim
                break
            counter += 1
    
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        rank = 0
        for sim in sims[:11]:
            doc = order[sim[0]].split('.')[0]
            print(doc)
            similarity = sim[1]
            authors = reader.select_author_by_id(doc)
            authors = ','.join([w for w in authors])
            title = reader.select_title_by_id(doc)
            if doc == name:
                print('==========================')
                wri.write('==========================\n')
                output = '\t'.join([str(rank), title, authors, doc, str(similarity)])
                print(output)
                wri.write(output+"\n")
                wri.write('==========================\n')
            else:
                output = '\t'.join([str(rank), title, authors, doc, str(similarity)])
                print(output)
                wri.write(output+"\n")
            rank += 1
        print('==========================')
        wri.write('==========================\n')
