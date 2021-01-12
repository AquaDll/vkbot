import vk_api
import os
from time import sleep
from datetime import datetime
import json
import bs4
from bs4 import BeautifulSoup
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk = vk_api.VkApi(token='')
vk._auth_token()
vk.get_api()


# Стартовая клавиатура
keyboard_standart = VkKeyboard(one_time=True)


# Четная/нечетная неделя
def Number_of_week():
    if datetime.today().isocalendar()[1] % 2 == 0:
        return('Идет Четная неделя!')        
    else:
        return('Идет Нечетная неделя!')

# Для беседы
def get_random_id():
    return random.randint(0, 100000000)





    

    


# Орел Решка
def Brosit_monetku(id):
    f = ['Орел','Решка','Ребро']
    d = random.randint(0, len(f)-1)
    vk.method("messages.send", {"peer_id": id, "random_id": 0, "message": 'Вам выпало: "'+f[d]+'"'})


# Уроки Расписание Звонков

lessons = '''
1 пара- 8:45-10:15

Перемена: 15 минут

2 пара- 10:30-12:00

Перемена: 40 минут

3 пара- 12:40-14:10

Перемена: 10 минут

4 пара- 14:20-15:50

Перемена: 10 минут

5 пара- 16:00-17:30
'''


bot_help = '''
⚙ Всю актуальную информацию об KMMBot вы можете найти тут:
//Ссылка тут
'''
# Создатели

creators = """
Разработчики - @d3c0dik(Sergey)
Редакция - 

"""
# Сам код

group_id = '200200719'
longpoll = VkBotLongPoll(vk, group_id)

for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            #print(event.object)
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split(" ")

            str1 = message[0].split("|")[0]

            str1 = str1.replace("[club", "")
            if group_id == str1:
                message.pop(0)

            message = ' '.join(message).lower()

            id = json_object['peer_id']
            print(message)
            
            if message == 'начать' or message == 'помощь':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  bot_help })
            elif message == 'kmmbot' or message == 'botkmm':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  '''Привет! Появились какие-то проблемы или же нашел баг? 
               @club198158738 (Пиши в сообщения сообщества!)
                ''' })
            elif message == 'бросить монетку':
                Brosit_monetku(event.object.message['peer_id'])  
            elif message == 'номер недели' or message == 'какой сегодня номер недели':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  Number_of_week() })
            elif message == 'создатели' or message == 'разработчики':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  creators })
            elif message == 'расписание':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  lessons })
            elif message == 'nigger' or message == 'ниггеры' or message == 'ниггер' or message == 'нигга' or message == 'черный':
                vk.method("messages.send", {"peer_id": id, "message": "Nigga?", "attachment": "photo-200206824_457239017", "random_id": 0})
          

            
