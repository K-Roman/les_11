# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class Parser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.list_out = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        n = 0
        with open(self.file_name, mode='r') as file:
            for line in file:
                if self.i >= len(self.list_out):
                    raise StopIteration
                if self.list_out[self.i][1:17] in line and 'NOK' in line:
                    n += 1
        return self.list_out[self.i][1:17], n

    def method(self):
        self.read()


    def read(self):
        with open(self.file_name, mode='r') as file:
            for line in file:
                if "NOK" in line and line not in self.list_out:
                    self.list_out.append(line)

    # def statistics(self):
    #     for i, item in enumerate(list_out):
    #         list_out[i] = item[0:17] + ']'
    #     set_of_time = set(list_out)
    #     for i, item in enumerate(set_of_time):
    #         stat_out[item] = list_out.count(item)
    #
    #     with open(self.file_name_out, mode='w') as file:
    #         for key in stat_out:
    #             file.write("{} --> {}\n".format(key, stat_out[key]))



# grouped_events = Parser(file_name=file_name)
# grouped_events.method()
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')


def pars_generator(file_name):

    with open(file_name, mode='r') as fi:
        list_out = [line[1:17] for line in fi if 'NOK' in line]
    set_out = set(list_out)
    list1 = list(set_out)
    list1.sort()
    for line in list1:
        if line not in list_out:
            continue
        else:
            yield line, list_out.count(line)


def pars_generator(file_name):
    res = defaultdict(lambda : 0)
    with open(file_name, mode='r') as file:
        for line in file:
            if line.endswith('NOK\n'):
                line = line[1:17]
                res[line] += 1
    for time, count in res.items():
        yield time, count

