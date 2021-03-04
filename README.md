# I2DL Project

## Content

[Training a denoiser model](#training-a-denoiser-model) <br/>
[Use pretrained denoiser model](#use-pretrained-denoiser-model) <br/>

## Training a denoiser model
**Note**: the following steps show you how to train a PnP CNN denoiser using the provided **Plug_and_Play.ipynb** notebook. You can use the same notebook to train the PnP U-net or PnP Gan Denoisers by changing the model class

1) Download the BSDS500 dataset from https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/ , the Waterloo exploration dataset from https://ece.uwaterloo.ca/~k29ma/exploration/ , and the ground truth test images of 'Parrot', 'Monarch', and 'Lena' in **images/test_images**. 
2) Use script in **Supplementary/bmptojpg.py** to convert the BMP images in the Waterloo dataset to JPG.
3) Combine all 500 images from the BSDS500 dataset and 1500 images from the Waterloo exploration dataset into one folder and upload the folder to Google Drive into a subfolder.  Rename the folder to 'train'. Repeat the process with some of other images to create an validation set folder 'val'. Upload the test images to the same path where your 'train' and 'val' folders are in. The folder structure should look like this:
![](images/folder_structure.png?raw=true)
4) Change data_path in 'Plug_and_Play.ipynb' to the folder that contains your 'train' and 'val' folders.
5) Change network model class (if you want). Note that the output image should have the same size as the input image.
![](images/nn_class.png?raw=true)
6) Specify training settings and train your model.
![](images/specify_training_settings.png?raw=true) 

7) Test the denoising performance on a sample of the validation set by using
```python
denoising_performance('val_set')
```
8) Test the PnP denoiser performance by using
```python
pnp('parrot')                       # 'parrot', 'monarch', 'lena'
```

## Use pretrained PnP denoiser model

1) Download one of the pretrained models provided in **Supplementary/Pretrained_Models** and the ground truth test images of 'Parrot', 'Monarch', and 'Lena' in **images/test_images**.
2) Upload the pretrained model and the test images into a Google Drive folder.
3) Change data_path in 'Plug_and_Play.ipynb' to the Google Drive folder which contains the test images.
4) Copy and paste the model class provided as a .txt with each pretrained denoiser model into the 'Network model class' cell.
5) Uncomment the last four lines in this cell and replace the path in checkpoint with the path where you uploaded your pretrained model
![](images/Load_NN_Model.png?raw=true)
```python
checkpoint = torch.load('./drive/MyDrive/your_path/denoiser_name.pth')
```
6) Skip the 'Network training' cell
7) Test the denoising performance by using
```python
denoising_performance('parrot')     # 'parrot', 'monarch', 'lena'
```
8) Test the PnP denoiser performance by using
```python
pnp('parrot')                       # 'parrot', 'monarch', 'lena'
``` 

