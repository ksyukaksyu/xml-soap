import osa

URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
client1 = osa.client.Client(URL)


def get_average_temp(filename):
    with open(filename) as file:
        file_data = file.readlines()
        file_data_list = [x.strip() for x in file_data]
        response = 0
        for temp in file_data_list:
            response += client1.service.ConvertTemp(Temperature=temp.split()[0],
                                                    FromUnit='degreeFahrenheit',
                                                    ToUnit='degreeCelsius')
        print('Average temp in Celsius: {}'.format(response/len(file_data_list)))

        # или можно сначала посчитать среднее в фаренгейтах, а потом перевести в цельсий (так менее красиво, но
        # зато только один запрос к сервису):
        total_temp = 0
        for temp in file_data_list:
            total_temp += int(temp.split()[0])
        average_temp = total_temp / len(file_data_list)
        response_2 = client1.service.ConvertTemp(Temperature=average_temp,
                                                    FromUnit='degreeFahrenheit',
                                                    ToUnit='degreeCelsius')
        print(response_2)




get_average_temp('./txt/temps.txt')
