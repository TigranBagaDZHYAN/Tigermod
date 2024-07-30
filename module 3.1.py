calls = 0
def count_calls ():# Создаём функцию count_calls
    global calls
    calls+=1

def string_info (string):# Создаём функцию string_info
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains (string, list_to_search):# Создаём функцию is_contains с двумя параметрами cтрока и список
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybara'))  # Вывод результата
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)