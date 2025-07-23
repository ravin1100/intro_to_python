# Simple list creation
# Filtering conditions (e.g., only even numbers)
# Nested loops (e.g., combinations or matrix flattening)

squares = [i*i for i in range(10)]
print(squares)

filtered = [i*i for i in range(10) if i%2==0]
print(filtered)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
nested = [num for row in matrix for num in row]
print(nested)


word = "elephant"

letters = [i for i in word]
print(letters)

vowels = [i for i in letters if i in 'aeiou']
print(vowels)

consonants = [i for i in word if i not in 'aeiou']
print(consonants)

cities = ["jaipur", "kota", "sikar", "bengaluru", "hyderabad", "delhi"]

upper_city = [city.upper() for city in cities if len(city)>6]
print(upper_city)

upper_city = [city.upper() if len(city)>6 else city for city in cities ]
print(upper_city)

filterd = [city.upper() for city in cities if len(city) <6]
print(filterd)



# output
# =============
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 4, 16, 36, 64]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ['e', 'l', 'e', 'p', 'h', 'a', 'n', 't']
# ['e', 'e', 'a']
# ['l', 'p', 'h', 'n', 't']
# ['BENGALURU', 'HYDERABAD']
# ['jaipur', 'kota', 'sikar', 'BENGALURU', 'HYDERABAD', 'delhi']
# ['KOTA', 'SIKAR', 'DELHI']