person = {"name": "Jessa", "country": "USA", "telephone": 1178}
# Iterating the dictionary using for-loop
print('key', ':', 'value')

for key in person:
    print(key, ':', person[key])

# using items() method
print('key', ':', 'value')

for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])
