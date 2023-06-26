import os
import ExtractData
import getZipFiles
import ExtractData
import Createcsv
import Extractjson

def Main(TestDataSet):
    directory = os.path.dirname(os.path.abspath(__file__)) + "\\" + TestDataSet

    # List all files in the directory
    file_names = os.listdir(directory)

    # Iterate over each file in the directory
    for file in file_names:
        # Call the getZipFiles function to extract the zip files from the PDFs
        getZipFiles.getZipFiles("\\" + TestDataSet + "\\" + file, file[:-4] + ".zip")

    # Extract the JSON files from the zipped files
    Extractjson.Extractjson()

    # Update the directory path to the jsonoutput folder
    directory = os.path.dirname(directory) + "\\" + "jsonoutput"

    # List all files in the jsonoutput folder
    files = os.listdir(directory)

    data = []

    # Iterate over each file in the jsonoutput folder
    for dir in files:
        try:
            # Call the ExtractData function to extract relevant data from the structuredData.json file
            data.extend(ExtractData.ExtractData(directory + "\\" + dir + "\\" + "structuredData.json"))
            print(dir + " Extracted Successfully!")
        except:
            print("Error in file " + dir)
            continue

    # Call the Createcsv function to create a CSV file with the extracted data
    Createcsv.Createcsv(data)


# Call the Main function with the name of the TestDataSet directory
Main("TestDataSet")
