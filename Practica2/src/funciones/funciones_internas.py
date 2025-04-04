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
