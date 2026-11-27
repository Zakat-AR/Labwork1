import random
from Logs import logger_graph


def log_graph(*args):
    """Записує повідомлення графа в лог одним коректно сформованим рядком."""
    logger_graph.info(" ".join(map(str, args)))
#Списки для ребер і вузлів графа
list_cities = []
list_roads = []
list_to_get_roads = []

#Налаштування класу вузлів(міст) графа
class cities ():
    def __init__(self , name , id_of_city , number_of_roads):
        self.name = name
        self.id_of_city = id_of_city
        self.number_of_roads = number_of_roads


#Налаштування класу ребер(доріг) графа
#id1 = номер міста , з якого починається дорога
#id2 = номер міста , на якому закінчується дорога
class roads():
    
    def __init__(self ,name ):
        self.name = name
        self.id1 = None
        self.id2 = None
        self.lenght = None

    def another_characteristics(self , id1 , id2 = False , lenght=0 ):
        self.id1 = id1
        self.id2 = id2
        self.lenght = lenght

#Рандом на кількість місць
number_of_cities = random.randint(25,26)
#Список імен на майбутній рандом назв
names = ["Лаугвуг","Сьонкай","Хват","Алкай","Ротрам","Фьорн","Лакран","Іградсиль","Азерот","Стратхольм","Дуратар",
         "Рль'єх","Харків","Лиманськ","Москва","Київ","Александрія","Афіни","Мордор","Гондор","Морія","Севастополь",
         "Заполярний","Азабат","Вашингтон","Пекін","Мотовилівка","Чигирин","Мен","Париж","Мінськ","Варшава","Лондон",
         "Червоноград","Ленінград","Сталінград","Петроград","Станіславград","Доброград","Злоград","Градоград","Градосніг","Градодощ","Градотуман",
         "Львів","Вінниця","Полтава","Миколаїв","Одеса","Рівне","Івано-Франківськ","Дніпропетровськ","Донецьк","ЛУганськ","Маріуполь",
         "Астрахань","Кузбаз","Альфан","Чокротиз","Іркутськ","Тюмень","Магнітогорськ","Петрозаводськ","Чок-Алай","Чок-Фан","Чок-Клак"]
number__roads = 0

road_names = ["Q","W","E","R","T","Y","U",
              "I","O","P","A","S","D","F",
              "G","H","J","K","L","Z","X",
              "C","V","B","N","M"]
#Налаштування міст
for number in range (number_of_cities):
    id_city = number 
    city_name = random.choice(names)
    roads_to_city = random.randint(5,25)
    number__roads += roads_to_city

    if number == number_of_cities -1 and number__roads % 2 != 0:
        roads_to_city += 1
        number__roads +=1
        

    #Даємо дорозі ім'я
    for number_road in range(roads_to_city):
        road_name = random.choice(road_names)

        
        #Утворюємо дорогу і зберігаємо у списку
        road = roads(road_name)
        list_roads.append(road)
    
    #Утворюємо місто і зберігаємо його у списку
    city = cities(city_name ,id_city , roads_to_city)
    list_cities.append(city)
    
    

    #Списки для зберігання і порівняння кількості доріг
    list_for_input = [0]
    list_for_comparing = [roads_to_city]
    list_with_city_number = [ list_for_input , list_for_comparing ]
    list_to_get_roads.append(list_with_city_number)



# Налаштування оріг на основі айді(номерів) міст
all_roads = 0
created_roads = 0
for number_city in range (number_of_cities):

    #Беремо число доріг для одного міста
    city = list_cities[number_city]
    number_roads = city.number_of_roads
    all_roads += number_roads

    
    #Налаштовуємо дороги для одного міста
    for number in range (all_roads -number_roads , all_roads ):

        #Беремо значення знайдених і досткпних доріг для міста
        list_with_city_number = list_to_get_roads[number_city]
        list_for_input = list_with_city_number[0]
        list_for_comparing = list_with_city_number[1]
        count_while = 0

        
        road = list_roads[number]
        
        #Умова на нову дорогу  
        if list_for_input[0] < list_for_comparing[0] :
            list_for_input[0] += 1
            id_road_1 = number_city
            id_road_2 = False

            #Випадкове значення відстані
            distance = random.randint(1,125)

            #Шукаємо друге місто до однієї дороги
            while id_road_2 == False:
                count_while +=1
                    
                id_road_2 = random.randint(1,number_of_cities)
                id_road_2 -= 1

                #Дорога не веде до тогож міста
                if id_road_2 == id_road_1 :
                    id_road_2 = False
                    
                          
                #Якщо дорога інша , то наступна перевірка
                elif id_road_2 !=  id_road_1:
                    list_with_city_number = list_to_get_roads[id_road_2 ]
                    list_for_input = list_with_city_number[0]
                    list_for_comparing = list_with_city_number[1]


                    #Дорогу можна додати , лише за наявності вільного слоту                         
                    if list_for_input[0] < list_for_comparing[0]:
                        list_for_input[0] +=1
                        created_roads +=1
                        road.another_characteristics(id_road_1 ,id_road_2 , distance )
                    else:
                        id_road_2 = False

                #Щоб не залишитись на вічно у циклі               
                if count_while > 25:
                    id_road_2 = True          
                        

