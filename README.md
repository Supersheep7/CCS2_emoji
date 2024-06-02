# Repository containing experiments, datasets and model for CCS2 Exam

## Repo structure:

* Dataset -> Contains all the used tweets 
* Legacy -> Contains old stuff, can be ignored
* Public -> Contains all used images
* corpus.txt -> All the tweets from original dataset in a single .txt
* data.json -> Gold data from MultiEmo60 survey
* dictionary-full.json -> Last saved dictionary for the full model
* dictionary-text-1.json -> This dictionary is used to store the extracted features from different models during the experiment
* embeddings.py -> Helper function for experiments.ipynb
* experiments.ipynb -> Notebook for emoji embedding extraction through fasttext
* image-experiments.ipynb -> Notebook for latent representation extraction through an autoencoder
* lookup.json/lookup.py -> First incarnation of our emoji dictionary
* multi-tsne.jpg/textual-tsne.jpg/visual-tsne.jpg -> Saved plots for each t-SNE
* multiemo60.csv -> csv with all data collected through our experiment
* multimodel.ipynb -> Notebook for multimodal vector extraction, computation of t-SNE plots, quantitative evaluation, etc
* sample_analysis.ipynb -> Notebook for analysis of our experiment's results

## Instruction to replicate the experiments

1. Ensure that all libraries are installed in the environment and that all datasets are correctly in place in the repository. 
2. Run all cells from experiments.ipynb to process the twitter dataset and train fasttext for extracting our dictionary's embeddings. The results will be stored in dictionary-text-1.json
3. Run all cells from image-experiments.ipynb to train the autoencoder on the emoji image dataset and extracting our latent representations. The results will be added to dictionary-text-1.json
4. Run all cells from multimodel.ipynb. The quantitative evaluation and t-SNE scatterplots will be shown in the cells of that notebook. 
5. If you want to analyze the data collected through MultiEmo60 experiment, run the cells from sample_analysis.ipynb to have access to the data in dataframe form. 

For any further information feel free to contact me at lqv142@alumni.ku.dk

