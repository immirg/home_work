'''
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
'''


def counting_numbers_in_a_list(list_num: list):
    """
    A function to count the sum of the numbers in each element of the list.
    if there are non-numeric characters, displays an error message.
    :param list_num: List of strings with numbers separated by commas.
    :return: Returns nothing, but prints the result for each element of the list
    """
    for elem in list_num:
        sum_num = 0
        elem = elem.split(',')
        try:
            for j in elem:
                sum_num += int(j)
            print(sum_num)
        except ValueError:
            print('Can\'t do it!')
            continue


list_of_numbers = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
counting_numbers_in_a_list(list_num=list_of_numbers)
