# Data Analysis Bash Script
# Run this script from terminal by inputting the command "bash tshark-cmds.sh" in the correct directory

# Make folder for analysis output to be stored in
mkdir ../Data-Analysis

# cd "c:\Program Files\Wireshark"
pwd

# tshark -r ../Data/Iphone-Data-Capture.pcapng -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -w test.csv
# tshark -r ../Data/Iphone-Data-Capture.pcapng -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -E header=y -E separator=,  > test.xlsx

tshark -r ../Data/Iphone-Data-Capture.pcapng -e packet_no -e packet_size -e ip.src -e ip.dst -e protocol -e length > ../Data-Analysis/Analysis1.csv