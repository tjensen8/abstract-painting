"""
This file makes the dataset to train the machine learning model from.
"""
import numpy as np
from tensorflow.keras.preprocessing.image import DirectoryIterator, ImageDataGenerator
import os

from load_config import load_config

config = load_config()

def iterate_in_directory(directory=None, save_to_dir=None):
    if directory==None:
        print("loading directory from config...")
        print(config['RAW_IMG_DIR'])
        directory = config['RAW_IMG_DIR']
    if save_to_dir==None:
        print("preprocessed images will be saved to (per config)...")
        if config['PREPROCESSED_IMG_DIR']==None:
            print("Images will not be saved to a directory")
        else: print(config['PREPROCESSED_IMG_DIR'])
        save_to_dir = config['PREPROCESSED_IMG_DIR']
    
    idg = ImageDataGenerator(samplewise_center=True)

    """
    directory_iterator = DirectoryIterator(
        directory=directory,
        image_data_generator=idg,
        target_size=(config['IMAGE_PARAMS']['IMAGE_HEIGHT'],config['IMAGE_PARAMS']['IMAGE_WIDTH']),
        classes=None,
        seed=0,
        save_to_dir=save_to_dir
        )
    """
    idg.flow_from_directory(
        directory=directory,
        target_size=(config['IMAGE_PARAMS']['IMAGE_HEIGHT'],config['IMAGE_PARAMS']['IMAGE_WIDTH'])
        )
    return idg

if __name__ == '__main__':
    datagen = iterate_in_directory()