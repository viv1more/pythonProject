teams = {

    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

# print(teams)

print('\n\n')
# print(teams['Seattle'])

teams['Mumbai'] = 'Indians'

for key in teams:
    print(key, end =" ")
    print(teams[key])

print(teams)

#to make dictionary empty we can use {}

# teams = {}
# print(teams)