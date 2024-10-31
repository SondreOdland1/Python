
phrase = "Giraffe Academy" # Definerer Giraff Academy som variabelen phrase

print(phrase)
print("Giraffe\nAcademy") #Skriver Academy på neste linje
print("Giraffe\"Academy") #hvis du ønsker og ha med anførselstegn i outputen
print("Giraffe Academy")


print(phrase + "is cool") #Kan sette sammen to stings

print(phrase.lower()) #Printer variabelen phrase med kun små bokstaver
print(phrase.upper()) #Printer variabelen phrase med kun store bokstaver

print(phrase.isupper()) #sjekker om det er kun store bokstaver

print(phrase.upper().isupper()) #her blir variabelen konvertert til kun store bokstaver før den sjekker om alle er store, dermed får vi "true"

print(len(phrase)) #hvor mange karakterer er i stringen phrase

print(phrase[3]) #Henter fjerde verdi i variabelen

print(phrase.index('a')) #forteller hvor i variabelen G befinner seg 

print(phrase.replace('Giraffe', 'Frus')) #Bytter ut verdier i variabelen med andre 


