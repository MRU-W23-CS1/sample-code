cities = ["Edmonton", "Fort McMurray", "Calgary", "Red Deer"]
population = [712_391, 76_000, 1_019_942, 73_593]
print(cities)
print(population)

biggest_pop = population[0]
biggest_city = cities[0]

for i in range(len(cities)): # equivalent to range(0, len(cities), 1)
    if population[i] > biggest_pop:
        biggest_pop = population[i]
        biggest_city = cities[i]

print(f"The biggest city is {biggest_city}")