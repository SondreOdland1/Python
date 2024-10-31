lucky_numbers = [4, 15, 8, 16, 23, 42]
friends = ['Warren Buffett', 'Charlie Munger', 'Pewdiepie', 'Pewdiepie', 'Pewdiepie', 'Pewdiepie', 'Pewdiepie', "Adolf Hitler", "Donald Trump"]
print(friends)
print(lucky_numbers)

friends.append("Walter White") #legger til en verdi i listen
print(friends)

friends.insert(1, "Gus Fring") #legger til en verdi i listen hvor indeksen er 1. Alle andre verdier skyves til høgre
print(friends)

friends.pop() #fjerner den bakerste verdien i listen
friends.pop()
print(friends)

friends.remove('Gus Fring')
print(friends)
print(friends.index('Adolf Hitler')) #Kan se om Adolf Hitler er i listen, og dermed se hvilken index verdien har.
print(friends.count('Pewdiepie')) #Teller hvor mange ganger samme verdi går igjen

friends.sort() #sorterer i alfabetisk rekkefølge
print(friends)

friends2 = friends.copy() #Lager en kopi av variebelen 
print(friends2) 

friends.clear() #fjerne alle verdiene i listen 'friends'

lucky_numbers.sort()
print(lucky_numbers) #Sorterer tallene i stigende rekkefølge

lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers) #veldig enkel måte å sette to liste sammen
print(friends)




