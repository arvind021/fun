import requests

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI3ODc1NjUwMTAzIiwianRpIjoiMDE5ODc4NzktZGJmYi00MmQ4LWI4YzgtZjliMTY1MDQzMTQyIiwiZXhwIjoxNzk5NjQ3NTExfQ.r_rG9eIWHhiwO75SxWBX7vXDDq949ekZjVNsJCeKLKgu5mLaK15bPx2sn3FTgDd2lurlGvJPlDYH9i1dssSLv8sXFIKJSt7vZWrUuQMyI-n-w2qUTJJcG9HKKl7q61ffJcOEdRucko3n-Ni4NiehjSXUaJrMdnCNb7YWRPvsyDE"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def search_text(text):
    url = "https://funstat.info/api/v1/text/search/"  # trailing slash added
    data = {"text": text}
    try:
        r = requests.post(url, json=data, headers=HEADERS)
        print(r.status_code)
        print(r.json())
    except Exception as e:
        print("Error:", e)

def common_groups(user1, user2):
    url = "https://funstat.info/api/v1/groups/common_groups/"
    data = {"users": [user1, user2]}
    try:
        r = requests.post(url, json=data, headers=HEADERS)
        print(r.status_code)
        print(r.json())
    except Exception as e:
        print("Error:", e)

choice = input("Option choose karo (1/2): ")
if choice == "1":
    text = input("Search text / username likho: ")
    search_text(text)
elif choice == "2":
    u1 = input("User 1: ")
    u2 = input("User 2: ")
    common_groups(u1, u2)
else:
    print("Galat option")
