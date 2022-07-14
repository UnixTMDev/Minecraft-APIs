# This is an API frontend to download a minecraft server's data* based on the server inputted by user.
# *Not all of it, see my Hypixel example.
# You can snatch this, assuming you credit me.
# If you don't, I'll report you to the place you posted my code on.



# APIs:
# MineTools for server data

# How it works:
# Just saves the icon and JSON data from MineTools API.
import sys
import os
import urllib.request, json
print("You MUST delete the folder corresponding to the server's IP address, or the file saving will not work.\n\n")
print("Port is 12345 in 192.168.900.128:12345")
print("Hey, what's the IP for the server?\n")
serverIP = sys.stdin.readline()
ayo = len(serverIP)
ayo = ayo-1
serverIP = serverIP[:ayo]
print("What was the port? [DO DEFAULT IF THERE IS NOT A SPECIFIED ONE]\n(DEFAULT IS 25565) (port being 12345 its server.ip.idk.bro:12345)\n")
serverPort = sys.stdin.readline()
wtf = len(serverPort)
wtf = wtf-1
serverPort = serverPort[:wtf]

# API links
#
queryURL = "https://api.minetools.eu/query/"+serverIP+"/"+serverPort+"/"
# ^ More advanced data accessible without joining (JSON)
pingURL = "https://api.minetools.eu/ping/"+serverIP+"/"+serverPort+"/"
# ^ Stuff you see from the server list (JSON)
iconURL = "https://api.minetools.eu/favicon/"+serverIP+"/"+serverPort+"/"
# ^ Server's icon (PNG)

print("\n\nIf detailed data just says Timed Out, see this API note.")
print("'Don't forget to enable it! Make sure to have [enable-query=true] set in your server.properties to use this function at all.'")
print("So, make sure it's on for the server you're testing if you want details.\n\n")

dataExtension = ".json"
imgExtension = ".png"
folder = "servers/"+serverIP+":"+serverPort
iconDir = folder+"/server-icon"+imgExtension
queryDir = folder+"/detailed-server-data"+dataExtension
pingDir = folder+"/server-listing"+dataExtension
os.mkdir(folder)


# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]
urllib.request.urlretrieve(iconURL, iconDir)
# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]

# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]
urllib.request.urlretrieve(pingURL, pingDir)
# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]

# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]
urllib.request.urlretrieve(queryURL, queryDir)
# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]