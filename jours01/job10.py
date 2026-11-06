capital_investie=100000
taux_annuel=3.5
gain_annuel=capital_investie * taux_annuel/100

capital_augmenter=5000
taux_augmenter=2
gain_augmenter=capital_augmenter * taux_augmenter/100

capital_total= capital_investie + capital_augmenter
taux_total= taux_annuel + taux_augmenter
gain_total=capital_total * taux_total/100

print(f"Gain Annuel: {gain_annuel}, Gain Augmenter: {gain_augmenter}, Gain Total:{gain_total}. ")
