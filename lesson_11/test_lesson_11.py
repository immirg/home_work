import logging
import pytest
from datetime import datetime

"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""


def read_file(time, log_level, massage):
    """
    the correctness of the last log written to the file is checked
    :param time: time of recording in log to file
    :param log_level: logging level
    :param massage: message text
    """
    expected_result = f'{time} - {log_level} - {massage}'
    with open('login_system.log', 'r') as file:
        text_in_file = file.readlines()
        len_text_file = len(text_in_file)
        actual_result = text_in_file[len_text_file-1]
        # [:-1] для удаления в конце строки \n
        assert actual_result[:-1] == expected_result


@pytest.mark.parametrize('username, status', [
    ('Bob', 'success'),
    ('Bill', 'expired'),
    ('Eva', 'failed'),
])
def test_log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format=f'{current_time} - %(levelname)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

    log_name = None
    if status == 'success':
        log_name = 'INFO'
    elif status == 'expired':
        log_name = 'WARNING'
    elif status == 'failed':
        log_name = 'ERROR'

    read_file(time=current_time, log_level=log_name, massage=log_message)




