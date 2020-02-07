import requests

print("=== Local File ===")
with open('f1.txt', 'r') as file:
#    data = file.read().replace('\n', '')
    data = file.read()
print(data)
print("==================")
print("")
print("=== Remote file on github ===")
url = 'https://raw.githubusercontent.com/jmquint/tpub/master/f1'
page = requests.get(url)
print("***"+page.text+"***")
print("===========================")
