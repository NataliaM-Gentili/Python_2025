#calculamos y actualizamos puntajes
def update_scores(round, this_round, total_points):
    """Toma los datos de la ronda pasada por parametro, y actualiza los stats de cada usuario en total_points"""
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
    """Toma el segundo elemento del diccionario exterior, y el elemento con la clave score del diccionario interno"""
    return item[1]['score']   
  
def one_round (rounds, this_round, total_points):
    """Recorre cada ronda actualizando los puntos de cada jugador
    y la imprime en orden descendente acorde a los puntos totales (score)"""
    for round_number, round in enumerate (rounds, start=1):
        update_scores(round, this_round, total_points)
        #print()
        #print(this_round)
        #print()
        #print(total_points)
        #print()
        print(f"RANKING RONDA {round_number}: \n")
        #ordeno por puntaje
        total = sorted(total_points.items(), key = get_score, reverse = True)
        this = sorted(this_round.items(), key = get_score, reverse = True)
        #reverse indica que se ordene en orden decreciente

        mvp_player = this[0][0]
        total_points[mvp_player]['MVPs'] += 1
        
        print("              ESTA RONDA             |||         ESTADISTICAS TOTALES")
        print("Player   Kills Assists Deaths Points     Player   Kills Assists Deaths  MVPs  Points")
        i = 0
        for i in range(len(this)):
            act = this[i]
            tot = total[i]
            #print(tot)
            print(f"{act[0]:<10} {act[1]['kills']:<6}{act[1]['assists']:<7}{act[1]['deaths']:<8}{act[1]['score']:<2}{" ":<4}{"|":<3}{tot[0]:<10} {tot[1]['kills']:<6}{tot[1]['assists']:<7}{tot[1]['deaths']:<8}{tot[1]['MVPs']:<6}{tot[1]['score']:<2}")
        print()


        print(f"MVP DE LA RONDA: {mvp_player}")
        print()
    return total
        
   
def ranking_final (total):
    print()
    print("Ranking final:")
    print("Player   Kills Assists Deaths  MVPs  Points")
    print("-----------------------------------------------")
    for player, stats in total:
        print(f"{player:<10} {stats['kills']:<6}{stats['assists']:<7}{stats['deaths']:<8}{stats['MVPs']:<6}{stats['score']:<2}")
    print("-----------------------------------------------")
    print() 
    print(f"{total[0][0].upper()} ES UN DESTRUCTOR!!")
    