
is_male = True  #True så printer du det som står i if statement, false så printer du det som står i else statementen
is_tall = False

if is_male:
    print('your are a male')
else:
    print('Your are not a male')



if is_male or is_tall:
    print('your are a male or tall or both')
else:
    print('Your neither male nor tall')



if is_male and is_tall:
    print('Your are a male and tall')
else:
    print('Your are either not male or not tall or both')


if is_male and is_tall:
    print('Your are a male and tall')
elif is_male and not(is_tall):
    print('you are a short male')
elif not (is_male) and is_tall:
    print('you are a not a male but you are tall')
else:
    print('Your are either not male or not tall or both')
