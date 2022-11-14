import requests
import json
import yadisk

class hero:
   hero_d = {}
   hero_list = []
   def __init__(self, name, id):
       self.name = name
       self.id = id
       self.b_url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"


   def hero_intelligence(self):
       url ='/id/' + self.id + ".json"
       response = (requests.get(self.b_url + url ).json())
       hero_power = response['powerstats']
       hero_intelligence = int(hero_power['intelligence'])
       hero.hero_d[self.name] = hero_intelligence
       return



hulk = hero('hulk' ,'332')
hulk.hero_intelligence()
Captain_America = hero('Captain_America' ,'149')
Captain_America.hero_intelligence()
Thanos = hero('Thanos' ,'655')
Thanos.hero_intelligence()

def smartest(slovar):
    i = max(slovar, key=slovar.get)
    print(f'Самый умный герой - {i}')

smartest(hero.hero_d)

####Задание 2



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        r = file_path.split('/')
        name = r[-1]
        t = yadisk.YaDisk(token=self.token)
        t.upload(file_path, name)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь к файлу-")
    token = input("Введите токен-")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)







