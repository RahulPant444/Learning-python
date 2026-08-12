import requests


def get_usernames():
    url = "https://dummyjson.com/users"

    response = requests.get(url)
    data = response.json()

    usernames = []

    if data["users"]:
        for user in data["users"]:
            usernames.append(user["username"])

        return usernames
    else:
        raise Exception("No users found")


def main():
    try:
        usernames = get_usernames()

        print("Usernames: ")
        print(usernames)

    except Exception as x:
        print(str(x))


if __name__ == "__main__":
    main()
