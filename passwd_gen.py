import itertools

def generate_passwords(adjectives_file, animals_file, output_file):
    with open(adjectives_file, 'r') as file:
        adjectives = [line.strip().lower() for line in file if line.strip()]

    with open(animals_file, 'r') as file:
        animals = [line.strip().lower() for line in file if line.strip()]

    with open(output_file, 'w') as file:
        for adjective, animal in itertools.product(adjectives, animals):
            for i in range(100):
                number = f"{i:02d}"
                # Generate all four variations
                passwords = [
                    f"{adjective}{animal}{number}",  # All lowercase
                    f"{adjective.capitalize()}{animal}{number}",  # Adjective capitalized
                    f"{adjective}{animal.capitalize()}{number}",  # Animal capitalized
                    f"{adjective.capitalize()}{animal.capitalize()}{number}"  # Both capitalized
                ]
                for password in passwords:
                    file.write(password + '\n')

# Adjust these file paths according to your setup
adjectives_file = 'Cleaned_Adjectives1.txt'
animals_file = 'Cleaned_Animals1.txt'
output_file = 'output_passwords.txt'

generate_passwords(adjectives_file, animals_file, output_file)
