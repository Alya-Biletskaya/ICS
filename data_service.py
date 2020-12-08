""" модуль для доступу до вхідних даних та перегляду даних
"""



def get_clients():
    """отримує данні по курсу

    Returns:
        clients_list : список курсу гривні до валют іноземних країн
    """

    from_file = [
       "103;5,65;6,05;10,03;2003"
        "104;1,13;1,23;2,00;2003"
        "105;2,28;2,52;4,12;2003"
        "106;2,02;2,24;3,66;2003"
        "109;2,68;3,18;5,12;2003"
        "111;3,34;3,96;6,53;2003"
        "103;1,10;11,21;13,50;2004"
        "104;2,50;2,60;2,75;2004"
       "105;4,44;4,65;4,70;2004"
        "106;4,05;4,25;4,50;2004"
        "109;6,05;6,30;6,80;2004"
        "111;7,00;7,25;7,50;2004"
        "103;13,64;13,70;13,80;2005"
        "104;2,80;2,83;2,85;2005"
        "105;4,75;4,80;4,85;2005"
        "106;4,62;4,64;4,66;2005"
        "109;6,90;6,95;7,00;2005"
        "111;7,65;7,75;7,85;2005",
    ]

    # накопичувач рядків
    clients_list = []

    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list


def get_orders():
    """повертає список накладних

    Returns:
        from_file: список накладних
    """

    from_file = [
        "1 англійський фунт стерлінг;103;2003;565,46;604,57;1,07;1003,17;1,66;1,77"
        "1 англійський фунт стерлінг;103;2004;110,25;1120,60;10,16;1350,40;1,21;12,25" 
        "1 англійський фунт стерлінг;103;2005;1364,20;1370,10;1,00;1380,15;1,01;1,01"
        "10 бельгійських франків;104;2003;113,03;122,60;1,08;200,38;1,63;1,77"
        "10 бельгійських франків;104;2004;250,45;260,45;1,04;275,20;1,06;1,10"
        "10 бельгійських франків;104 2005;280,10;283,40;1,01;285,10;1,01;1,02"
        "1 німецька марка;105;2003;227,91;252,07;1,11;412,02;1,63;1,81"
        "1 німецька марка;105;2004;444,23;465,40;1,05;470,20;1,01;1,06"
        "1 німецька марка;105;2005;475,23;480,30;1,01;485,20;1,01;1,02"
        "1 голандський гульден;106 2003;202,42;224,00;1,11;366,26;1,64;1,81" 
        "1 голандський гульден;106 2004;405,05;425,35;1,05;450,30;1,06;1,11"
        "1 голандський гульден;106 2005;462,20;464,10;1,00;466,15;1,00;1,01"
        "1 канадський долар;109;2003;267,88;318,00;1,19;511,92;1,61;1,91"
        "1 канадський долар;109;2004;605,20;630,15;1,04;680,25;1,08;1,12"
        "1 канадський долар;109;2005;690,10;695,15;1,01;699,80;1,01;1,01"
        "1 долар США;111;2003;334,00;396,00;1,19;652,62;1,65;1,95" 
        "1 долар США;111;2004;700,30;725,15;1,04;750,10;1,03;1,07"
        "1 долар США;111;2005;765,15;775,10;1,01;785,20;1,01;1,03"
    ]

    # розбити строку на реквізити та перетворити формати (при потребі)
    orders_list = []    # список-накопичувач
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list





def show_clients(clients):
    """виводить список валюти за заданої умови

    Args:
        clients : сприсок валюти
    """

    client_code_from = input("З якого кода валюти? ")
    client_code_to   = input("По який кода валюти? ")
    
    for client in clients:
        if  client_code_from  <= client[0] <= client_code_to:
            print( "код: {:4} назва: {:18} адреса: {:20}".format(client[0], client[1], client[2]))


# clients = get_clients()
# show_clients(clients)

orders = get_orders()
for o in  orders:
    print(o)