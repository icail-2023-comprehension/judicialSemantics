## Welcome to Judicial Semantics!

This website contains a practical tool for understanding and comparing the semantics of standard and technical legal language for the German legal system.


### Word2Vec Models

We have trained two word2vec Models -- one for standard and one for legal german language.

- standard german: [model](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.vector) and [numpy file](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.vector.vectors.npy)
- legal german: [model](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.vector) and [numpy file](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.vector.vectors.npy)

Note that you need **both** the model and the numpy files to load the model.

### Semantics of a Single Word

For understanding the differnce in semantics of a single word, we generate two plots: one depicting the semantics of the word in standard german an one in legal german.

You can download the script for generating these plots [here](https://github.com/ictai1672/judicialSemantics/blob/main/single-word.py).

To run the script, you need to download both the standard and legal word2vec model as well as the two folloing files: [file1](https://github.com/ictai1672/judicialSemantics/blob/main/urteile.counter) and [file2](https://github.com/ictai1672/judicialSemantics/blob/main/deutsch.counter) (containing the word count for each word in both corpora).
All these files must be in the same folder as the ``single-word.py``

To generate a plot for a word, simply call ``python single-word.py word``. Note that running the script even for one single word might take some time.
The script also supports generating plots for multiple words at the same time (which might save time). If you wish to generate plots for multiple words, simply call the script with multiple arguments (i.e. ``python single-word.py word1 word2 word3``).

The script will generate multiple png files: four for each word, named ``plot-WORD-german-pca.png``, ``plot-WORD-urteile-pca.png``, ``plot-WORD-german-tsne.png``, and ``plot-WORD-urteile-tsne.png``. The files named ``german`` are the plots for the standard language while ``urteile`` are the ones for the technical legal language.



### Semantics of Word Pairs
We also offer to investigate the relative difference of two words in both model. This is inteded for cases where two words have a similar semantics in one, but a different semantics in the other two models.

You can download the script for generating these plots [here](https://github.com/ictai1672/judicialSemantics/blob/main/word-pair.py).

The setup of this script is as for the script for single words.

To run the script you need to provide two words that should be plotted w.r.t. each other. As for the single-word-script, you can also invoke this scirpt with a longer list of words. In this case the script will interpret them as a list of pairs.

The generated files are again pngs and contain both words in their file names.

## Examples

### Single Words

![Sicherung vorbereiten](https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ablehnen-german-pca.png?raw=true)
