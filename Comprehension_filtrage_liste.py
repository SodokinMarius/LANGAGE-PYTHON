#coding : utf-8

if __name__ == '__main__':
    maliste=[1,2,3,7,8]

    qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de

    fruits_stockes = [15 , 3 , 18 , 21] # Par exemple 15 pommes , 3

    [nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if  nb_fruits > qtt_a_retirer ]

