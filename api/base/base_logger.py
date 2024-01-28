# import logging
from django.utils import timezone
from core import settings
from django.contrib import messages
import json
from core.settings import TIME_FORMATE



import logging

import sys




def configure_logger():
    logger = logging.getLogger(__name__)
    # logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    # console_handler = logging.StreamHandler(sys.stdout)
    json_formatter = logging.Formatter('{\n' \
                                       '    "timestamp": %(asctime)s,\n' \
                                       '    "level": %(levelname)s,\n' \
                                       '    "message": %(message)s,\n' \
                                       '    "class": %(class)s,\n' \
                                    #    '    "error": %(error)s\n' \
                                       '}', datefmt="%Y-%m-%d %H:%M"
    )
    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

    

    return logger



# def configure_logger():
#     logger = logging.getLogger(__name__)
#     console_handler = logging.StreamHandler()
#     json_formatter = logging.Formatter('{\n' \
#                                        '    "timestamp": "%(asctime)s",\n' \
#                                        '    "level": "%(levelname)s",\n' \
#                                     #    '    "message": "%(message)s",\n' \
#                                        '    "class": "%(class)s",\n' \
#                                        '}', datefmt="%Y-%m-%d %H:%M"
#     )
#     console_handler.setFormatter(json_formatter)
#     logger.addHandler(console_handler)

#     return logger






















class MyLogger: pass
# def error_logger(*args, **kwargs):
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     print('this is from base logger file /*/*/*/*/*/*/')
#     console_handler = logging.StreamHandler()
#     json_formatter = logging.Formatter('{\n' \
#                                     '    "timestamp": "%(asctime)s",\n' \
#                                     '    "level": "%(levelname)s",\n' \
#                                     '    "message": "%(message)s",\n' \
#                                     '    "class": "%(class)s",\n' \
#                                     '}', datefmt="%Y-%m-%d %H:%M"
#     )
#     # json_formatter = logging.Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
#     console_handler.setFormatter(json_formatter)
#     logger.addHandler(console_handler)





















    #     return logger
    
    # def info_logger(self):
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel(logging.DEBUG)
    #     print('this is from base logger file /*/*/*/*/*/*/')
    #     console_handler = logging.StreamHandler()
    #     json_formatter = logging.Formatter('{\n' \
    #                                     '    "timestamp": "%(asctime)s",\n' \
    #                                     '    "level": "%(levelname)s",\n' \
    #                                     '    "message": "%(message)s",\n' \
    #                                     '    "class": "%(class)s",\n' \
    #                                     '}', datefmt="%Y-%m-%d %H:%M"
    #     )
    #     console_handler.setFormatter(json_formatter)
    #     logger.addHandler(console_handler)
    #     return logger
    
    
    # def warning_logger(self):
    # def __init__(self):
    #     self.logger = logging.getLogger(__name__)
    #     self.logger.setLevel(logging.DEBUG)
    #     print('this is from base logger file /*/*/*/*/*/*/')
    #     console_handler = logging.StreamHandler()
    #     json_formatter = logging.Formatter('{\n' \
    #                                     '    "timestamp": "%(asctime)s",\n' \
    #                                     '    "level": "%(levelname)s",\n' \
    #                                     '    "message": "%(message)s",\n' \
    #                                     '    "class": "%(class)s",\n' \
    #                                     '}', datefmt="%Y-%m-%d %H:%M"
    #     )
    #     print('middle')
    #     console_handler.setFormatter(json_formatter)
    #     print('middle11')
    #     self.logger.addHandler(console_handler)



    # def get_logger(self):
    #     return self.logger


        # return logger


"""
class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        json_formatter = logging.Formatter(
            '{\n'
            '    "timestamp": "%(asctime)s",\n'
            '    "level": "%(levelname)s",\n'
            '    "message": "%(message)s",\n'
            '    "class": "%(class)s",\n'
            '}', datefmt="%Y-%m-%d %H:%M"
        )
        console_handler.setFormatter(json_formatter)
        self.logger.addHandler(console_handler)


    def error_logger(self):
        return self.logger

    def info_logger(self):
        return self.logger

    def warning_logger(self):
        return self.logger
        
"""


# logger = logging.getLogger(__name__)
# logger = logging.getLogger("messages")
# local_time = timezone.localtime(timezone.now())
# form_time = local_time.strftime(settings.TIME_FORMATE)




# class JsonFormatter(logging.Formatter):
#     def format(self, record):
#         log_data = {
#             # 'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
#             'timestamp': form_time,
#             'level': record.levelname,
#             'message': record.getMessage(),
#             'custom_message': 'Ваше сообщение здесь',
#             'logger_name': record.name,
#             'exception': self.formatException(record.exc_info) if record.exc_info else None,
#         }

#         return json.dumps(log_data)





# class MyLogger: pass

#     update_q = 'update'

#     create_q = 'create'

#     delete_q = 'delete'

#     # retrieve_q = 'retrieve'
#     RETRIEVE_Q = 'retrieve'


#     def __init__(self, name):
#         self.logger = logging.getLogger(name)
#         log_handler = logging.StreamHandler()
#         log_handler.setFormatter(JsonFormatter())
#         self.logger.addHandler(log_handler)
#         self.logger.setLevel(logging.DEBUG)


#     def log_error(self, obj_type, obj_id, exception, name_class, name_method):
#         """
#         Метод для логирования ошибок.
#         """
#         log_data = {
#             'obj_type': obj_type,
#             'obj_id': obj_id,
#             'exception': str(exception),
#             'name_class': name_class,
#             'name_method': name_method,
#         }




