import datetime

time_delta = datetime.timedelta(hours=7, minutes=30)
trains = [{'train_number': '12', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '07:12:00',
        'destination_time': '09:15:00',
        },
        {'train_number': '15', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '07:12:00',
        'destination_time': '23:17:00',
        },
        {'train_number': '271', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '04:12:00',
        'destination_time': '20:15:00',
        },
        {'train_number': '29', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '20:12:00',
        'destination_time': '04:15:00',
        },
        {'train_number': '100', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '00:12:00',
        'destination_time': '03:15:00',
        },
        {'train_number': '10191', 
        'departure_place': 'Novie_Novinki',
        'destination_place': 'Starie_Strainki',
        'departure_time': '17:12:00',
        'destination_time': '01:15:00',
        }
]

result_arr = []
for i in trains:
    start_time = datetime.datetime.strptime(i['departure_time'], '%H:%M:%S')
    end_time = datetime.datetime.strptime(i['destination_time'], '%H:%M:%S')
    diff = abs(end_time - start_time)
    if diff > time_delta:
        result_arr.append(i)
print(result_arr)
