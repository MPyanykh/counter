calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    result1 = (len(string), string.upper(), string.lower())
    return (result1)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

print(string_info('Hello, world!!'))
print(is_contains('Urbanist', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('python', ["Java", "C++", "Python"]))

print ('Итого вызовов функций:', calls)




