import json
import requests


class Post:
    def __init__(self,d):
        self.__dict__ = d

    def __str__(self):
        result = 'Post:\n'
        for k, v in self.__dict__.items():
            result += str(k)
            result += ' = '
            result += str(v)
            result += '\n'

        return result

idPhoto = input("Enter photo id: ")
response = requests.get("https://jsonplaceholder.typicode.com/posts/"+idPhoto)
postJson = json.loads(response.content)
if response.status_code // 100 == 2:
      post1= Post(postJson)
      print(post1)
else:
    print('invalid id')