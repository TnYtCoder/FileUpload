import requests, time, os, sys
from colorama import Fore

time.sleep(1)
os.system('clear')
time.sleep(1)
print(Fore.GREEN, "")

def typewriter(logo):
    for char in logo:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def banner():
	logo = '''
 _____ _  _     _____ _     ____  _     ____  ____  ____
/    // \/ \   /  __// \ /\/  __\/ \   /  _ \/  _ \/  _ |
|  __\| || |   |  \  | | |||  \/|| |   | / \|| / \|| | \|
| |   | || |_/\|  /_ | \_/||  __/| |_/\| \_/|| |-||| |_/|
\_/   \_/\____/\____\|____/\_/   \____/\____/\_/ \|\____/

<----------------------------->
|Python Script To Upload Files|
|Storage Credit : File.io     |
<----------------------------->
	'''
	typewriter(logo)
banner()

def upload_file(file_path):
    url = "https://file.io"
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(url, files=files)

    if response.ok:
        response_data = response.json()
        if response_data["success"]:
            return response_data["link"]
        else:
            print(Fore.RED , "File upload failed.")
    else:
        print(Fore.RED, "\nError occurred during file upload.")
    return None

if __name__ == "__main__":
    print(Fore.LIGHTBLUE_EX, "")
    file_path = input("Your File Path : ")
    process = "Processing...\n"
    typewriter(process)
    link = upload_file(file_path)
    if link:
	    print(Fore.GREEN , "File uploaded successfully.")
	    fileurl = "\nFile Url : ", link
	    typewriter(fileurl)

thank = "\nThank You For Using !!!\n"
typewriter(thank)
