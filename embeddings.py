import fasttext

def extract_embeddings(dataframe, emoji_list):

    embedding_list = []
    dataframe['Text'].to_csv('corpus.txt', index=False, header=False, encoding='utf-8')
    model = fasttext.train_unsupervised('corpus.txt', model='cbow')
    for emoji in emoji_list:
        embedding_list.append((emoji, model[emoji]))

    return embedding_list
