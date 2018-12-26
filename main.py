from __future__ import division

import torch, torchtext
import table

# load data
train = torch.load('train.pt')
valid = torch.load('valid.pt')

fields = table.IO.TableDataset.load_fields(
        torch.load('vocab.pt'))
fields = dict([(k, f) for (k, f) in fields.items()
               if k in train.examples[0].__dict__])
train.fields = fields
valid.fields = fields

train_iter = table.IO.OrderedIterator(
    dataset=train, batch_size=200, device=-1, repeat=False)
valid_iter = table.IO.OrderedIterator(
    dataset=valid, batch_size=200, device=-1, train=False, sort=True, sort_within_batch=False)
print("Data loaded!")

# Init glove
word_dict = fields['src'].vocab
word_padding_idx = word_dict.stoi[table.IO.PAD_WORD]
num_word = len(word_dict)
vectors = torchtext.vocab.GloVe(dim=300)
word_dict.load_vectors(vectors)
print("Glove initialized!")

for batch in train_iter:
    pass

for batch in valid_iter:
    pass

