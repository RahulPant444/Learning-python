import requests


def random_jokes():

    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"

    response = requests.get(url)

    data = response.json()

    if data["success"] and "data" in data:
     jokes_data = data["data"]
     jokes = jokes_data["content"]
     return jokes

    else:
     raise Exception("Jokes not fetched")

def main():
    try:
     jokes  = random_jokes()
     print(f"Jokes:  {jokes}")
    except Exception as x:
     print(str(x))


if __name__ == "__main__":
  main()