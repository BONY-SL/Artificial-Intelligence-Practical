person = {"name": "Jessa", "country": "USA"}

# updating the country name
person["country"] = "Canada"

# print the updated country
print(person['country'])

# updating the country name using update() method
person.update({"country": "USA"})

# print the updated country
print(person['country'])
