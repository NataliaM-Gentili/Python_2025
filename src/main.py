from funciones import one_round, ranking_final

rounds = [
    {
    'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
    'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
    'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
    'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
    'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
    'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
    'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
    'Viper': {'kills': 0, 'assists': 1, 'deaths': False},
    'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
    'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
    'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
    'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
    'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
    'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
    'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
    'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
    'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
    'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
    'Frost': {'kills': 8, 'assists': 1, 'deaths': True},
    'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
    'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
    'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
    'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
    'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
    'Reaper': {'kills': 20, 'assists': 1, 'deaths': True}
    }
]

# creo los diccionarios
# this round es utilizado para imprimir el puntaje por ronda 
# no contempla las rondas anteriores
this_round = {}
for round_number, round in enumerate (rounds, start=1):
        for round in rounds:
            for player in round:
                if player not in this_round:
                    this_round[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'score': 0}
# total points lleva la acumulacion de todas las rondas       
total_points = {}
for round in rounds:
    for player in round:
        if player not in total_points:
            total_points[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'score': 0}

 
total = one_round(rounds, this_round, total_points)
ranking_final(total)

