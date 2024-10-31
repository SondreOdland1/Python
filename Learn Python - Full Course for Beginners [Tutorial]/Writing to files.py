
text_file = open('file.txt', 'a') #'a' gjør at vi kan legge tekst til en fil

text_file.write('Toby - Human Resources')
text_file.write('\nKelly - Customer Service') #'\n' sier at denne teksten skal komme på en ny linje
text_file.write('\nKelly - Customer Service') #'\n' sier at denne teksten skal komme på en ny linje
text_file.write('\nKelly - Customer Service') #'\n' sier at denne teksten skal komme på en ny linje

text_file.close()

#Ved å kalle filen noe annet, skaper du en ny fil
text_file = open('file1.txt', 'w') #'w' gjør at du lager din egen fil, i denne koden vill kun toby og kelly vises i filen 

text_file.write('Toby - Human Resources')
text_file.write('\nKelly - Customer Service') #'\n' sier at denne teksten skal komme på en ny linje

text_file.close()


#åpne koden i en html fil
text_file = open('index.html', 'w')

text_file.write('<p> This is HTML</p>')

text_file.close()