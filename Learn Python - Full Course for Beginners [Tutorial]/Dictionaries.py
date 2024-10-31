
monthConversions = { 
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct':'October',
    'Nov': 'November',
    'Dec': 'December',
}
#The keys has to be uniq, can't name to keys "Jan". We can also use numbers as keys


print(monthConversions['Apr'])
print(monthConversions['Feb'])

print(monthConversions.get('Dec', 'Not a valid key'))
print(monthConversions.get('Des', 'Not a valid key'))

