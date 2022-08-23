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
#### ablehnen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ablehnen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ablehnen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ablehnen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ablehnen-urteile-tsne.png?raw=true" width="500">
#### abstandnahme
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstandnahme-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstandnahme-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstandnahme-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstandnahme-urteile-tsne.png?raw=true" width="500">
#### abstellen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstellen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstellen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstellen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abstellen-urteile-tsne.png?raw=true" width="500">
#### abweisend
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abweisend-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abweisend-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abweisend-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-abweisend-urteile-tsne.png?raw=true" width="500">
#### angeben
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angeben-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angeben-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angeben-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angeben-urteile-tsne.png?raw=true" width="500">
#### anstrengen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-anstrengen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-anstrengen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-anstrengen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-anstrengen-urteile-tsne.png?raw=true" width="500">
#### antragssteller
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-antragssteller-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-antragssteller-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-antragssteller-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-antragssteller-urteile-tsne.png?raw=true" width="500">
#### auffordern
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-auffordern-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-auffordern-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-auffordern-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-auffordern-urteile-tsne.png?raw=true" width="500">
#### ausweislich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ausweislich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ausweislich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ausweislich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ausweislich-urteile-tsne.png?raw=true" width="500">
#### beabsichtigen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beabsichtigen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beabsichtigen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beabsichtigen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beabsichtigen-urteile-tsne.png?raw=true" width="500">
#### beauftragt
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beauftragt-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beauftragt-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beauftragt-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beauftragt-urteile-tsne.png?raw=true" width="500">
#### befragt
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befragt-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befragt-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befragt-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befragt-urteile-tsne.png?raw=true" width="500">
#### befristungsvereinbarung
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befristungsvereinbarung-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befristungsvereinbarung-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befristungsvereinbarung-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-befristungsvereinbarung-urteile-tsne.png?raw=true" width="500">
#### behauptet
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-behauptet-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-behauptet-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-behauptet-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-behauptet-urteile-tsne.png?raw=true" width="500">
#### beibringen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beibringen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beibringen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beibringen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beibringen-urteile-tsne.png?raw=true" width="500">
#### beiladen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beiladen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beiladen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beiladen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beiladen-urteile-tsne.png?raw=true" width="500">
#### beispielsweise
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beispielsweise-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beispielsweise-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beispielsweise-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beispielsweise-urteile-tsne.png?raw=true" width="500">
#### beklagen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beklagen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beklagen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beklagen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beklagen-urteile-tsne.png?raw=true" width="500">
#### berücksichtigen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berücksichtigen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berücksichtigen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berücksichtigen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berücksichtigen-urteile-tsne.png?raw=true" width="500">
#### besitz
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-besitz-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-besitz-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-besitz-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-besitz-urteile-tsne.png?raw=true" width="500">
#### betreffend
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betreffend-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betreffend-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betreffend-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betreffend-urteile-tsne.png?raw=true" width="500">
#### beziehungsweise
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beziehungsweise-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beziehungsweise-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beziehungsweise-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beziehungsweise-urteile-tsne.png?raw=true" width="500">
#### bezüglich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bezüglich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bezüglich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bezüglich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bezüglich-urteile-tsne.png?raw=true" width="500">
#### bürgin
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgin-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgin-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgin-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgin-urteile-tsne.png?raw=true" width="500">
#### dahingehend
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahingehend-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahingehend-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahingehend-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahingehend-urteile-tsne.png?raw=true" width="500">
#### eigentum
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigentum-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigentum-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigentum-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigentum-urteile-tsne.png?raw=true" width="500">
#### einreden
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einreden-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einreden-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einreden-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einreden-urteile-tsne.png?raw=true" width="500">
#### einschliesslich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einschliesslich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einschliesslich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einschliesslich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einschliesslich-urteile-tsne.png?raw=true" width="500">
#### einspruch
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einspruch-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einspruch-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einspruch-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-einspruch-urteile-tsne.png?raw=true" width="500">
#### freispruch
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-freispruch-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-freispruch-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-freispruch-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-freispruch-urteile-tsne.png?raw=true" width="500">
#### frist
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-frist-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-frist-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-frist-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-frist-urteile-tsne.png?raw=true" width="500">
#### gegenwart
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gegenwart-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gegenwart-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gegenwart-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gegenwart-urteile-tsne.png?raw=true" width="500">
#### genehmigen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigen-urteile-tsne.png?raw=true" width="500">
#### genehmigungsfiktion
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigungsfiktion-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigungsfiktion-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigungsfiktion-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-genehmigungsfiktion-urteile-tsne.png?raw=true" width="500">
#### grundsätzlich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-urteile-tsne.png?raw=true" width="500">
#### gutachten
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachten-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachten-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachten-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachten-urteile-tsne.png?raw=true" width="500">
#### gutachter
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachter-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachter-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachter-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-gutachter-urteile-tsne.png?raw=true" width="500">
#### hinsichtlich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-hinsichtlich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-hinsichtlich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-hinsichtlich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-hinsichtlich-urteile-tsne.png?raw=true" width="500">
#### kläger
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kläger-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kläger-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kläger-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kläger-urteile-tsne.png?raw=true" width="500">
#### lohn
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-lohn-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-lohn-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-lohn-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-lohn-urteile-tsne.png?raw=true" width="500">
#### nachlassen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-nachlassen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-nachlassen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-nachlassen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-nachlassen-urteile-tsne.png?raw=true" width="500">
#### ordentlich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ordentlich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ordentlich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ordentlich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-ordentlich-urteile-tsne.png?raw=true" width="500">
#### partei
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-partei-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-partei-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-partei-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-partei-urteile-tsne.png?raw=true" width="500">
#### priorität
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-priorität-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-priorität-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-priorität-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-priorität-urteile-tsne.png?raw=true" width="500">
#### sache
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sache-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sache-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sache-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sache-urteile-tsne.png?raw=true" width="500">
#### sachverständige
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sachverständige-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sachverständige-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sachverständige-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sachverständige-urteile-tsne.png?raw=true" width="500">
#### sicherstellen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sicherstellen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sicherstellen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sicherstellen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-sicherstellen-urteile-tsne.png?raw=true" width="500">
#### streitgegenständlich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-streitgegenständlich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-streitgegenständlich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-streitgegenständlich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-streitgegenständlich-urteile-tsne.png?raw=true" width="500">
#### substanzverletzung
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-substanzverletzung-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-substanzverletzung-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-substanzverletzung-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-substanzverletzung-urteile-tsne.png?raw=true" width="500">
#### üblicherweise
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-üblicherweise-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-üblicherweise-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-üblicherweise-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-üblicherweise-urteile-tsne.png?raw=true" width="500">
#### unstreitig
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-unstreitig-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-unstreitig-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-unstreitig-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-unstreitig-urteile-tsne.png?raw=true" width="500">
#### verfahrensgegenständliche
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfahrensgegenständliche-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfahrensgegenständliche-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfahrensgegenständliche-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfahrensgegenständliche-urteile-tsne.png?raw=true" width="500">
#### verfügungsbeklagte
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfügungsbeklagte-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfügungsbeklagte-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfügungsbeklagte-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verfügungsbeklagte-urteile-tsne.png?raw=true" width="500">
#### vermerken
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vermerken-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vermerken-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vermerken-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vermerken-urteile-tsne.png?raw=true" width="500">
#### verpflichten
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verpflichten-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verpflichten-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verpflichten-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-verpflichten-urteile-tsne.png?raw=true" width="500">
#### vertrag
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertrag-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertrag-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertrag-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertrag-urteile-tsne.png?raw=true" width="500">
#### vorgeschlagen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorgeschlagen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorgeschlagen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorgeschlagen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorgeschlagen-urteile-tsne.png?raw=true" width="500">
#### vorlegen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-urteile-tsne.png?raw=true" width="500">
#### willenserklärung
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-willenserklärung-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-willenserklärung-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-willenserklärung-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-willenserklärung-urteile-tsne.png?raw=true" width="500">
#### zedent
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedent-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedent-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedent-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedent-urteile-tsne.png?raw=true" width="500">
#### zedentin
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedentin-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedentin-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedentin-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zedentin-urteile-tsne.png?raw=true" width="500">
#### zusichern
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zusichern-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zusichern-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zusichern-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-zusichern-urteile-tsne.png?raw=true" width="500">


