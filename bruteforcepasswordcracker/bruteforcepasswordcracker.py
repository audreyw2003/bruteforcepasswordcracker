import itertools
import secrets
import string

def save_pass_list(pass_list):
    with open("passwordlist.txt", "w") as file:
        for i in pass_list:
            file.write(f'{i}\n')
    return 'Generated passwords saved to passwordlist.txt.'
def brute_force(target_password, num_passwords):
    pass_list = generate_passwords(num_passwords)
    save_pass_list(pass_list)
    for i in pass_list:
        if (i==target_password):
            return target_password
    return None

def generate_passwords(num_passwords):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pass_list = []
    count = 0
    while(count< num_passwords):
        password = ''
        for i in range(0,15):
            password += ''.join(secrets.choice(alphabet))
        pass_list.append(password)
        count+=1
    return pass_list

def main():
    target_password = input("Enter password to attempt brute force on: ")
    num_passwords = int(input("Enter number of passwords to generate for comparison during brute force: "))
    result = brute_force(target_password, num_passwords)
    if result:
        print('Password cracked.')
    else:
        print('Password not cracked.')

main()