#         message = f"ID {obj_type}, {obj_id}, не найден: {name_class}, {name_method}, ошибка: {exception} время: {form_time}"
        
#         if name_method == self.update_q:
#             # message = f"Ошибка при  {obj_type}, {obj_id}, не найден: {name_class}, {name_method}, ошибка: {exception} время: {form_time}"
#             message2 = f"Ошибка при обновлении {obj_type}, c ID {obj_id} класс {name_class}, метод {obj_type} , ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.create_q:
#             message2 = f"Ошибка при создании {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.delete_q:
#             message2 = f"Ошибка при удалении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         # elif name_method == self.retrieve_q:
#         #     message2 = f"Ошибка при получении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.RETRIEVE_Q:
#             log_data['message'] = f"Ошибка при получении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}"



#         logger.error(message2)
#         # self.logger.error(json.dumps(log_data, default=str))


#     def log_warning(self, obj_type, obj_id, exception, name_class, name_method):
#         """
#         Метод для логирования предупреждений.
#         """
#         # message = f"Заказ с ID {kwargs['pk']} не найден: {self.__class__.__name__}.{self.action} ошибка {ht} время {form_time}"
#         message = f"{obj_type} с ID {obj_id} не найден: {name_class}, {name_method}, ошибка: {exception} время: {form_time}"
        
#         if name_method == self.update_q:
#             message2 = f"При обновлении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.create_q:
#             message2 = f"При создании {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.delete_q:
#             message2 = f"При удалении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         elif name_method == self.retrieve_q:
#             message2 = f"При получении {obj_type} ID {obj_id}, класс: {name_class}, метод: {name_method}, ошибка: {exception} время: {form_time}"
        
#         # logger.warning(message2)






# def log_factory(name):
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)




# class MyLogger:
#     def __init__(self, name, log_file='log.txt'):
#         self.logger = logging.getLogger(name)
#         self.logger.setLevel(logging.DEBUG)

#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#         file_handler = logging.FileHandler(log_file)
#         file_handler.setFormatter(formatter)

#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(formatter)

#         self.logger.addHandler(file_handler)
#         self.logger.addHandler(console_handler)

#     def log_with_timezone(self, level, message):
#         timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')
#         log_message = f'{timestamp} - {level} - {message}'
#         getattr(self.logger, level.lower())(log_message)





'''
if __name__ == "__main__":
    logger = MyLogger("my_logger")

    logger.log_with_timezone("DEBUG", "Debug message")
    logger.log_with_timezone("INFO", "Info message")
    logger.log_with_timezone("WARNING", "Warning message")
    logger.log_with_timezone("ERROR", "Error message")
    logger.log_with_timezone("CRITICAL", "Critical message")
'''







# import logging
# import json
# import sys

# # Настройка логгера

# logger = logging.getLogger("my_logger")
# logger.info


# logger.setLevel(logging.DEBUG)

# # Создание обработчика для вывода в консоль
# console_handler = logging.StreamHandler(sys.stdout)

# # Форматирование в виде JSON
# json_formatter = logging.Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')

# # Установка форматирования для обработчика
# console_handler.setFormatter(json_formatter)

# # Добавление обработчика к логгеру
# logger.addHandler(console_handler)















"""


class MyLogger:
    def error_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        print('this is from base logger file /*/*/*/*/*/*/')
        console_handler = logging.StreamHandler(sys.stdout)
        json_formatter = logging.Formatter('{\n' \
                                        '    "timestamp": "%(asctime)s",\n' \
                                        '    "level": "%(levelname)s",\n' \
                                        '    "message": "%(message)s",\n' \
                                        '    "class": "%(class)s",\n' \
                                        '}', datefmt="%Y-%m-%d %H:%M"
        )
        # json_formatter = logging.Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
        console_handler.setFormatter(json_formatter)
        logger.addHandler(console_handler)

        return logger
    
    def info_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        print('this is from base logger file /*/*/*/*/*/*/')
        console_handler = logging.StreamHandler(sys.stdout)
        json_formatter = logging.Formatter('{\n' \
                                        '    "timestamp": "%(asctime)s",\n' \
                                        '    "level": "%(levelname)s",\n' \
                                        '    "message": "%(message)s",\n' \
                                        '    "class": "%(class)s",\n' \
                                        '}', datefmt="%Y-%m-%d %H:%M"
        )
        console_handler.setFormatter(json_formatter)
        logger.addHandler(console_handler)
        return logger
    
    
    def warning_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        print('this is from base logger file /*/*/*/*/*/*/')
        console_handler = logging.StreamHandler(sys.stdout)
        json_formatter = logging.Formatter('{\n' \
                                        '    "timestamp": "%(asctime)s",\n' \
                                        '    "level": "%(levelname)s",\n' \
                                        '    "message": "%(message)s",\n' \
                                        '    "class": "%(class)s",\n' \
                                        '}', datefmt="%Y-%m-%d %H:%M"
        )
        console_handler.setFormatter(json_formatter)
        logger.addHandler(console_handler)
        return logger

"""


"""
def configure_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    print('this is from base logger file /*/*/*/*/*/*/')
    console_handler = logging.StreamHandler(sys.stdout)
    json_formatter = logging.Formatter('{\n' \
                                       '    "timestamp": "%(asctime)s",\n' \
                                       '    "level": "%(levelname)s",\n' \
                                       '    "message": "%(message)s",\n' \
                                    #    '    "class": "%(class)s",\n' \
                                       '    "class": "%(class)s",\n' \
                                       '}', datefmt="%Y-%m-%d %H:%M"
    )
    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

    return logger



"""


























