import re

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
    return re.search(r'(?!## Version )+([0-9]+\.?[0-9]*\.*[0-9]*)', lines[0]).group()

def extract_friendlyversion(lines):
    return re.search(r'(?!## Version )+([0-9]+\.?[0-9]*\.*[0-9]*)+(.*)+(?= \()', lines[0]).group()
    
def extract_date(lines):
    return re.search(r'(202[0-9]-[01]*[0-9]-[0123]*[0-9])', lines[0]).group()
    
def extract_url(lines):
    dl_line = "empty"

    for line in lines:
        if "### [Download]" in line:
            dl_line = line
            return re.search(r'(https:\/\/cdn.jsdelivr.net\/gh\/retrotink-llc\/firmware@main\/RetroTINK-)+((4K\/)|(5X%20Pro\/))+(Release\/|Experimental\/|SD%20card%20images\/)+(.+)+(.zip|.hex)', dl_line).group()
    
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
        if not(line == "\n" or line == " " or "<br" in line or "<p" in line) and found_end == False:
            changelog_list_2.append(line)
            found_end = True
        elif found_end == True and not ("<br" in line or "<p" in line) and not ((line == "\n" or line == " ") and (changelog_list_2[-1] == "\n" or changelog_list_2[-1] == " ")):
            changelog_list_2.append(line)

    if not changelog_list_2:
        print("Text parsing error - version extraction")
        sys.exit()

    return changelog_list_2[::-1]

def open_write(name, text):
    try:
        with open (name, "w") as versionfile:
            versionfile.write(text)
            versionfile.close()
        return
    except:
        print("Write error!")
        sys.exit()

def main():
    rt4k_lines = read_and_extract_latest("4k.md")
    rt4k_exp_lines = read_and_extract_latest("4k-experimental.md")
    rt4k_sd_lines = read_and_extract_latest("4k-sdcards.md")
    rt5x_lines = read_and_extract_latest("5x.md")
    rt5x_exp_lines = read_and_extract_latest("5x-experimental.md")
    
    test_set = [rt4k_lines, rt4k_exp_lines, rt4k_sd_lines, rt5x_lines, rt5x_exp_lines]
    
    for lines in test_set:
        print(''.join(extract_version(lines)))
        print(''.join(extract_friendlyversion(lines)))
        print(''.join(extract_date(lines)))
        print(''.join(extract_url(lines)))
        print(''.join(extract_crc32(lines)))
        print(''.join(extract_sha256(lines)))
        print(''.join(extract_changelog(lines)))

if __name__ == "__main__":
    main()