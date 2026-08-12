import requests


def random_user():

 url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

 response = requests.get(url)

 Data = response.json()
 
 if Data["success"] and "data" in Data:
    user_data = Data["data"]
    username = user_data["login"]["username"]
    country = user_data["location"]["country"]
    return username, country
 else:
   raise Exception("Failed to Fetch The Data")

def main():
   try:
      username , country = random_user()
      print(f"Username: {username} \nCountry: {country}")
   except Exception as x:
      print(str(x))


if __name__=="__main__":
   main()


teri handling success pr hai but data ka format yeh hai 
