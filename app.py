import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split


def create_dataframe(path_dataset: str, svae_csv_file: str):
    files = ['Normal', 'COVID', 'Lung_Opacity','Viral Pneumonia']
    path = path_dataset
    data_dir = os.path.join(path)

    data = []
    for id, level in enumerate(files):
        for file in os.listdir(os.path.join(data_dir, level+'/')):
            data.append([level + '/' + file, level])


    data = pd.DataFrame(data, columns = ['image_file', 'labels'])

    data['path'] = path + '/' +data['image_file']
    data['labels'] = data['labels'].map({'Normal': 'Normal',
                                        'COVID': 'COVID',
                                        'Lung_Opacity': 'Lung_Opacity',
                                        'Viral Pneumonia': 'Viral_Pneumonia'})

    data.to_csv(svae_csv_file, index=False)


def split_dataset(path_dataframe: str, ):
    # read csv file
    data = pd.read_csv(path_dataframe)
    
    # split data
    df_train, temp = train_test_split(data, test_size=0.2, stratify=data.labels, random_state=42)
    df_test, df_valid = train_test_split(temp, test_size=0.5, stratify=temp.labels, random_state=42)

    # save csv file
    df_train.to_csv('./train_set.csv', index=False)
    df_valid.to_csv('./valid_set.csv', index=False)
    df_test.to_csv('./test_set.csv', index=False)


def move_image(path_csv: str, destination_folder: str):
    
    df = pd.read_csv(path_csv, usecols=['path'])

    # List of image names
    image_paths = set(df.path.values)

    # Source folder paths
    source_folders = ["./dataset/COVID-19_Radiography_Dataset/COVID", "./dataset/COVID-19_Radiography_Dataset/Lung_Opacity",
                    "./dataset/COVID-19_Radiography_Dataset/Normal", "./dataset/COVID-19_Radiography_Dataset/Viral Pneumonia"]

    # Destination folder path
    destination_folder = fr"./{destination_folder}_dataset"
    
    for img in image_paths:

        for folder in source_folders:

            for file in os.listdir(folder):

                if img in os.path.join(folder+'/', file):
                    shutil.move(img, destination_folder)            


# all data
create_dataframe('./dataset/COVID-19_Radiography_Dataset/', './dataset.csv')

# split data
split_dataset('./dataset.csv')

# validation data
move_image('./valid_set.csv', './Validation')

# test data
move_image('./test_set.csv', './Test')