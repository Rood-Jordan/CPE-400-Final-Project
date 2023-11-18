# CPE 400 Final Project Analysis Script
# Jordan Rood and Sofia Gratny

# import package to run system calls
import os

dataDir = "../Data"
dataAnalysisDir = "../Data-Analysis"

# if directory already exists, remove directory for reanalysis
if(os.path.exists(os.path.join(os.getcwd(), dataAnalysisDir))):
    os.rmdir(dataAnalysisDir)

# make Data Analysis directory to store *.csv files in
os.mkdir(dataAnalysisDir)

# loop through tshark calls for analysis and export of data to Data Analysis directory - calls for all data collections
for x in range(1, 11):
    # construct input and output filename
    infilename = "collection-" + str(x) + ".pcapng"
    outfilename = "analysis-" + str(x) + ".csv"

    print("dataDirPath ", os.path.join(dataDir, infilename))

    # construct tshark command
    cmd = "tshark -r " + os.path.join(dataDir, infilename) + " -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -E header=y -E separator=,  > " + os.path.join(dataAnalysisDir, outfilename)
    
    print(cmd)
    # make command call
    os.system(cmd)

# Example tshark call
# "tshark -r ../Data/Iphone-Data-Capture.pcapng -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -E header=y -E separator=,  > ../Data-Analysis/test.xlsx"