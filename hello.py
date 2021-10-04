class Cours:
    def __init__(self, name):
        self.name = name

    def sum(self):
        self.data1 = int(input("Quel est votre premier chiffre ?"))
        self.data2 =  int(input("Quel est votre deuxieme  chiffre ?"))
        self.total = self.data1 + self.data2
        print("La somme donne  ", self.total)
        
    def afficher(self):
        print("Bonjour "+self.name)

    def age(self, age):
        self.age = int(input("Quel age as tu ? "))
        print("Tu as ",self.age, " an(s)")

    def anneDeNaissance(self, anneActuel):
        self.anneActuel = int(anneActuel)
        self.dateNaissance = self.anneActuel - int(self.age)
        print("Tu es nee en "+ str(self.dateNaissance))

# Demander d'entrer une annee
# Affichier "passe" si elle est inferieur a 2021
#Afficher "futur" i elle est superieure
#Afficher "present" si c''''''est lanne actuel
    def  annee(self, annee):
        self.annee =int( annee)
        if self.annee > 2021:
            print("Futur")
        elif self.annee < 2021:
            print("Passe")
        else:
            print("Present")

    def  anneeNais(self):
            self.anneeNais =int(input('Votre annee de naissance ?'))
            if self.anneeNais > 2021:
                print("Tu n'ai pas encore nee")
            elif self.anneeNais < 2021:
                if (2021 - self.anneeNais) > 18:
                    print("Vous etes majeur")
                else:
                    print("Vous etes mineur")
            else:
                print("Vous venez de naitre")

#Demander un mot a l'utilisateur
# Demander de taper un mot contenant la lettre e
    def lettreE(self):
        self.lettreE = input("Taper un mot")
        if "e" in self.lettreE :
            print("OK")

    def password(self):
        self.password = "toto"
        self.passwordEntre = input("Taper votre mot de passe")
        if(self.password == self.passwordEntre): 
            print("Bienvenue")
        else :
            print("Mot de passe incorrect")

    def voyelle(self):
        self.voyelle = input("Taper une lettre")
        if self.voyelle in "aeiouyAEIOUY":
            print("C'est une voyelle")
        else :
            print("C'est une console")

    def testBoolean(self):
        self.a = int(input("Entrer un nombre"))
        self.b = int(input("Entrer un nombre"))
        self.c = int(input("Entrer un nombre"))
        self.d = int(input("Entrer un nombre"))

        if self.a == self.b and self.a == self.c and self.a == self.d:
            return True
        elif self.a > self.c and self.d < self.b :
            return self.a + self.c + self.b + self.d

    def longeurChaine(self):
        self.chaine1 = input("Premier caractere ?")
        self.chaine2 = input("Deuxieme caractere ?")

        if len(self.chaine1) > len(self.chaine2):
            return self.chaine1
        else:
            return self.chaine2

    def AfficheRien(self):
        self.mot = input("Entrer un mot ? ")

        print("Ce mot a ",len(self.mot), " caractere(s)")

    def zero(self):
        return 0


cour1 = Cours("Landry")
#cour1.afficher()
#cour1.sum()
#cour1.age(30)
#cour1.anneDeNaissance(2021)
#cour1.annee(1990)
#cour1.anneeNais()

#cour1.lettreE()
#cour1.password()
#cour1.voyelle()

#print(cour1.testBoolean())

print(cour1.longeurChaine())

