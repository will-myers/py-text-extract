# importing required modules
from PyPDF2 import PdfReader
import sys
import os.path

if (len(sys.argv) < 3):
    print("Please provide an input file path and an output directory")
    sys.exit()

# Get the file path
filepath = sys.argv[1]

# Get the output directory
outputDir = sys.argv[2]

print(filepath)
print(outputDir)

# Get the pages to exclude (if any)
exclusions = []
if (len(sys.argv) == 4):
    print("Exclusions provided")
    exclusionList = sys.argv[3].split(",")
    for exclusion in exclusionList:
        # Check if it is a range of pages
        if (exclusion.find("-") != -1):
            exRange = exclusion.split("-")
            for i in range(int(exRange[0]), int(exRange[1]) + 1):
                exclusions.append(i)
        else:
            exclusions.append(int(exclusion))

print(exclusions)

# Check if file exists
if (not os.path.isfile(filepath)):
    print("File not found")
    sys.exit()

# Check if output directory exists
if (not os.path.isdir(outputDir)):
    # Create the directory
    os.makedirs(outputDir)

print("Extracting text from " + filepath)

# creating a pdf reader object
reader = PdfReader(filepath)

for i in range(len(reader.pages)):
    # Get the page number
    pageNum = i + 1

    # Check if the page is excluded
    if (pageNum in exclusions):
        continue
    
    # Get the page
    page = reader.pages[i]

    # Extract the text
    text = page.extract_text()

    # Output file name
    outputFileName = outputDir + "/page_" + str(pageNum) + ".txt"

    # Create the output file
    with open(outputFileName, "w") as output_file:
        output_file.write(text)
        print("Created file: " + outputFileName)
    
print("Done")