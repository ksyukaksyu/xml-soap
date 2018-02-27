import osa

URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
client1 = osa.client.Client(URL)

with open('./txt/temps.txt') as file:
    file_data = file.readlines()
    file_data_list = [x.strip() for x in file_data]
    print(file_data_list)
    c = 0
    response = 0

    for temp in file_data_list:
        response += client1.service.ConvertTemp(Temperature=temp.split()[0],
                                                FromUnit='degreeFahrenheit',
                                                ToUnit='degreeCelsius')
        c += 1

    print(response/c)
    # или можно сначала посчитать среднее в фаренгейтах, а потом перевести в цельсий
