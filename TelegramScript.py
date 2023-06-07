import json
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib
from datetime import *

matplotlib.use('SVG')


def load_json(name_json):
    try:
        with open(name_json, 'r', encoding='utf-8') as f:
            file = json.load(f)
            return file
    except FileNotFoundError:
        print('Неправильный файл')


def all_messages(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('from') == user1:
            count1 += 1
        elif item.get('from') == user2:
            count2 += 1

    messages_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(sorted(messages_data.items(), key=lambda x: x[1]))
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_messages({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_messages({t_date}).png'

    return f'''
    {count1} сообщений от {user1}
    {count2} сообщений от {user2}
    {count1 + count2} сообщений всего\n
    ''', photo


def date_day(file):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a13 = 0
    a14 = 0
    a15 = 0
    a16 = 0
    a17 = 0
    a18 = 0
    a19 = 0
    a20 = 0
    a21 = 0
    a22 = 0
    a23 = 0
    a24 = 0
    a25 = 0
    a26 = 0
    a27 = 0
    a28 = 0
    a29 = 0
    a30 = 0
    a31 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        item = item['date'].split('T')[0]
        item = item.split('-')[2]
        if item == '01':
            a1 += 1
        elif item == '02':
            a2 += 1
        elif item == '03':
            a3 += 1
        elif item == '04':
            a4 += 1
        elif item == '05':
            a5 += 1
        elif item == '06':
            a6 += 1
        elif item == '07':
            a7 += 1
        elif item == '08':
            a8 += 1
        elif item == '09':
            a9 += 1
        elif item == '10':
            a10 += 1
        elif item == '11':
            a11 += 1
        elif item == '12':
            a12 += 1
        elif item == '13':
            a13 += 1
        elif item == '14':
            a14 += 1
        elif item == '15':
            a15 += 1
        elif item == '16':
            a16 += 1
        elif item == '17':
            a17 += 1
        elif item == '18':
            a18 += 1
        elif item == '19':
            a19 += 1
        elif item == '20':
            a20 += 1
        elif item == '21':
            a21 += 1
        elif item == '22':
            a22 += 1
        elif item == '23':
            a23 += 1
        elif item == '24':
            a24 += 1
        elif item == '25':
            a25 += 1
        elif item == '26':
            a26 += 1
        elif item == '27':
            a27 += 1
        elif item == '28':
            a28 += 1
        elif item == '29':
            a29 += 1
        elif item == '30':
            a30 += 1
        elif item == '31':
            a31 += 1

    day_data = {
        '1': a1,
        '2': a2,
        '3': a3,
        '4': a4,
        '5': a5,
        '6': a6,
        '7': a7,
        '8': a8,
        '9': a9,
        '10': a10,
        '11': a11,
        '12': a12,
        '13': a13,
        '14': a14,
        '15': a15,
        '16': a16,
        '17': a17,
        '18': a18,
        '19': a19,
        '20': a20,
        '21': a21,
        '22': a22,
        '23': a23,
        '24': a24,
        '25': a25,
        '26': a26,
        '27': a27,
        '28': a28,
        '29': a29,
        '30': a30,
        '31': a31
    }

    d = OrderedDict(day_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_day({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_day({t_date}).png'

    return \
        f'''
        1 число: {a1},\n 
        2 число: {a2},\n 
        3 число: {a3},\n
        4 число: {a4},\n
        5 число: {a5},\n
        6 число: {a6},\n
        7 число: {a7},\n
        8 число: {a8},\n
        9 число: {a9},\n
        10 число: {a10},\n
        11 число: {a11},\n
        12 число: {a12},\n
        13 число: {a13},\n
        14 число: {a14},\n
        15 число: {a15},\n
        16 число: {a16},\n
        17 число: {a17},\n
        18 число: {a18},\n
        19 число: {a19},\n
        20 число: {a20},\n
        21 число: {a21},\n
        22 число: {a22},\n
        23 число: {a23},\n
        24 число: {a24},\n
        25 число: {a25},\n
        26 число: {a26},\n
        27 число: {a27},\n
        28 число: {a28},\n
        29 число: {a29},\n
        30 число: {a30},\n
        31 число: {a31}
        ''', photo


def date_hour(file):
    h00 = 0
    h01 = 0
    h02 = 0
    h03 = 0
    h04 = 0
    h05 = 0
    h06 = 0
    h07 = 0
    h08 = 0
    h09 = 0
    h10 = 0
    h11 = 0
    h12 = 0
    h13 = 0
    h14 = 0
    h15 = 0
    h16 = 0
    h17 = 0
    h18 = 0
    h19 = 0
    h20 = 0
    h21 = 0
    h22 = 0
    h23 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        item = item['date'].split('T')[1]
        item = item.split(':')[0]
        if item == '00':
            h00 += 1
        elif item == '01':
            h01 += 1
        elif item == '02':
            h02 += 1
        elif item == '03':
            h03 += 1
        elif item == '04':
            h04 += 1
        elif item == '05':
            h05 += 1
        elif item == '06':
            h06 += 1
        elif item == '07':
            h07 += 1
        elif item == '08':
            h08 += 1
        elif item == '09':
            h09 += 1
        elif item == '10':
            h10 += 1
        elif item == '11':
            h11 += 1
        elif item == '12':
            h12 += 1
        elif item == '13':
            h13 += 1
        elif item == '14':
            h14 += 1
        elif item == '15':
            h15 += 1
        elif item == '16':
            h16 += 1
        elif item == '17':
            h17 += 1
        elif item == '18':
            h18 += 1
        elif item == '19':
            h19 += 1
        elif item == '20':
            h20 += 1
        elif item == '21':
            h21 += 1
        elif item == '22':
            h22 += 1
        elif item == '23':
            h23 += 1

    hour_data = {
        '00': h00,
        '01': h01,
        '02': h02,
        '03': h03,
        '04': h04,
        '05': h05,
        '06': h06,
        '07': h07,
        '08': h08,
        '09': h09,
        '10': h10,
        '11': h11,
        '12': h12,
        '13': h13,
        '14': h14,
        '15': h15,
        '16': h16,
        '17': h17,
        '18': h18,
        '19': h19,
        '20': h20,
        '21': h21,
        '22': h22,
        '23': h23
    }

    d = OrderedDict(hour_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_hour({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_hour({t_date}).png'

    return f'''
    00 часов: {h00},\n 
    01 часов: {h01},\n 02 часов: {h02},\n 
    03 часов: {h03},\n 04 часов: {h04},\n 
    05 часов: {h05},\n 06 часов: {h06},\n 
    07 часов: {h07},\n 08 часов: {h08},\n 
    09 часов: {h09},\n 10 часов: {h10},\n 
    11 часов: {h11},\n 12 часов: {h12},\n 
    13 часов: {h13},\n 14 часов: {h14},\n 
    15 часов: {h15},\n 16 часов: {h16},\n 
    17 часов: {h17},\n 18 часов: {h18},\n 
    19 часов: {h19},\n 20 часов: {h20},\n 
    21 час: {h21},\n 22 час: {h22},\n 
    23 час: {h23} ''', photo


def month_data(file):
    january = 0
    february = 0
    march = 0
    april = 0
    may = 0
    june = 0
    jule = 0
    august = 0
    september = 0
    october = 0
    november = 0
    december = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        item = item['date'].split('T')[0]
        item = item.split('-')[1]
        if item == '01':
            january += 1
        elif item == '02':
            february += 1
        elif item == '03':
            march += 1
        elif item == '04':
            april += 1
        elif item == '05':
            may += 1
        elif item == '06':
            june += 1
        elif item == '07':
            jule += 1
        elif item == '08':
            august += 1
        elif item == '09':
            september += 1
        elif item == '10':
            october += 1
        elif item == '11':
            november += 1
        elif item == '12':
            december += 1

    monthes_data = {
        'Январь': january,
        'Февраль': february,
        'Март': march,
        'Апрель': april,
        'Май': may,
        'Июнь': june,
        'Июль': jule,
        'Август': august,
        'Сентябрь': september,
        'Октябрь': october,
        'Ноябрь': november,
        'Декабрь': december
    }

    d = OrderedDict(monthes_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_months({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_months({t_date}).png'

    return f'''
          Кол-во сообщений:\n
          в Январе: {january},\n
          в феврале: {february},\n
          в марте: {march},\n
          в апреле: {april},\n
          в мае: {may},\n
          в июне: {june},\n
          в июле: {jule},\n
          в августе: {august},\n
          в сентябре: {september},\n
          в октябре: {october},\n
          в ноябре: {november},\n
          в декабре: {december}
''', photo


def year_data(file):
    year2020 = 0
    year2021 = 0
    year2022 = 0
    year2023 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        item = item.get('date').split('T')[0]
        item = item.split('-')[0]
        if item == '2020':
            year2020 += 1
        elif item == '2021':
            year2021 += 1
        elif item == '2022':
            year2022 += 1
        elif item == '2023':
            year2023 += 1

    years_data = {
        '2020 год': year2020,
        '2021 год': year2021,
        '2022 год': year2022,
        '2023 год': year2023
    }

    d = OrderedDict(years_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_year({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_year({t_date}).png'

    return f'''
          Кол-во сообщений в 2020 году: {year2020}\n
          Кол-во сообщений в 2021 году: {year2021}\n
          Кол-во сообщений в 2022 году: {year2022}\n
          Кол-во сообщений в 2023 году: {year2023}\n''', photo


def sticker_data(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('media_type') == 'sticker' and item.get('from') == user1:
            count1 += 1
        elif item.get('media_type') == 'sticker' and item.get('from') == user2:
            count2 += 1
    count = count1 + count2

    stickers_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(stickers_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_sticker({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_sticker({t_date}).png'

    return f'''Кол-во стикеров всего: {count}\n
          Кол-во стикеров от {user1}: {count1}\n
          Кол-во стикеров от {user2}: {count2}''', photo


def voice_data(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('media_type') == 'voice_message' and item.get('from') == user1:
            count1 += 1
        elif item.get('media_type') == 'voice_message' and item.get('from') == user2:
            count2 += 1
    count = count1 + count2

    voices_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(voices_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_voices({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_voices({t_date}).png'

    return f'''
          Кол-во голосовых сообщений всего: {count}\n
          Кол-во голосовых сообщений от {user1}: {count1}\n
          Кол-во голосовых сообщений от {user2}: {count2}''', photo


def video_message_data(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('media_type') == 'video_message' and item.get('from') == user1:
            count1 += 1
        elif item.get('media_type') == 'video_message' and item.get('from') == user2:
            count2 += 1
    count = count1 + count2

    video_messages_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(video_messages_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_video_message({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_video_message({t_date}).png'

    return f'''
          Кол-во видеосообщений всего: {count}\n
          Кол-во видеосообщений от {user1}: {count1}\n
          Кол-во видеосообщений от {user2}: {count2}''', photo


def video_file_data(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('media_type') == 'video_file' and item.get('from') == user1:
            count1 += 1
        elif item.get('media_type') == 'video_file' and item.get('from') == user2:
            count2 += 1
    count = count1 + count2

    video_files_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(video_files_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_files_data({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_files_data({t_date}).png'

    return f'''
          Кол-во видео всего: {count}\n
          Кол-во видео от {user1}: {count1}\n
          Кол-во видео от {user2}: {count2}''', photo


def photo_data(file, user1, user2):
    count1 = 0
    count2 = 0
    t_date = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    for item in file['messages']:
        if item.get('photo') == '(File not included. Change data exporting settings to download.)' and item.get(
                'from') == user1:
            count1 += 1
        elif item.get('photo') == '(File not included. Change data exporting settings to download.)' and item.get(
                'from') == user2:
            count2 += 2
    count = count1 + count2

    photos_data = {
        user1: count1,
        user2: count2
    }

    d = OrderedDict(photos_data.items())
    values = list(d.values())
    keys = list(d.keys())
    plt.bar(range(len(d)), values, tick_label=keys)
    plt.savefig(f'addons/photos/saved_photo_data({t_date}).png', dpi=200)
    plt.close()
    photo = f'addons/photos/saved_photo_data({t_date}).png'

    return f'''
          Кол-во фотографий всего: {count}\n
          Кол-во фотографий от {user1}: {count1}\n
          Кол-во фотографий от {user2}: {count2}''', photo
