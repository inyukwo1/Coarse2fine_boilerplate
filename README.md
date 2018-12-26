# CoarseToFineBoilerplate

This is a boilerplate for implementing CoarseToFine. (L Dong, Coarse-to-Fine Decoding for Neural Semantic Parsing, 2018 https://arxiv.org/pdf/1805.04793.pdf)
Implementing CoarseToFine aims to practice pytorch and NLP.

## How to do it

1. Read CoarseToFine paper carefully (https://arxiv.org/pdf/1805.04793.pdf).
2. Download python3.5 (https://www.python.org/downloads/release/python-352/). This project only can be run at python 3.5.
3. Make virtualenv (example shell commands are in below).
4. Install requirements (example shell commands are in below).
5. See main.py and see how to load dataset. I recommend you to run train.py first and see how ```batch``` looks like in line 32 and 35.
6. Implement remainings. You also need to implement accuracy metrics and your model's accuracy have to be comparable with the paper's result. 

<pre><code>
$ virtualenv --python=python3.5 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python main.py
</code> </pre>


If there are questions or suggestions, ask Inhyuk Na(ina@dblab.postech.ac.kr).

## TroubleShooting

If you meet some kind of ```~~ zip error ~~``` but you don't have any idea, try to run ```rm -rf .vector_cache/```