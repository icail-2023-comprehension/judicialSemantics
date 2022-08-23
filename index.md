## Welcome to Judicial Semantics!

This website contains a practical tool for understanding and comparing the semantics of standard and technical legal language for the German legal system.


### Word2Vec Models

We have trained two word2vec Models -- one for standard and one for legal german language.

- standard german: [download model](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.vector) [download numpy file](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.vector.vectors.npy)
- legal german: [download model](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.vector) [download numpy file](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.vector.vectors.npy)

Note that you need **both** the model and the numpy files to load the model.

### Semantics of a Single Word

For understanding the differnce in semantics of a single word, we generate two plots: one depicting the semantics of the word in standard german an one in legal german.

You can download the script for generating these plots [here]().

To run the script, you need to download both the standard and legal word2vec model as well as the two folloing files: [file1](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.counter) and [file2](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.counter) (containing the word count for each word in both corpora).
All these files must be in the same folder as the ``single-word.py``

To generate a plot for a word, simply call ``python single-word.py word``
