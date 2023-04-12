# Функція, що описує атаку зомбі на рослин
# Повертає True, якщо захисники перемогли
def plants_with_zombie(zombies, plants):

    # Визначаємо кількість елементів у більшому масиві і різницю кількості елементів
    # Також доповнюємо менший масив значеннями 0
    length_zombies = len(zombies)
    length_plants = len(plants)
    j = 0
    different = 0
    if length_zombies > length_plants:
        length_max = length_zombies
        different = length_zombies - length_plants
        while j < different:
            plants.append(0)
            j = j+1
    else:
        length_max = length_plants
        different = length_plants - length_zombies
        while j < different:
            zombies.append(0)
            j = j+1

    start_attack_zombie = 0
    start_attack_plants = 0
    number_alive_zombie = 0
    number_alive_plants = 0
    i = 0
    # Зомбі атакують рослин з тим самим індексом масиву
    while i < length_max:
         # Розраховуємо початкову силу атаки зомбі і рослин
         start_attack_zombie = start_attack_zombie + zombies[i]
         start_attack_plants = start_attack_plants + plants[i]

         # Виживає число з більшим значенням, якщо одинакові, то гинуть обоє
         if zombies[i] > plants[i]:
             plants[i] = 0
         elif plants[i] > zombies[i]:
             zombies[i] = 0
         else:
             zombies[i] = 0
             plants[i] = 0

         # Рахуємо кількість виживших рослин і зомбі
         if zombies[i] != 0:
             number_alive_zombie = number_alive_zombie + 1
         if plants[i] != 0:
             number_alive_plants = number_alive_plants + 1
         i = i + 1

    # Визначаємо, яка команда перемогла
    if number_alive_zombie > number_alive_plants:
        result = False
    elif number_alive_zombie < number_alive_plants:
        result = True
    else:
         if start_attack_zombie > start_attack_plants:
             result = False
         elif start_attack_zombie < start_attack_plants:
             result = True
         else:
             result = True
    return result



zombies1 = [1, 3, 5, 7]
plants1 = [2, 4, 6, 8]
print(plants_with_zombie(zombies1, plants1))
zombies1 = [1, 3, 5, 7]
plants1 = [2, 4]
print(plants_with_zombie(zombies1, plants1))
zombies1 = [1, 3, 5, 7]
plants1 = [2, 4, 0, 8]
print(plants_with_zombie(zombies1, plants1))
zombies1 = [2, 1, 1, 1]
plants1 = [1, 2, 1, 1]
print(plants_with_zombie(zombies1, plants1))