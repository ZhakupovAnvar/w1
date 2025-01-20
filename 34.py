import random
import string
'''#1
for i in range (3):
    print(random.randrange(100, 999, 5))

#2
def generate(num_tickets=100):
    tickets = set()
    while len(tickets) < num_tickets:
        ticket = str(random.randint(10**9, 10**10 - 1))  
        tickets.add(ticket)
    return list(tickets)

def pick_lucky_tickets(tickets, num_winners=2):
    return random.sample(tickets, num_winners)

tickets = generate()
lucky_tickets = pick_lucky_tickets(tickets)

print("Generated Tickets:", tickets)
print("Lucky Tickets:", lucky_tickets)

#3
def get_string():
    letters=string.ascii_lowercase
    result=''.join(random.choice(letters) for i in range (1))
    print(result)

get_string()

#4
def get_5():
    letters=string.ascii_letters
    result=''.join(random.choice(letters) for i in range (5))
    print(result)

get_5()

#5
def generate_password(length=10):
    uppercase_letters = random.sample(string.ascii_uppercase, 2)  
    digits = random.sample(string.digits, 1)                     
    special_symbols = random.sample(string.punctuation, 1)        
    remaining_length = length - (len(uppercase_letters) + len(digits) + len(special_symbols))

    lowercase_letters = random.choices(string.ascii_letters, k=remaining_length)
    password_list = uppercase_letters + digits + special_symbols + lowercase_letters
    
    return ''.join(password_list)

password = generate_password()
print(password)

#6
first=random.uniform(0.1,1)
second=random.uniform(9.5, 99.5)
print(first)
print(second)
print(first*second)

#7
numbers_of_dice=[1, 2, 3, 4, 5, 6]
state=random.getstate()
random.setstate(state)
print(random.sample(numbers_of_dice, k=1))

random.setstate(state)
print(random.sample(numbers_of_dice, k=1))

random.setstate(state)
print(random.sample(numbers_of_dice, k=1))

random.setstate(state)
print(random.sample(numbers_of_dice, k=1))

random.setstate(state)
print(random.sample(numbers_of_dice, k=1))

#8
def generate_custom_random_string(letters, length):
    return ''.join(random.choice(letters) for _ in range(length))

specific_letters = "ANVAR"  
string_length = 5
random_string = generate_custom_random_string(specific_letters, string_length)

print("Random String:", random_string)

#9
def generate_unique_random_string(characters, length):
    return ''.join(random.sample(characters, length))

allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
string_length = 8  
random_string = generate_unique_random_string(allowed_characters, string_length)

print(random_string)'''

#10
