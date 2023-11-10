# 2AMM30-groep-2
This repository contains all the files needed to replicate the results for the assignment, both component 1 and 2.

## Component 1
- Cleaning and filtering of articles is done in `cleaning_nobel_articles_comp1.ipynb`. Output of which can be found in `nobel_data/comp1_nobel_articles_cleaned.json`
- Experimenting with slicing paragraphs is done in `comp1_cutting_paragraphs.ipynb`, output of which is found in `nobel_data/nobel_articles_4pars.json`
- A list of all winners can be found in `nobel_data/laureates.json`

## Component 2
- Preprocessing of the reports is done in `cleaning_comp2.ipynb`

## Labeled data
Labeled output from Label Studio can be found in `/data/`, with train and test data separated, as well as per component.


## Results
The resulting triplets can be found in `component1_triplets.json` and `component2_triplets.json` respectively.

## Replicating our training
To run the code used for fine-tuning the models:
- Open the `Flairmodel.ipynb` in Colab
- Upload the contents of the `data` folder to your Colab workspace
- Run the cells under `Prerequisites`
- Run either the `Component 1` or `Component 2` cells

