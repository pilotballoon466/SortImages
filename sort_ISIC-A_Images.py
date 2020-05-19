import os
import json as json

PATH = ""
IMAGE_DIR = PATH + "/Images"
JSON_DIR = PATH + "/Descriptions"
BENIGN_IMAGES = PATH + "/SortedData/Benign"
MALIGNANT_IMAGES = PATH + "/SortedData/Malignant"
INDETERMINATE_IMAGES = PATH + "/SortedData/Indeterminate"
NULL_VALUE_IMAGES = PATH + "/SortedData/Null_Values"


def sortImage(benign_malignant, fileName):
    if benign_malignant == "benign":
        try:
            filePath = IMAGE_DIR + "/" +  fileName + ".jpeg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  fileName + ".jpeg", BENIGN_IMAGES + "/" + fileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  fileName + ".jpeg")
                print("To:\t" + BENIGN_IMAGES + "/" + fileName + ".jpeg")
            #else:
                #print("ERROR: " + fileName)
        except Exception as err:
            print(err)

    elif benign_malignant == "malignant":
        try:
            filePath = IMAGE_DIR + "/" +  fileName + ".jpeg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  fileName + ".jpeg", MALIGNANT_IMAGES + "/" + fileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  fileName + ".jpeg")
                print("To:\t" + MALIGNANT_IMAGES + "/" + fileName + ".jpeg")
            #else:
                #print("ERROR: " + fileName)
        except Exception as err:
            print(err)

    elif benign_malignant in ["indeterminate", "indeterminate/malignant", "indeterminate/benign"]:
        try:
            filePath = IMAGE_DIR + "/" +  fileName + ".jpeg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  fileName + ".jpeg", INDETERMINATE_IMAGES + "/" + fileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  fileName + ".jpeg")
                print("To:\t" + INDETERMINATE_IMAGES + "/" + fileName + ".jpeg")
            #else:
                #print("ERROR: " + fileName)
        except Exception as err:
            print(err)

    elif benign_malignant is None:
        try:
            filePath = IMAGE_DIR + "/" +  fileName + ".jpeg"
            if os.path.isfile(filePath):
                os.rename( IMAGE_DIR + "/" +  fileName + ".jpeg", NULL_VALUE_IMAGES + "/" + fileName + ".jpeg")
                print("From:\t" + IMAGE_DIR + "/" +  fileName + ".jpeg")
                print("To:\t" + NULL_VALUE_IMAGES + "/" + fileName + ".jpeg")
            #else:
                #print("ERROR: " + fileName)
        except Exception as err:
            print(err)

def load(filename):
    try:
        data={}
        with open(JSON_DIR + "/" +filename) as tmpFile: 
            data = json.load(tmpFile)
    
        return data
    except Exception as err:
        print(err)
        return False

def main():
    for jsonFile in os.listdir(JSON_DIR):
        data = load(jsonFile)        
        if "meta" in data.keys():
            metaData = data["meta"]
            if "clinical" in metaData.keys():
                clinicalData = metaData["clinical"]
                if "benign_malignant" in clinicalData.keys():
                    if clinicalData["benign_malignant"] in ["benign" , "malignant", "indeterminate", "indeterminate/malignant", "indeterminate/benign"]:
                        #print(jsonFile + ": " + clinicalData["benign_malignant"])
                        sortImage(clinicalData["benign_malignant"], jsonFile)
                    else:
                        if clinicalData["benign_malignant"] is not None: 
                            print(jsonFile + ": clincalData " + clinicalData["benign_malignant"])
                        else:
                            print(jsonFile + ": clincalData is null")
                            sortImage(clinicalData["benign_malignant"], jsonFile)



        data={}

    print("Sorting process ended!")

if __name__ == "__main__":
    main()
