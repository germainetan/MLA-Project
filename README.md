# MLA-Project (Group 1)

### equation_dataset 
Contains all of the equation images used to evaluate cnn model

### evaluation_csv
Contains the csv(s) of the evaluated images
- Column Names: path, gt, predicted output, % similarity, WER

### ground_truth_csv
Contains the csv(s) of the ground truth to the equation images
- Column Names: path, gt

### gt_tsv
Contains the tsv(s) of the ground truth to the equation images

### images_compare_with_rcnn
Contains the images used for comparing with rcnn model

### processed_data
Contains the folders that have been processed by the bounding box & cropping function
- Note: each directory have their respective ground_truth_csv

### Drawing bounding box notebook
First Step to preprocess images that stores equation images
> Note: eqn_folder is meant to be replaced so that older folders do not get replaced
- creates directory in the processed_data/<eqn_folder>

### Encoder-decoder notebook
To retrieve the ground truths that are in the folder containing equation images and to store in .csv

### final notebook
Contains CNN Model & Evaluation functions to store evaluated results into evaluation_csv

### final_82
Contains all the individual digits & symbols images used to train CNN model. However, since the folder size is too large it cannot be uploaded to github repo

### train_test_split.py
Splits all the individual digits & symbols images into 90% train and 10% test to be stored in final_82

### Pre-Requisities
Please ensure that you change the folder path for any functions that you will use
- ```pre_processing_from_dir``` : directory consisting your training/test images
- ```pd.read_csv``` : csv file containing your ground truth
- ```pre_processing_from_test``` : folder under processed_data consisting of pre-processed equation images
- ```filtered_data.to_csv``` : change accordingly how you would like your file name to be named

### How to train the CNN model

1. Run all the cells under the subheading "Global Variable", you need to edit these changes before running as they may override previous trained model.
2. Run all the cells under the subheading "Running model on Training Data (Digits & Symbols Images only (17 classes))".

### How to run the CNN model with equation images

1. Make sure you run the model before doing this (model can take a few hours depending on your hyperparameters)
2. images would have to be pre-processed using the ``` Draw bounding box.ipynb ```
3. A folder would then be created and stored under processed_data folder
5. Run all the cells under the subheading "Retrieve Ground Truth from csv".
- <i>Note: Ground Truth has to be in .csv format</i>


