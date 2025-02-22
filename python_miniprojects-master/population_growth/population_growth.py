current_population = 380123456
born_seconds = 6
die_seconds = 12
imigrate_seconds = 40
seconds_in_year = 31536000

people_born = int(seconds_in_year / born_seconds)
people_die = int(seconds_in_year / die_seconds)
people_imigrate = int(seconds_in_year / imigrate_seconds)
first_year_population = current_population + people_born + people_imigrate - people_die
second_year_population = first_year_population + people_born + people_imigrate - people_die
third_year_population = second_year_population + people_born + people_imigrate - people_die

print(first_year_population)
print(second_year_population)
print(third_year_population)