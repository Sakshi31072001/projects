import requests



Api_Key = "iucdwCe9Zmgohx4ziWCOXtYleaMQO7ACT81gxF9l"


def NasaNews(Date):


    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date': str(Date)}

    r = requests.get(Url, params=Params)
    Data = r.json()

    print(Data)
    NasaNews('2020-09-09')