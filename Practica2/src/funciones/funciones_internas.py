def update_scores(round, this_round, total_points):
    """Actualiza los stats de cada usuario por ronda y en el total
    
    Args:
        round (dict): Contains the data of the current round
        this_round (dict): updates the data for each player in the current round
        total_points (dict): acumulates the global points of the game
    
    Returns:
        None
        
    """
    for player,stats in round.items():
        score = 0
        score += stats['kills'] * 3
        score += stats['assists'] * 1
        score += -1 if stats['deaths'] else 0
        this_round[player]['score'] = score
        this_round[player]['kills'] = stats['kills']
        this_round[player]['assists'] = stats['assists']
        this_round[player]['deaths'] = -1 if stats['deaths'] else 0
        total_points[player]['score'] += score
        total_points[player]['kills'] += stats['kills']
        total_points[player]['assists'] += stats['assists']
        total_points[player]['deaths'] += -1 if stats['deaths'] else 0
        
def get_score(item):
    """Toma el segundo elemento del diccionario exterior, 
    y el elemento con la clave 'score' del diccionario interno
    
    Args:
        item (tuple): A tuple (clave, diccionario_interno)    
    Returns: 
        ??
        #int: value associated with the 'score' key
        #function
    """
    return item[1]['score']   

def print_data(this, total):
    """Imprime los puntajes obtenidos
    
    Args: 
        this (list): The sorted data of the current round or "this_round"
        total (list): The sorted total_points data
    
    Returns:
        None
    
    """
    print("              ESTA RONDA              |          ESTADISTICAS TOTALES \n")
    print("Player   Kills Assists Deaths Points  |   Player   Kills Assists Deaths  MVPs  Points")
    print("-------------------------------------------------------------------------------------")
    i = 0
    for i in range(len(this)):
        act = this[i]
        tot = total[i]
        print(f"{act[0]:<10} {act[1]['kills']:<6}{act[1]['assists']:<7}{act[1]['deaths']:<8}{act[1]['score']:<2}{" ":<4}{"|":<3}{tot[0]:<10} {tot[1]['kills']:<6}{tot[1]['assists']:<7}{tot[1]['deaths']:<8}{tot[1]['MVPs']:<6}{tot[1]['score']:<2}")
    print("\n")
