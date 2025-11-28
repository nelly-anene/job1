# Stimulation financière d'un investement

def simulation_investissement () :
    montant_initial = 20000
    taux_rendement = 5
    print (f"Montant initial : {montant_initial} euros")
    print (f"Taux de rendement annuel : {taux_rendement}%")

    gain_annuel = montant_initial * taux_rendement /100
    print (f"Gain annuel initial : {gain_annuel}euros")
 
    montant_ajoute = 5000
    montant_total = montant_initial + montant_ajoute
    taux_rendement_ajoute = taux_rendement + 2
    gain_annuel_ajoute = montant_total * taux_rendement_ajoute / 100
    print (f"Après ajoute de 5 000 euros et augmentation du taux :")
    print (f"Nouveau montant total : {montant_total} euros")
    print (f"Nouveau montant taux de rendement : {taux_rendement_ajoute}%")
    print (f"Nouveau gain annuel:{gain_annuel_ajoute} euros")

    retrait = montant_total * 0.10
    montant_apres_retrait = montant_total - retrait
    taux_rendement_final = taux_rendement_ajoute - 1
    print(f"Après retrait de 10% et diminution du taux :")
    print(f"Montant après retrait : {montant_apres_retrait} euros")
    print(f"Taux de rendement final : {taux_rendement_final}%")

    gain_annuel_final = montant_apres_retrait * taux_rendement_final / 100
    print(f"Gain annuel final : {gain_annuel_final} euros")

if __name__ == '__main__':
    simulation_investissement()