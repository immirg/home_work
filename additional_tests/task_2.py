import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

'''
1) Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
'''


def palindrome_check(word):
    """
    check the entered word for a palindrome
    :param word: word that should be checked for palindrome
    if the entered word is a palindrome then '+' is printed otherwise '-'
    """
    return '+' if word == word[::-1] else '-'


# word = input('>>> ')
# print(palindrome_check(word=word))

'''
2) Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити:
- в адресі є тільки 1 '@', після '@' йде тільки 1 '.'
Не використовувати RE
Якщо умови виконані, то вивести "пошта валідна", інкше вивести "пошта не валідна"
'''


def check_email(email):
    """
    checking email for correctness
    :param email: incoming email for verification
    :return: if the email is correct it returns 'Mail is valid' otherwise 'Mail is not valid'
    """
    at_count = email.count('@')
    if at_count != 1:
        return 'Mail is not valid'

    at_id = email.find('@')
    domain_parts = email[at_id+1:]
    if domain_parts.count('.') < 1:
        return 'Mail is not valid'

    if len(domain_parts[:at_id]) < 2:
        return 'Mail is not valid'

    domain = domain_parts.split('.')
    if len(domain) < 2:
        return 'Mail is not valid'

    for elem in domain:
        if len(elem) < 2:
            return 'Mail is not valid'

    return 'Mail is valid'


# email = input('>>> ')
# print(check_email('asd@asd.com'))
# print(check_email('d@asd.com'))
# print(check_email('asd@asd.'))
# print(check_email('asd@.'))
# print(check_email('@.'))


'''
3) Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
складається з 4 чисел (а не літер чи інших символів)
числа розділені точкою
кожне число в діапазоні від 0 до 255 Якщо адреса неправильна, виводьте повідомлення: «Неправильна IP-адреса». 
Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
'''


def check_ip(ip: str):
    """
    check that the IP address consists of 4 numbers in the range from 0 to 255 and the numbers are separated by a dot
    :param ip: IP for verification
    :return: If the address is correct 'Correct IP address' otherwise 'Incorrect IP address'
    """
    list_ip = ip.split('.')
    if ip.count('.') != 3 or len(list_ip) != 4:
        return 'Incorrect IP address'

    for index, elem in enumerate(list_ip):
        if not elem or list_ip[index][0] == '0' and len(list_ip[index]) > 1:
            return 'Incorrect IP address'

    for k in list_ip:
        if not k.isdigit() or int(k) > 255:
            return 'Incorrect IP address'
    return 'Correct IP address'


# print(check_ip('17.172.224.47'))
# print(check_ip('07.172.224.0'))
# print(check_ip('07.172.224.'))


if __name__ == '__main__':
    unittest.main()
