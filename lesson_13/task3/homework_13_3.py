import logging
import xml.etree.ElementTree as ET

tree = ET.parse('groups.xml')
root = tree.getroot()

logging.basicConfig(level=logging.INFO, format='%(asctime)s, -%(levelname)s, -%(message)s', filename='json_logs.log')


# def function(num):
#     for groups in root:
#         if groups[0].text == str(num):
#             for elem in groups:
#                 if elem.tag == 'timingExbytes':
#                     for child in elem:
#                         if child.tag == 'incoming':
#                             return logging.info(f'{child.text} parameter for number {num}')
#             return logging.info(f'There is no incoming parameter for number {num} ')
#     return logging.info(f'In the XML document number {num} is missing')


def function(num):
    for groups in root:
        if groups.find('number').text == str(num):
            if groups.find('timingExbytes'):
                timing_exbytes = groups.find('timingExbytes')
                if timing_exbytes.find('incoming').tag:
                    incoming = timing_exbytes.find('incoming')
                    return logging.info(f' {incoming.text} parameter for number {num}')
            return logging.info(f' There is no incoming parameter for number {num} ')
    return logging.info(f' In the XML document number {num} is missing')


for i in range(5+1):
    function(i)
