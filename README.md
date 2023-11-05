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
