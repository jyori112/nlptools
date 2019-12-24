import sys
from pathlib import PosixPath

import numpy as np
from gensim.models import KeyedVectors, Vocab

class Embedding(KeyedVectors):
    def __init__(self, index2word, vectors):
        self.index2word = index2word
        self.vectors = vectors

        # initialize gensim keyedvectors
        super().__init__(vectors.shape[1])

        # set vocab
        self.vocab = {word: Vocab(index=idx) for idx, word in enumerate(index2word)}

    def save_text(self, fp):
        if isinstance(fp, (str, PosixPath)):
            with open(fp, 'w') as f:
                return self.save(f)

        print(f"{len(self)} {self.vector_size}", file=fp)

        for word in self:
            vec = self[word]
            vec_str = ' '.join('{:.6f}'.format(float(v)) for v in vec)
            print(f'{word} {vec_str}', file=fp)

    def write_text(self):
        self.save(sys.stdin)

    @staticmethod
    def load(fp, vocabsize=None):
        if isinstance(fp, (str, PosixPath)):
            with open(fp) as f:
                return Embedding.load(f, vocabsize=vocabsize)

        # Read header
        _vocabsize, dim = map(int, fp.readline().strip().split())

        if vocabsize is None:
            vocabsize = _vocabsize

        index2word = []
        vectors = np.empty((vocabsize, dim), dtype=np.float32)

        for idx, line in enumerate(fp):
            word, vec_str = line.strip().split(' ', 1)
            index2word.append(word)
            vectors[idx] = np.fromstring(vec_str, sep=' ')

        return Embedding(index2word, vectors)
