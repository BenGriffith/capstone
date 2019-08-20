def convertAgeToDays(age):
    '''
    Converting value from AgeuponOutcome to age in number of days
    '''

    days_in_week = 7
    days_in_month = 30
    days_in_year = 365
    age_list = age.split()

    if age_list[1][0] == 'w':
        age_in_days = int(age_list[0]) * 7
    elif age_list[1][0] == 'm':
        age_in_days = int(age_list[0]) * 30
    elif age_list[1][0] == 'y':
        age_in_days = int(age_list[0]) * 365
    else:
        age_in_days = int(age_list[0])

    return age_in_days

def getBreed(animal_breed):
    '''
    getBreed takes in one argument and if 'Mix' or '/' is found these values will be removed or replaced with whitespace
    '''
    breed_name = ''
    breed = animal_breed.split()
    slash_exist = False

    if 'Mix' in breed:
        breed.pop()
        breed_name = ' '.join(breed)
    else:
        breed = ' '.join(breed)
        for i in breed:
            if i == '/' :
                slash_exist = True
        
        if slash_exist:
            breed_name = breed.replace('/', ' ')
        else:
            breed_name = breed
    
    return breed_name

def getColor(animal_color):
    '''
    getColor takes in animal_color and returns one of two values based on whether a '/' is found
    in the argument
    '''

    for i in animal_color:
        if i == '/':
            color = 'Mixed'
            break
        else:
            color = 'Non-Mixed'
    
    return color