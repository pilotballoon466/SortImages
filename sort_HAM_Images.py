import os

PATH = ""
IMAGE_DIR = PATH + "/HAM10000_images"
JSON_DIR = PATH + "/HAM10000_metadata.csv"
BENIGN_IMAGES = PATH + "/SortedData/Benign"
MALIGNANT_IMAGES = PATH + "/SortedData/Malignant"
INDETERMINATE_IMAGES = PATH + "/SortedData/Indeterminate"
NULL_VALUE_IMAGES = PATH + "/SortedData/Null_Values"

def sortImage(diagnosis, imageFileName):
    if diagnosis == "nv":
        try:
            filePath = IMAGE_DIR + "/" +  imageFileName + ".jpg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  imageFileName + ".jpg", BENIGN_IMAGES + "/" + imageFileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  imageFileName + ".jpg")
                print("To:\t" + BENIGN_IMAGES + "/" + imageFileName + ".jpeg")
            #else:
                #print("ERROR: " + imageFileName)
        except Exception as err:
            print(err)
    elif diagnosis == "mel":
        try:
            filePath = IMAGE_DIR + "/" +  imageFileName + ".jpg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  imageFileName + ".jpg", MALIGNANT_IMAGES + "/" + imageFileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  imageFileName + ".jpg")
                print("To:\t" + MALIGNANT_IMAGES + "/" + imageFileName + ".jpeg")
            #else:
                #print("ERROR: " + imageFileName)
        except Exception as err:
            print(err)


def loadCsv():
    try:
        csv={}
        csv = open(JSON_DIR)
        return csv
    except Exception as err:
        print(err)
        return False



def main():
    csvData = loadCsv()

    counter = 0
    difDiag=["nv", "mel"]

    for line in csvData:
        lineArray = line.split(",")

        if lineArray[2] in difDiag:
            sortImage(lineArray[2], lineArray[1])

        

    print("Sorting process ended!")
    


if __name__ == "__main__":
    main()
