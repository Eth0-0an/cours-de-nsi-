def nombre_coureurs(lst):
    ```retourne le nombre de coureurs dans lst```
    assert type(lst) == list
    assert all([type (obj) == str for obj in lst])
    return len(lst)

    ##########################
    def premier(lst):
        ```retourne le nombre de coureurs dans lst```
        assert type(lst) == list
        assert all([type (obj) == str for obj in lst])
        return lst[0]
# Tests

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert premier(classement) == "Nadia"
##################

def dernier(classement):
    ```retourne le nombre de coureurs dans lst```
        assert type(lst) == list
        assert all([type (obj) == str for obj in lst])
        return lst[0]

# Tests

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert dernier(classement) == "Laure"

####################################

def longueur_vol(n):
    assert type (n) == int and n>=1
    compteur)=0
    while n>=1:
        if n %2==0:
            n=n//2
        else:
            n=3*n+1
        compteur +=1
return compteur 

# Tests

assert longueur_vol(3) == 7
assert longueur_vol(7) == 16
assert longueur_vol(1) == 0