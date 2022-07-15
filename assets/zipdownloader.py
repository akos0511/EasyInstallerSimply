import os
import requests
import gdown

linksraw = requests.get("https://raw.githubusercontent.com/Twin1YT/EasyInstallerSimply/main/OlderSeasons.txt")

txt = linksraw.text

lines = [line for line in txt.splitlines() if line.startswith('|')]

lines = '\n'.join(lines)

lines = '\n'.join(['{} {}'.format(i, line) for i, line in enumerate(lines.splitlines())])
print(lines)

links = [line for line in txt.splitlines() if line.startswith("https")]

links = '\n'.join(links)

linksnum = '\n'.join(['{} {}'.format(i, line) for i, line in enumerate(links.splitlines())])




print("Select a build by typing the number next to it! ")
build = input("Build: ")

link = linksnum.splitlines()[int(build)]

link = link.split()[1]
r = requests.get(link)

legit = r.url
legit = legit.split('/')[-2]

print("Where would you like to download the build to? ")
path = input("Path: ")

if not os.path.exists(path):
    print("The path you entered does not exist! ")
else: 
    print("path found!")
url = 'https://drive.google.com/uc?id=' + legit
output = path
gdown.download(url, output, quiet=False)
print("Download complete!")