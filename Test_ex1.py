import pytest
from ExDebug1 import environnement_optimal

#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    #Arrange : préparer les variables d'entrée et le resultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #Act: appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu



#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal2():
    #Arrange : préparer les variables d'entrée et le resultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu


#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal3():
    #Arrange : préparer les variables d'entrée et le resultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu


#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal4():
    #Arrange : préparer les variables d'entrée et le resultat attendu
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu