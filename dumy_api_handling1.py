import requests

def get_usernames():
    url = "https://dummyjson.com/users"

    response = requests.get(url)
    data = response.json()

    usernames = []

    if data["users"]:
        for users in data["users"]:
            usernames.append(users["username"])

        return usernames
    else:
        raise Exception("Username not found")

def main():
    try:
      usernames = get_usernames()

      print("Username:")
      print(usernames)

    except Exception as x:
        print(str(x))

if __name__ == "__main__":
    main()