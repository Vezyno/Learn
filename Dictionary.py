
enemy = {
    'lock_x': 70,
    'lock_y': 45,
    'color': 'green',
    'health': 100,
    'name': 'mudillo',
    'awards': ['stalin', 'lenina']
}
print(enemy['lock_x'])

enemy['rank'] = 'admiral'
del enemy['rank']

enemy['lock_x'] += 10
print(enemy)
print(enemy.keys())
print(enemy.values())

all_enemies = []
for x in range(10):
    all_enemies.append(enemy.copy())

all_enemies[5]['health'] = 30
print(all_enemies)
for ene in all_enemies:
    print(ene)