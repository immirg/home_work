import logging
from datetime import datetime, timedelta

console_out = logging.StreamHandler()
file_log = logging.FileHandler('hb_test.log')
logging.basicConfig(handlers=(file_log, console_out), level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(message)s')


def read_time(line):
    tm = line[line.find('Timestamp') + 10: line.find('Key') - 1]
    return datetime.strptime(tm, '%H:%M:%S')


def check_time(lines):
    len_lines = len(lines)
    for index in range(len_lines-1):
        current_time = read_time(lines[index])
        next_time = read_time(lines[index+1])
        interval = current_time - next_time
        if timedelta(seconds=33) > interval >= timedelta(seconds=31):
            logging.warning(f'Interval between heartbeats at {current_time.time()} and {next_time.time()} was '
                            f'{(current_time-next_time).seconds} seconds, which is greater than expected')
        if interval >= timedelta(seconds=33):
            logging.error(f'  Interval between heartbeats at {current_time.time()} and {next_time.time()} was '
                            f'{(current_time-next_time).seconds} seconds, which is greater than expected')


def filter_lines_by_key(key):
    filtered_lines = []
    with open('hblog.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            value = line[line.find('Key') + 4: line.find('TradePrice') - 1]
            if value == key:
                filtered_lines.append(line)
    check_time(filtered_lines)


if __name__ == "__main__":
    filter_lines_by_key(key='TSTFEED0300|7E3E|0400')
