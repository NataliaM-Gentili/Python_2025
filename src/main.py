from funciones import functions

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
 
this_round = functions.initialize_data(rounds)
total_points = functions.initialize_data(rounds)
total = functions.process_data(rounds, this_round, total_points)
functions.ranking_final(total) 
 

