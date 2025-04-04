from funciones import funciones_internas
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
        funciones_internas.update_scores(round, this_round, total_points)
        print(f"RANKING RONDA {round_number} \n".center(80))

        total = sorted(total_points.items(), key = funciones_internas.get_score, reverse = True)
        this = sorted(this_round.items(), key = funciones_internas.get_score, reverse = True)

        mvp_player = this[0][0]
        total_points[mvp_player]['MVPs'] += 1
        funciones_internas.print_data(this, total)
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