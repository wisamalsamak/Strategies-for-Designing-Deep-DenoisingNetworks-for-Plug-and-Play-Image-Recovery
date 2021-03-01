# I2DL Project

## Content

[Train a denoiser model](#train-a-denoiser-model) <br/>
[Use pretrained denoiser model](#use-pretrained-denoiser-model) <br/>

## Train a denoiser model

1) Download the BSDS500 dataset from https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/ and the Waterloo exploration dataset from https://ece.uwaterloo.ca/~k29ma/exploration/ . 
2) Use script in **Supplementary/bmptojpg.py** to convert the BMP images in the Waterloo dataset to JPG.
3) Combine all 500 images from the BSDS500 dataset and 1500 images from the Waterloo exploration dataset into one folder and upload the folder to Google Drive. Rename the folder to 'train' and create an empty folder called 'val'.
4) Change data_path in Plug_and_Play.ipynb



## Use pretrained denoiser model

1) Download one of the pretrained models provided in **Supplementary/Pretrained_Models**
2) Change data_path in Plug_and_Play.ipynb
3) Comment out the last four lines in this cell

![](images/Load_NN_Model.png.png?raw=true "Load_NN_Model")
