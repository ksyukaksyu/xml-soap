import osa

URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
client1 = osa.client.Client(URL)

URL2 = 'http://www.webservicex.net/length.asmx?WSDL'
client2 = osa.client.Client(URL2)


def read_file_in_list(filename):
    with open(filename) as file:
        file_data = file.readlines()
        file_data_list = [x.strip() for x in file_data]
        return file_data_list


def get_average_temp(filename):
    file_data_list = read_file_in_list(filename)
    response = 0
    for temp in file_data_list:
        response += client1.service.ConvertTemp(Temperature=temp.split()[0],
                                                FromUnit='degreeFahrenheit',
                                                ToUnit='degreeCelsius')
    print('Average temp in Celsius: {}'.format(response / len(file_data_list)))

    # или можно сначала посчитать среднее в фаренгейтах, а потом перевести в цельсий (так менее красиво, но
    # зато только один запрос к сервису):
    total_temp = 0
    for temp in file_data_list:
        total_temp += int(temp.split()[0])
    average_temp = total_temp / len(file_data_list)
    response_2 = client1.service.ConvertTemp(Temperature=average_temp,
                                             FromUnit='degreeFahrenheit',
                                             ToUnit='degreeCelsius')
    print('Average temp in Celsius (2): {}'.format(response_2))


def get_way_len(filename):
    file_data_list = read_file_in_list(filename)
    total_way = 0
    for way_len in file_data_list:
        total_way += float(way_len.split()[1].replace(',', ''))

    print('Total way in Kilometers: {0:.2f}'.format(client2.service.ChangeLengthUnit(LengthValue=total_way,
                                                                                     fromLengthUnit='Miles',
                                                                                     toLengthUnit='Kilometers')))


get_average_temp('./txt/temps.txt')
get_way_len('./txt/travel.txt')