#Перевірка отриманих результатів
correct_ways = []
log_graph(all_roads, "Roads_num")
log_graph(number_of_cities ,"Cities_num")
for x in range (all_roads):
    road = list_roads[x]
    distance1 = road.id1
    distance2 = road.id2

    #Відбірка шляхів , які підходять    
    if distance1 != None and distance2 != None:
        log_graph(distance1 , distance2 , road.name , road.lenght )
        correct_ways.append(road)

#Детальна перевірка
log_graph("Заплановано слотів:", all_roads)
log_graph("Створено доріг:", created_roads)
log_graph("Зайнято слотів:", sum(x[0][0] for x in list_to_get_roads))
log_graph("Кількість об'єктів:", len(list_roads))

for city in list_cities:
    count_roads = 0

    for road in list_roads:
        if road.id1 == city.id_of_city or road.id2 == city.id_of_city:
            count_roads += 1

    log_graph(
        city.name,
        "ID:", city.id_of_city,
        "Очікується:", city.number_of_roads,
        "Фактично:", count_roads )


def get_distance(correct_ways, list_cities, list_to_get_roads , last_city):
    #Зазначаємо початкову точку обрахунку
    required_city = random.randint(1,number_of_cities - 1)
    our_city = list_to_get_roads[required_city]
    list_ = our_city[0]
    all_roads = list_[0]
    starting_city = last_city
    previous_city = -1

    #Списки з інформацією про можливі шляхи , минулі вузли , чинні вузли
    interesting_ways = []
    previous_cities = []
    starting_cities = []

    #Списки-прокладки , які будуть змінюватись , поки основні дають дані для циклів
    list_for_input_ways = []
    list_for_input_previous = []
    list_for_input_starting = []

    #Лічильники для умов уникнення петель та закінчення циклу
    counter_1 = 0
    counter_2 = 0

    routes = []
    jeneral_result = 0
    count = 0
    count_adding = 0

    possible_name = ""
    name_for_compare = ""
    #len(routes) < all_roads

    #Початок циклу
    while  count < 100   :

        count +=1

        jeneral_result = -1
        #print("ARS")

        #Очищуємо списки перед початком роботи
        interesting_ways.clear()
        previous_cities.clear()
        starting_cities.clear()

        #Шукаємо дороги , які з'єднані з початковим вузлом
        for one_road in range (len(correct_ways)):
            road = correct_ways[one_road]

            #Беремо айді цих доріг
            road_id_1 = road.id1
            road_id_2 = road.id2


            #Умови потенціально правильної дороги
            qiute_difficult_logic_a = road_id_1 == starting_city  and road_id_2 != previous_city
            qiute_difficult_logic_b = road_id_2 == starting_city  and road_id_1 != previous_city


            #Збереження дороги
            if qiute_difficult_logic_a :

                #Створюємо окремий список для цієї дороги
                special_list_roads = []
                special_list_roads.append(road)

                #Зберігаємо цей список та оновлюєм значення минулого та чинного вузлів
                interesting_ways.append(special_list_roads)
                previous_city = road_id_1
                starting_city = road_id_2


                #Створюємо списки для збереження оновлених чинних і минулих вузлів
                special_list_previous = []
                special_list_starting = []

                #Зберігаємо нові значення
                special_list_previous.append(previous_city)
                special_list_starting.append(starting_city)

                #Зберігаємо списки
                previous_cities.append(special_list_previous)
                starting_cities.append(special_list_starting)



                starting_city = 0
                previous_city = -1

            #Цей блок має аналогічну логіку , лише значення минулого та чинного списків обмінялись місцями.
            #Причиною цього блоку є те , що не всі дороги будуть підключені до міста/вузла , на якому ми знаходимось , та мати його номер своїм першим айді
            #Тобто , друге айді дороги до міста А не завжди дорівнює першому айді інших доріг з міста А    
            elif qiute_difficult_logic_b :

                special_list_roads = []
                special_list_roads.append(road)

                interesting_ways.append(special_list_roads)
                previous_city = road_id_2
                starting_city = road_id_1


                special_list_previous = []
                special_list_starting = []

                special_list_previous.append(previous_city)
                special_list_starting.append(starting_city)

                previous_cities.append(special_list_previous)
                starting_cities.append(special_list_starting)



                starting_city = 0
                previous_city = -1
        #Тут починається новий цикл на продевження шляхів , звкладених у попередньому/зовнішньому
        #На момент написання графу вважалось , що буде легше для розуміння ситуації і написання коду ;
        #-->  якщо обрахунок шляхів з першого міста та обрахунок їхніх продовжень будуть розділені
        # Тому логіка подальшого коду схожа на перший цикл , однак розрахована на довільну кількість пройдених вузлів.        
        while jeneral_result != required_city:

            #Очищення списків-прокладок перед кожною ітерацією
            list_for_input_ways.clear()
            list_for_input_previous.clear()
            list_for_input_starting.clear()


            #Перерахунок ребер , які задовольнили умови , щоб бути початком дороги до кінцевого вузла
            for road_ in range(len(interesting_ways)):

                #локальні/special списки додавались і будуть додаватись одночасно , через що ;
                #наприклад , 10-ий список доріг у подальшому коді буде працювати з 10-им списком усіх минулих вузлів
                #вони будуть мати не лише однакові номери , а й необхідні для правильного обрахування дані
                possible_road = interesting_ways[road_]
                starting_city_list = starting_cities[road_]


                #Для кожного списку правильного шляху будуть перебиратись усі дороги , аби знайти правильне продовження    
                for one_road in range (len(correct_ways)):

                    #Беремо останню/актуальну дорогу
                    #Беремо астульне значення поточного вузла
                    road = possible_road[-1]
                    starting_city = starting_city_list[-1]

                    #Беремо айді поточного вузла/мізла
                    testing_road = correct_ways[one_road]
                    road_id_1 = testing_road.id1
                    road_id_2 = testing_road.id2

                    #Беремо список минулих вузлів для даного шляху
                    previuos_city_list = previous_cities[road_]

                    for compare in range(len(previuos_city_list)):

                        id_previous_city = previuos_city_list[compare]

                        result_1 = road_id_1 != id_previous_city
                        result_2 = road_id_2 != id_previous_city


                        #Ідея: якщо ця дорога не дорівнює ні однму з минулих взлів , то кількість пройдених превірок = кількість пройдених вузлів
                        if result_1:

                            counter_1 +=1

                        if result_2:

                            counter_2 +=1



                    #Оновлена версія минулої умови потенціального правильного шляху
                    qiute_difficult_logic_a = road_id_1 == starting_city  and counter_2 == len(previuos_city_list)
                    qiute_difficult_logic_b = road_id_2 == starting_city  and counter_1 == len(previuos_city_list)

                    counter_1 = 0
                    counter_2 = 0


                    #Збереження дороги , що відповідає умовам
                    if qiute_difficult_logic_a :

                        #Логіка дій тут така:
                        #Беремо відповідний список (тобто , кожен список доріг відповідає певному вузлу) 
                        #Айді останньої дороги списку відповідає певному вузлу/місту
                        #Це ми можемо побачити по "for road in range(len(interesting_ways)):"
                        #Тобто , коли ми додаємо дорогу до списку потенціально-правильних
                        #Ми наче додаємо вузол , до якого вона веде , це видно по :
                        #starting_city = road_id_2/1 . Тепер відносно такого значення початкового міста ми роздивляємось усі
                        #--> потенціально-правильно шляхи і утворюємо нові списки для кожного з них , відбувається утворення похідних списків.
                        #Це реалізується тим , що ми беремо початковий список , додаємо нову дорогу , кидаємо цей список у список-прокладку
                        #Для іншої потенціальної дороги відносоно певного вузла ми знову беремо той же список з доріг , додаємо до нього поточну і додаємо до прокладки.
                        #Таким чином утворюється декілька списків , які різняться лише останнім елементом. 
                        special_list_roads = []

                        for x in range(len(possible_road)):
                            special_list_roads.append(possible_road[x])


                        special_list_roads.append(testing_road)
                        list_for_input_ways.append(special_list_roads)

                        #Оновлюємо значення минулоих міст і поточного
                        previous_city = road_id_1
                        starting_city = road_id_2



                        #Логіка аналогічна до збереження доріг , але тут йдеться про минулі вузли 
                        special_list_previous = []

                        for y in range(len(previuos_city_list)):
                            special_list_previous.append(previuos_city_list[y])


                        special_list_previous.append(previous_city)
                        list_for_input_previous.append(special_list_previous)


                        #Логіка аналогічна , але тут йдеться про поточні значення міста
                        special_list_starting = []

                        for z in range(len(starting_city_list)):
                            special_list_starting.append(starting_city_list[z])

                        special_list_starting.append(starting_city)
                        list_for_input_starting.append(special_list_starting)



                    #Логіка аналогічна до if , але ,як було сказано раніше, положення потрібних айді може бути різним .
                    elif qiute_difficult_logic_b :

                        special_list_roads = []

                        for x in range(len(possible_road)):
                            special_list_roads.append(possible_road[x])


                        special_list_roads.append(testing_road)
                        list_for_input_ways.append(special_list_roads)


                        previous_city = road_id_2
                        starting_city = road_id_1


                        special_list_previous = []

                        for y in range(len(previuos_city_list)):
                            special_list_previous.append(previuos_city_list[y])


                        special_list_previous.append(previous_city)
                        list_for_input_previous.append(special_list_previous)


                        special_list_starting = []

                        for z in range(len(starting_city_list)):
                            special_list_starting.append(starting_city_list[z])

                        special_list_starting.append(starting_city)
                        list_for_input_starting.append(special_list_starting)

                cheking = -1
                for u in range(len(list_for_input_starting)):


                    cheking_list = list_for_input_starting[u]
                    cheking = cheking_list[-1]

                    route_list_ = list_for_input_ways[u]


                    if cheking == required_city :

                        if len(routes) != 0:

                            possible_name = ""

                            for possible in range(len(route_list_)):
                                way_route = route_list_[possible]
                                possible_name += way_route.name

                            count_adding = 0

                            for comparing in range(len(routes)):
                                name_for_compare = ""
                                way = routes[comparing]

                                for name_compare in range(len(way)):
                                    correct_way = way[name_compare]
                                    name_for_compare += correct_way.name

                                if name_for_compare == possible_name:
                                    count_adding = 1
                                    break

                            if count_adding == 0:
                                routes.append(route_list_)

                        else:
                            routes.append(route_list_)

                        jeneral_result = cheking


            if len(list_for_input_starting) == 0:
                log_graph("Подальших продовжень немає")
                break


            interesting_ways.clear()
            previous_cities.clear()
            starting_cities.clear()

            for element in range(len(list_for_input_starting)):

                interesting_ways.append(list_for_input_ways[element])
                previous_cities.append(list_for_input_previous[element])
                starting_cities.append(list_for_input_starting[element])

            list_for_input_ways.clear()
            list_for_input_previous.clear()
            list_for_input_starting.clear()




    # Обчислюємо довжину кожного знайденого маршруту
    route_distances = []
    for route in routes:
        total_distance = 0
        for road in route:
            total_distance += road.lenght
        route_distances.append(total_distance)

    log_graph("\n========== ДОВЖИНИ МАРШРУТІВ ==========")
    for number in range(len(route_distances)):
        log_graph("Маршрут №", number + 1, "| Довжина:", route_distances[number])

    if len(routes) == 0:
        log_graph("\nМаршрутів від початкового до кінцевого міста не знайдено.")
        return None

    #Знаходимо індекс найкоротшого маршруту
    shortest_distance = route_distances[0]
    shortest_index = 0
    for number in range(1, len(route_distances)):
        if route_distances[number] < shortest_distance:
            shortest_distance = route_distances[number]
            shortest_index = number

    log_graph("\n========== НАЙКОРОТШИЙ МАРШРУТ ==========")
    log_graph("Номер маршруту:", shortest_index + 1)
    log_graph("Довжина маршруту:", shortest_distance)

    shortest_route = routes[shortest_index]
    return shortest_route, shortest_distance


# Запускаємо пошук найкоротшого маршруту
answer = 0
def find_distance(last_city):
    result = get_distance(correct_ways, list_cities, list_to_get_roads , last_city)
    if result is not None:
        shortest_route, shortest_distance = result
        log_graph("\nДороги найкоротшого маршруту:")
        for road in shortest_route:
            log_graph(road.name, "|", road.id1, "->", road.id2, "| Довжина:", road.lenght)
            answer = road.lenght

       
