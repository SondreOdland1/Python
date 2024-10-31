
secret_word = "Luffy" #ordet man skal tippe seg fram til
guess = "" #guess variabel

while guess != secret_word: #while loopen vil fortsette så lenge guess ikke er lik secret_word
    guess = input ('Enter guess:') #input hvor bruker kan tipper ord

print('riktig')


# Her har vi laget flere variabla som vi kan referere til
secret_word = "zoro" 
guess = "" 
guess_count = 0 
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): #While loop med 2 bestemmelser
    if guess_count < guess_limit: #hvis order er feil og bruker har mer forsøk fortsette while loop
        guess = input ('Enter guess:') #input hvor bruker kan tippe
        guess_count += 1 #hver gange bruker tipper feil legges 1 til forsøk 
    else:
        out_of_guesses = True #Bruker har brukt 3 forsøk og else blir true, while loop brytes


if out_of_guesses:
    print('Du tapte, ikke mer forsøk')
else:
    print('Riktig')