### Word Pairs
#### angreifen-attackieren
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angreifen-attackieren-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-angreifen-attackieren-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-angreifen-attackieren-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-angreifen-attackieren-urteile-tsne.png?raw=true" width="500">
#### berühmen-weltbekannt
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berühmen-weltbekannt-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-berühmen-weltbekannt-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-berühmen-weltbekannt-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-berühmen-weltbekannt-urteile-tsne.png?raw=true" width="500">
#### beschwerdegegnerin-sachmangel
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beschwerdegegnerin-sachmangel-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-beschwerdegegnerin-sachmangel-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-beschwerdegegnerin-sachmangel-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-beschwerdegegnerin-sachmangel-urteile-tsne.png?raw=true" width="500">
#### betragen-betrügen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betragen-betrügen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-betragen-betrügen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-betragen-betrügen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-betragen-betrügen-urteile-tsne.png?raw=true" width="500">
#### bürgen-bürgin
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgen-bürgin-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-bürgen-bürgin-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgen-bürgin-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-bürgen-bürgin-urteile-tsne.png?raw=true" width="500">
#### bürgschaft-bürgin
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgschaft-bürgin-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-bürgschaft-bürgin-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-bürgschaft-bürgin-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-bürgschaft-bürgin-urteile-tsne.png?raw=true" width="500">
#### dahinstellen-unterscheiden
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahinstellen-unterscheiden-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-dahinstellen-unterscheiden-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-dahinstellen-unterscheiden-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-dahinstellen-unterscheiden-urteile-tsne.png?raw=true" width="500">
#### eigenartig-merkwürdig
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigenartig-merkwürdig-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-eigenartig-merkwürdig-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-eigenartig-merkwürdig-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-eigenartig-merkwürdig-urteile-tsne.png?raw=true" width="500">
#### grundsätzlich-bezüglich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-bezüglich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-grundsätzlich-bezüglich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-grundsätzlich-bezüglich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-grundsätzlich-bezüglich-urteile-tsne.png?raw=true" width="500">
#### kanzler-merkel
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kanzler-merkel-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-kanzler-merkel-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kanzler-merkel-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-kanzler-merkel-urteile-tsne.png?raw=true" width="500">
#### kommend-ziehend
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kommend-ziehend-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-kommend-ziehend-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-kommend-ziehend-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-kommend-ziehend-urteile-tsne.png?raw=true" width="500">
#### mark-zeichen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-mark-zeichen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-mark-zeichen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-mark-zeichen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-mark-zeichen-urteile-tsne.png?raw=true" width="500">
#### offen-unentschieden
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-offen-unentschieden-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-offen-unentschieden-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-offen-unentschieden-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-offen-unentschieden-urteile-tsne.png?raw=true" width="500">
#### übersenden-überreichen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-übersenden-überreichen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-übersenden-überreichen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-übersenden-überreichen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-übersenden-überreichen-urteile-tsne.png?raw=true" width="500">
#### vertreten-repräsentieren
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertreten-repräsentieren-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vertreten-repräsentieren-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vertreten-repräsentieren-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vertreten-repräsentieren-urteile-tsne.png?raw=true" width="500">
#### vorig-vergangen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorig-vergangen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vorig-vergangen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorig-vergangen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vorig-vergangen-urteile-tsne.png?raw=true" width="500">
#### vorlegen-beibringen
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-beibringen-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vorlegen-beibringen-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vorlegen-beibringen-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vorlegen-beibringen-urteile-tsne.png?raw=true" width="500">
#### vortrag-behaupten
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vortrag-behaupten-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vortrag-behaupten-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vortrag-behaupten-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vortrag-behaupten-urteile-tsne.png?raw=true" width="500">
#### vortrag-sachvortrag
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vortrag-sachvortrag-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vortrag-sachvortrag-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-vortrag-sachvortrag-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-vortrag-sachvortrag-urteile-tsne.png?raw=true" width="500">
#### wiedergabe-referieren
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-wiedergabe-referieren-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-wiedergabe-referieren-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-wiedergabe-referieren-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-wiedergabe-referieren-urteile-tsne.png?raw=true" width="500">
#### wirklich-mutmasslich
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-wirklich-mutmasslich-german-pca.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-wirklich-mutmasslich-urteile-pca.png?raw=true" width="500">
<img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots/plot-wirklich-mutmasslich-german-tsne.png?raw=true" width="500"><img src="https://github.com/ictai1672/judicialSemantics/blob/main/plots-pair/plot-wirklich-mutmasslich-urteile-tsne.png?raw=true" width="500">

