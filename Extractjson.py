import os
import zipfile


def Extractjson():
    # Specify the directory where the zipped files are located
    directory = os.path.dirname(os.path.abspath(__file__)) + "\zippedjsonoutput"

    # List all files in the directory
    file_names = os.listdir(directory)

    # Iterate over each file in the directory
    for file in file_names:
        zip_path = directory + "\\" + file

        # Open the zip file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # Extract all files in the zip file
            # Extract the files into a folder named after the zip file (without the .zip extension)
            zip_ref.extractall(os.path.dirname(directory) + "\jsonoutput" + "\\" + file[0:-4])
