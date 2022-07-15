# This is an API frontend to download a minecraft skin based on the username inputted by user.
# You can snatch this, assuming you credit me.
# If you don't, I'll report you to the place you posted my code on.

# APIs:
# Minotar for requesting skins
# MineTools for user data

# How it works:
# Minotar works better with UUIDs than with usernames. So, I use the MineTools User API to get the user data of the requested username.
# MineTools gives UUIDs, which is important, since Minotar prefers UUIDs, I use the Python URL Library's Request module to download the
# skin, and saves it in the Skins folder with the requested username and the part requested as the filename. (By the way, I will mark all the
# code that I didn't write myself.)

# TODO: Add if for parts
# TODO: Add Yes/No for suit/mask

import urllib.request, json
name = input("Enter the username for the owner of the skin you want to download: ")
print("What part of the character do you want?")
part = input("[face, bust, head, body, skin]\n")
part = part.lower()
if part == "face":
    bruh = input("Do you want the mask part with the face? [Yes/No]  ")
    if bruh.lower() == "yes":
        sussy = True
    if bruh.lower() == "no":
        sussy = False
if part == "bust":
    bruh = input("Do you want the suit and mask parts with the bust? [Yes/No]  ")
    if bruh.lower() == "yes":
        sussy = True
    if bruh.lower() == "no":
        sussy = False
if part == "body":
    bruh = input("Do you want the suit and mask parts with the body? [Yes/No]  ")
    if bruh.lower() == "yes":
        sussy = True
    if bruh.lower() == "no":
        sussy = False

if part == "body" and sussy == True:
    target = "armor/body"
if part == "body" and sussy == False:
    target = "body"

if part == "bust" and sussy == True:
    target = "armor/bust"
if part == "bust" and sussy == False:
    target = "bust"

if part == "face" and sussy == True:
    target = "helm"
if part == "face" and sussy == False:
    target = "avatar"

if part == "head":
    target = "cube"

if part == "skin":
    target = "skin"
# ok i think i overestimated how difficult that was gonna be
# im ok now

uuidApiURL = "https://api.minetools.eu/uuid/"
requestURL = uuidApiURL+name
skinAPIURL = "https://minotar.net/"+target+"/"
fileExtension = ".png"
# Snatched from: StackOverflow (https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script) [Top answer]
with urllib.request.urlopen(requestURL) as url:
    user = json.loads(url.read().decode())
    #print(user)
# Snatched from: StackOverflow (https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script) [Top answer]
userid = user["id"]
filename = userid + fileExtension
friendlyFileName = user["name"]+ "'s " + part.capitalize() + fileExtension
saveDir = "skins/"+friendlyFileName
# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]
urllib.request.urlretrieve(skinAPIURL+userid, saveDir)
# Stolen from StackOverflow (https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python) [Answer 1, Comment 3 and 2nd answer]
