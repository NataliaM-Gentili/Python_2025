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

def initialize_data(rounds):
    """Inicializa los diccionarios
    
    Args:
        rounds (list[dict[str, dict[str, Any]]]): A list containing the rounds of the game
        
    Returns:
        dict: A dictionary with the players
        
    """
    actual = {}
    for round_number, round in enumerate(rounds, start = 1):
        for player in round:
            if player not in actual:
                actual[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'score': 0}
    return actual

def process_data (rounds, this_round, total_points):
    """Recorre cada ronda actualizando los puntos y los imprime
    
    Args:
        rounds (list[dict[str, dict[str, Any]]]): A list of rounds
        this_round (dict): contains the data of the current round
        total_points (dict): contains the total scores of the game
        
    Returns:
        total (list): Contains the total points sorted in descending order
        
    """
    for round_number, round in enumerate (rounds, start=1):
        update_scores(round, this_round, total_points)
        print(f"RANKING RONDA {round_number} \n".center(80))

        total = sorted(total_points.items(), key = get_score, reverse = True)
        this = sorted(this_round.items(), key = get_score, reverse = True)

        mvp_player = this[0][0]
        total_points[mvp_player]['MVPs'] += 1
        i = 0
        for i in range(len(this)):
            act = this[i] 
            tot = total[i]
            print(f"{act[0]:<10} {act[1]['kills']:<6}{act[1]['assists']:<7}{act[1]['deaths']:<8}{act[1]['score']:<2}{" ":<4}{"|":<3}{tot[0]:<10} {tot[1]['kills']:<6}{tot[1]['assists']:<7}{tot[1]['deaths']:<8}{tot[1]['MVPs']:<6}{tot[1]['score']:<2}")
            print("\n")
            print(f"MVP DE LA RONDA: {mvp_player} \n".center(80))
            print("----------------------------------------- \n".center(80))
    return total
        
   
def ranking_final (total):
    """Imprime las estadísticas totales
      
    Args: 
        total (list): cointains the sorted total points ranking
    
    Returns:
        None
     
    """
    print(f"RANKING FINAL \n".center(80))
    print("Player   Kills Assists Deaths  MVPs  Points".center(80))
    print("-----------------------------------------------".center(80))
    for player, stats in total:
        print(f"{player:<10} {stats['kills']:<6}{stats['assists']:<7}{stats['deaths']:<8}{stats['MVPs']:<6}{stats['score']:<2}".center(76))
    print("----------------------------------------------- \n".center(80))
    print(f"{total[0][0].upper()} ES UN DESTRUCTOR!! \n".center(80))    