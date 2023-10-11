import pandas as pd
import glob as gl
import numpy as np

recipe_files = gl.glob('recipes/*.txt')
names = []
meal = []
urls = []
ingredients = []

for file in recipe_files:
    with open(file) as f:
        lines = f.readlines()
        line0 = lines[0].split(',')
        names.append(line0[0])
        meal.append(line0[1].strip())
        urls.append(lines[1])
        ingredients.append(lines[2:])

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat']
meals = ['Breakfast', 'Lunch', 'Dinner']

print('{0:<20}'.format(' '), end='')
for d in days:
    print('{0:<20}'.format(d), end='')
print()

for i in range(20 + len(days)*20):
    print('-', end='')
print()

meals_to_make = []

for m in meals:
    print('{0:<10}'.format(m), end='')
    print(' | ', end='')
    for d in days:
        
        meal_ind = []
        for i in range(len(names)):
            if meal[i] == m:
                meal_ind.append(i)

        meal_idx = np.random.choice(meal_ind)
        meals_to_make.append(names[meal_idx])
        print('{0:<20}'.format(names[meal_idx]), end='')
    print()

m2m_set = set(meals_to_make)

ing_name = []
ing_type = []

for m in m2m_set:
    ind = names.index(m)
    ing_list = ingredients[ind]

    for ing in ing_list:
        line = ing.split(',')
        name = line[1].strip()
        itype = line[2].strip()

        ing_name.append(name)
        ing_type.append(itype)

df = pd.DataFrame({'name': ing_name, 'type': ing_type})
df['name'] = df['name'].str.capitalize() 
df = df.drop_duplicates('name')
df = df.sort_values('type')

print()
print(df.to_markdown(index=False))
