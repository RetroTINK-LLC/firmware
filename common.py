import re
import argparse
import os
import sys

from random import randint

from discord_webhook import DiscordWebhook, DiscordEmbed

def open_read(name):
    try:
        with open (name, "r") as tinkfile:
            tinkdata = tinkfile.readlines()
            tinkfile.close()
        return tinkdata
    except:
        print("No config file!")
        sys.exit()
        
def extract_latest(lines):
    found_version = False
    changelog_list = []

    for line in lines:
        if "## Version" in line and not found_version:
            found_version = True
            changelog_list.append(line)
        elif "## Version" in line and found_version:
            return changelog_list
        elif found_version:
            changelog_list.append(line)

    print("Text parsing error - version extraction")
    sys.exit()

def read_and_extract_latest(name):
    return extract_latest(open_read(name))

def extract_version(lines):
    return re.search(r'(?!## Version )+([0-9]+(.?[0-9]+)*)', lines[0]).group()

def extract_friendlyversion(lines):
    return re.search(r'(?!## Version )+([0-9]+(.?[0-9]+)*)+(.*)+(?= \()', lines[0]).group()
    
def extract_date(lines):
    return re.search(r'(20\d\d-\d{2}-\d{2})', lines[0]).group()
    
def extract_url(lines):
    dl_line = "empty"

    for line in lines:
        if "### [Download]" in line:
            dl_line = line
            return re.search(r'(https?://).*(?=\))', dl_line).group()
    
    print("Text parsing error - version extraction")
    sys.exit()
    
def extract_crc32(lines):
    for line in lines:
        if "CRC-32: `" in line:
            return line[9:17]

    print("Text parsing error - version extraction")
    sys.exit()

def extract_sha256(lines):
    for line in lines:
        if "SHA-256: `" in line:
            return line[10:74]

    print("Text parsing error - version extraction")
    sys.exit()

def extract_changelog(lines):
    found_changelog = False
    found_end = False
    changelog_list = []
    changelog_list_2 = []

    for line in lines:
        if "### Changelog" in line and not found_changelog:
            found_changelog = True
        elif found_changelog:
            changelog_list.append(line)

    if not changelog_list:
        print("Text parsing error - version extraction")
        sys.exit()

    for line in changelog_list[::-1]:
        if not(line == "\n" or line == " " or line == "" or "<br" in line or "<p" in line) and found_end == False:
            changelog_list_2.append(line)
            found_end = True
        elif found_end == True and not ("<br" in line or "<p" in line) and not ((line == "\n" or line == " " or line == "") and (changelog_list_2[-1] == "\n" or changelog_list_2[-1] == " ")):
            changelog_list_2.append(line)

    if not changelog_list_2:
        print("Text parsing error - changlog transform failure")
        sys.exit()

    changelog_list_2[0] = changelog_list_2[0].rstrip()
    
    return changelog_list_2[::-1]

def check_version(version, args):
    if not os.path.exists(os.path.splitext(args.target)[0] + ".txt"):
        versionfile = open(os.path.splitext(args.target)[0] + ".txt", "x")
        versionfile.write(version + "\n")
        versionfile.close()
        
        return

    verstring = open_read(os.path.splitext(args.target)[0] + ".txt")[0].rstrip()

    if verstring == version:
        sys.exit(2)
    else:
        versionfile = open(os.path.splitext(args.target)[0] + ".txt", "w")
        versionfile.write(version + "\n")
        versionfile.close()
        return verstring

def generate_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    hex_color = f'{r:02x}{g:02x}{b:02x}'

    return int(hex_color, 16)

    return int(f'{r:02x}{g:02x}{b:02x}', 16)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=str, help='File to parse')
    args = parser.parse_args()

    if args.target is None:
        print("No file given!")
        sys.exit()
        
    if not os.path.exists(args.target):
        print("File does not exist!")
        sys.exit()
        
    if os.path.splitext(args.target)[1] != ".md":
        print("Wrong filetype!")
        sys.exit()

    device_type = ""
    update_type = ""

    is_4K = True

    if os.path.splitext(args.target)[0] == "4k":
        device_type = "RetroTINK-4K"
        update_type = "release firmware"
    elif os.path.splitext(args.target)[0] == "4k-experimental":
        device_type = "RetroTINK-4K"
        update_type = "experimental firmware"
    elif os.path.splitext(args.target)[0] == "4k-sdcards":
        device_type = "RetroTINK-4K"
        update_type = "SD card image"
    elif os.path.splitext(args.target)[0] == "5x":
        device_type = "RetroTINK-5X"
        update_type = "release firmware"
        is_4K = False
    elif os.path.splitext(args.target)[0] == "5x-experimental":
        device_type = "RetroTINK-5X"
        update_type = "experimental firmware"
        is_4K = False
    else:
        sys.exit()

    lines = read_and_extract_latest(args.target)
    
    version = ''.join(extract_version(lines))
    
    old_version = check_version(version, args)
    
    friendlyname = ''.join(extract_friendlyversion(lines))
    upload_date = ''.join(extract_date(lines))
    upload_url = ''.join(extract_url(lines))
    crc32 = ''.join(extract_crc32(lines))
    sha256 = ''.join(extract_sha256(lines))
    changelog = ''.join(extract_changelog(lines))

    main_lines = open_read("index.md")

    if is_4K:
        main_lines[9] = re.sub(r"\[Latest: [0-9]+\.[0-9]+(?:[^\]]*?)<br/>\((202\d-\d\d-\d\d)\)]\({}\)".format(args.target), "[Latest: {}<br/>({})]({})".format(friendlyname,upload_date,args.target), main_lines[9])
    else:
        main_lines[10] = re.sub(r"\[Latest: [0-9]+\.[0-9]+(?:[^\]]*?)<br/>\((202\d-\d\d-\d\d)\)]\({}\)".format(args.target), "[Latest: {}<br/>({})]({})".format(friendlyname,upload_date,args.target), main_lines[10])

    main_file = open("index.md", "w")
    for line in main_lines:
        main_file.write(f"{line}")
    main_file.close()

    debug = """device_type: {}
update_type: {}

version: {}
friendlyname: {}

upload_date: {}
upload_url: {}

crc32: {}
sha256: {}

changelog:
{}

link: {}
""".format(device_type, update_type, version, friendlyname, upload_date, upload_url, crc32, sha256, changelog, "https://retrotink-llc.github.io/" + os.path.splitext(args.target)[0] + ".html")

    embed_title = "A new {} {} is available!".format(device_type, update_type)
    embed_description = """
### **[Version {} ({})]({})**
{}
""".format(friendlyname, upload_date, "https://retrotink-llc.github.io/" + os.path.splitext(args.target)[0] + ".html", changelog)

    embed = DiscordEmbed(title = embed_title, description = embed_description, color = generate_color())

    webhook_url = os.environ['WEBHOOK']

    if is_4K:
        embed.set_thumbnail(url="https://retrotink-llc.github.io/firmware/assets/rt4k.webp")
    else:
        embed.set_thumbnail(url="https://retrotink-llc.github.io/firmware/assets/rt5x.webp")

    webhook = DiscordWebhook(url = webhook_url, username = "Tinky", avatar_url = "https://retrotink-llc.github.io/firmware/assets/tinky_webhook.png")

    webhook.add_embed(embed)
    
    webhook.execute()
    
    print(debug)

if __name__ == "__main__":
    main()