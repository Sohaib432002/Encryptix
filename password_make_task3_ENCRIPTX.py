import random

print('For a strong Password you must have to apply these conditions:')
print('1-your Password must contain capital letters.')
print('2-It must contain numbers.')
print('3-It must contain special symbols like @#$%.')
print('4-Your password must be at least 8 characters long.')


class PasswordGenerator:
    def __init__(self, length, use_uppercase=True, use_numbers=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special = use_special
        self.lowercase_alpha = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_uppercase else ''
        self.numbers = '1234567890' if use_numbers else ''
        self.special_char = '~!@#$%^&*)_|}?/' if use_special else ''

    def generate_password(self):
        if self.length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        all_chars = self.lowercase_alpha + self.uppercase_alpha + self.numbers + self.special_char
        if not all_chars:
            raise ValueError("At least one type of character must be selected.")

        password = ''.join(random.choice(all_chars) for _ in range(self.length))
        return password


def main():
    choice = input('Do you want to generate a password automatically? yes-press(y)/no-press(n): ')

    if choice.lower() == 'y':
        try:
            length = int(input('Enter the desired length of the password (at least 8): '))
            use_uppercase = input('Include uppercase letters? yes-press(y)/no-press(n): ').lower() == 'y'
            use_numbers = input('Include numbers? yes-press(y)/no-press(n): ').lower() == 'y'
            use_special = input('Include special characters? yes-press(y)/no-press(n): ').lower() == 'y'

            generator = PasswordGenerator(length, use_uppercase, use_numbers, use_special)
            password = generator.generate_password()
            print(f"Your generated password is: {password}")
        except ValueError as ve:
            print(f"Error: {ve}")
    elif choice.lower() == 'n':
        password = input('Enter your password:  ')

        validator = PasswordValidator(password)
        password = validator.special_char_checker()
        password = validator.upper_level_checker()
        password = validator.numbers_checker()
        password = validator.length_checker()

        print(f'So your password is {password}')
    else:
        print('Invalid choice')


class PasswordValidator:
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', "(", ")", "_", "+"]

    def __init__(self, password):
        self.password = password

    def special_char_checker(self):
        temp = False
        stop = False
        while not stop:
            for i in self.password:
                if i in self.special_char:
                    print('Your password contains special characters.')
                    temp = False
                    stop = True
                    break
                elif i not in self.special_char:
                    temp = True
            if temp:
                self.password = input('For a Strong password  please Again enter a password which must contain a special character: ')
            else:
                stop = True
        return self.password

    def upper_level_checker(self):
        temp = False
        stop = False
        while not stop:
            for i in self.password:
                if i.isupper():
                    print('Your password contains upper level characters.')
                    temp = False
                    stop = True
                    break
                elif not i.isupper():
                    temp = True
            if temp:
                self.password = input('For a Strong password  please Again enter a password which must contain an upper-level character: ')
            else:
                stop = True
        return self.password

    def numbers_checker(self):
        temp = False
        stop = False
        while not stop:
            for i in self.password:
                if i.isdigit():
                    print('Your password contains numbers.')
                    temp = False
                    stop = True
                    break
                elif not i.isdigit():
                    temp = True
            if temp:
                self.password = input('For a Strong password  please Again enter a password which must contain a number: ')
            else:
                stop = True
        return self.password

    def length_checker(self):
        temp = False
        stop = False
        while not stop:
            if len(self.password) >= 8:
                stop = True
                temp = False
            else:
                temp = True
            if temp:
                self.password = input('For a Strong password  please Again enter a password which must be at least 8 characters long: ')
            else:
                stop = True
        return self.password


if __name__ == "__main__":
    main()
