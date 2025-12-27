from colorama import Fore

Country = ['Emirates', 'America', 'Germany', 'Canada']      #Country
Airline_List = ['Delta', 'American', 'Turkish', 'Indiana', 'Emirates', 'Lufthansa', 'Air France', 'Qantas', 'Singapore', 'British Airways']     #Airlines
Travel_information = {}

try:
    f = open("Airline_details.txt", 'r')      #Airline_details
    f.readline()
except FileNotFoundError:
    print(Fore.RED + "Error: 'Airline_details.txt' file not found.")
    exit()

airlines = {}
registered_names = set()
airlines_satisfaction = []
passenger_satisfaction = []


Airlines_Data = {                       #Airline Matrix
    'Delta': [[0, 0, 0, 1],
              [1, 0, 1, 1],             #The order of the rows is as follows:[Emirates - America - Germany - Canada]
              [0, 1, 0, 1],             #The order of the columns is as follows:1.Emirates, 2.America, 3.Germany, 4.Canada
              [1, 1, 0, 0]],
    'American': [[0, 1, 0, 0],
                 [1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [0, 0, 1, 0]],
    'Turkish': [[0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0]],
    'Indiana': [[0, 1, 0, 0],
                [1, 0, 1, 1],
                [0, 1, 0, 0],
                [0, 1, 0, 0]],
    'Emirates': [[0, 1, 1, 1],
                 [1, 0, 1, 0],
                 [1, 1, 0, 1],
                 [1, 0, 1, 0]],
    'Lufthansa': [[0, 1, 0, 1],
                  [1, 0, 0, 1],
                  [0, 0, 0, 0],
                  [1, 1, 0, 0]],
    'Air France': [[0, 1, 0, 0],
                   [1, 0, 0, 1],
                   [0, 0, 0, 1],
                   [0, 1, 1, 0]],
    'Qantas': [[0, 1, 0, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]],
    'Singapore': [[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0]],
    'British Airways': [[0, 1, 0, 0],
                        [1, 0, 1, 1],
                        [0, 1, 0, 1],
                        [0, 1, 1, 0]],
}



print(Fore.CYAN+'Hello!Welcome to the airport.')
print(Fore.CYAN+'We are here to help you have a perfect flight.')
print(Fore.CYAN+'Please follow the steps below carefully.',end='\n\n')



def passenger_name():                   #name-passenger
    while True:
        name = input(Fore.LIGHTBLUE_EX + '\nPlease write your full name and surname: ').strip()
        if name.lower() == 'exit':      #To exit the program when the user wants
            return None

        if len(name.split()) <= 1:        #To ensure that the user enters their full first and last name
            print(Fore.RED + 'Warning! Please enter your full name.')
            continue                        #A major drawback of the program is that if the user's name is two-part and does not enter a last name, the program cannot recognize it.

        if all(item.isalpha() for item in name.split()):
            capitalized_name = ' '.join(word.capitalize() for word in name.split())         #This will make the program output more beautiful and readable.
            if capitalized_name in registered_names:
                print(Fore.RED + f'Warning! The name {capitalized_name} is already registered. Please enter a different name.')
                continue            #If the user wants to register their name twice or more, the application will not allow it.
            else:
                return capitalized_name


def passenger_gender():                 #gender-passenger
    while True:
        gender = input(Fore.LIGHTBLUE_EX + 'Please enter your gender (Male/Female): ').capitalize()
        if gender.lower() == 'exit':            ##To exit the program when the user wants
            return None

        if gender in ['Male', 'Female']:        #There are only two types of gender in the world.
            return gender

        else:
            print(Fore.RED + 'Warning! Determine your gender correctly.')


def passenger_age():                #age_passenger
    while True:
        try:
            age = int(input(Fore.LIGHTBLUE_EX + 'Please enter your age in numbers: '))
            if str(age).lower() == 'exit':          #To exit the program when the user wants
                return None

            if age <= 0:            #If the user enters a zero or negative age, an error will occur.
                print(Fore.RED + 'Warning! Please enter your age correctly.')

            else:
                return age

        except ValueError:
            print(Fore.RED + 'Warning! The input is invalid.')


def passenger_marriage():           #marriage-passenger
    while True:
        marriage = input(Fore.LIGHTBLUE_EX + 'Enter your marital status (Single/Married): ').capitalize()
        if marriage.lower() == 'exit':              #To exit the program when the user wants
            return None

        if marriage in ['Single', 'Married']:
            return marriage

        else:
            print(Fore.RED + 'Warning! Determine your marriage correctly.')


def passenger_airline():                #airline-passenger
    while True:
        airline = input(Fore.LIGHTBLUE_EX + 'Please specify the airline you wish to travel with: ').strip().title()
        if airline.lower() == 'exit':           #To exit the program when the user wants
            return None

        if airline in Airline_List:
            return airline

        else:
             print(Fore.RED + 'The entered airline is currently not offering service. Please select another airline.')


def passenger_origin():             #origin-passenger
    while True:
        origin = input(Fore.LIGHTBLUE_EX + 'Identify your origin: ').capitalize()
        if origin.lower() == 'exit':            #To exit the program when the user wants
            return None

        if origin in Country:
            return origin

        else:
            print(Fore.RED + 'Warning! The requested origin is invalid.')


def passenger_destination():            #destination-passenger
    while True:
        destination = input(Fore.LIGHTBLUE_EX + 'Identify your destination: ').capitalize()
        if destination.lower() == 'exit':           #To exit the program when the user wants
            return None

        if destination in Country:
            return destination

        else:
            print(Fore.RED + 'Sorry! There are no flights to your selected destination.')


def check_fly(airline, origin, destination):            #Using a dictionary, all airline matrices can be read.
    index_country = {
        'Emirates': 0,
        'America': 1,
        'Germany': 2,
        'Canada': 3
    }

    if origin not in index_country:
        print(Fore.RED + 'Warning! The selected origin is invalid.')
        return False

    elif destination not in index_country:
        '''print(Fore.RED + 'Sorry! There are no flights to your selected destination.')'''
        return False

    origin_index = index_country[origin]
    destination_index = index_country[destination]

    fly = Airlines_Data[airline][origin_index][destination_index]

    if fly == 0:           #Zero means there are no flights from origin to destination on this airline.
        '''print(Fore.LIGHTWHITE_EX + '\nThere are no trips from this origin to the selected destination.')'''
        return False

    else:               #One means the flight from origin to destination is operational.
        print(Fore.LIGHTWHITE_EX + '\nRegistered. Have a nice trip :)')
        return True



def remove_airline():           #remove airline
    name_remove = input(Fore.LIGHTBLUE_EX + '\nPlease write your full name and surname: ').strip().title()
    airline_remove = input(Fore.LIGHTBLUE_EX + 'Enter your registered airline: ').strip().title()

    if airline_remove not in Travel_information:
        print(Fore.RED + f'\nThere are no registrations for the airline {airline_remove}.')         #If the entered airline does not exist in the Travel information
        return

    found_trip = False
    for info in Travel_information[airline_remove]:
        if info['Name'] == name_remove:
            Travel_information[airline_remove].remove(info)
            found_trip = True
            print(Fore.LIGHTMAGENTA_EX + f'\nTrip for {name_remove} has been successfully canceled.')
            break

    if not found_trip:          #If the entered passenger name is invalid
        print(Fore.RED + f'No trip found for passenger named {name_remove} in airline {airline_remove}.')



def search_airline():           #search-airline
    print(Fore.LIGHTBLUE_EX + '\nChoose which part of the flight you want to search:', end='\n\n')
    print(Fore.LIGHTBLUE_EX + '1. Search airlines')         #Search airlines
    print(Fore.LIGHTBLUE_EX + '2. Passenger search')        #Passenger search

    search = input(Fore.LIGHTBLUE_EX + '\nPlease select: ').capitalize()


    if search == '1':           #Search airlines
        airline_search = input(Fore.LIGHTBLUE_EX + 'Enter the airline name: ').strip().title()
        if airline_search not in Travel_information:
            print(Fore.RED + f'There are no registrations for the airline {airline_search}.')
        else:
            print(Fore.LIGHTMAGENTA_EX + f'\nAirline: {airline_search}, Number of passengers: {len(Travel_information[airline_search])}')
            for info in Travel_information[airline_search]:
                print(Fore.LIGHTMAGENTA_EX + f'Passenger Info: {info}')

    elif search == '2':             #Passenger-search
        airline_passenger = input(Fore.LIGHTBLUE_EX + "Please enter the passenger's name: ").strip().title()
        found = False           #
        for airline, passengers in Travel_information.items():
            for info in passengers:
                if info['Name'].lower() == airline_passenger.lower():
                    print(Fore.LIGHTMAGENTA_EX+ f'Passenger Info for {airline_passenger} in Airline {airline}: {info}')
                    found = True
                    break
            if found:
                break

        if not found:
            print(Fore.RED + f'No records found for passenger named {airline_passenger}.')

    else:
        print(Fore.RED + 'The input is invalid. Please try again.')



def sorting_airlines():         #sorting-airlines
    print(Fore.LIGHTBLUE_EX + '\nWhich option would you like to sort by: ',end='\n\n')
    print(Fore.LIGHTBLUE_EX + '1. Sorting airlines (based on passenger satisfaction)')          #Sorting airlines
    print(Fore.LIGHTBLUE_EX + '2. Sorting passengers')              #Sorting passengers

    choice = input(Fore.MAGENTA + '\nPlease select: ')
    if choice.isalpha():
        print(Fore.RED + 'The input is invalid. Please enter it as a number.')

    elif choice == '1':         #Sorting airlines
        f.readline()                #Airline details

        for line in f.readlines():
            line = line.replace('\n', '')
            line_split = line.split(',')
            airlines[line_split[0]] = line_split[1:]

        for airline, info in airlines.items():
            a = str(airlines[airline][2]) + ' : ' + str(airline)
            airlines_satisfaction.append(a)

        print(Fore.LIGHTMAGENTA_EX + 'The order of airlines according to passenger satisfaction is as follows:', end='\n')
        print(sorted(airlines_satisfaction))


    elif choice == '2':             #Sorting-passengers
        airline = input(Fore.LIGHTBLUE_EX+'\nEnter the name of the desired airline: ').capitalize()
        if airline in Travel_information:

            names = [passenger['Name'] for passenger in Travel_information[airline]]
            names_sorted = sorted(names)

            print(Fore.LIGHTMAGENTA_EX + f'\nPassenger names for airline "{airline}":')
            for name in names_sorted:
                print(Fore.LIGHTMAGENTA_EX + f' - {name}')

        else:
            print(Fore.RED + f'The airline "{airline}" does not exist in our records.')

    else:
        print(Fore.RED + 'The option is invalid. Please try again.')

while True:
    print(Fore.LIGHTWHITE_EX + '\nI would be happy to know what I can do for you?', end='\n\n')
    print(Fore.LIGHTWHITE_EX + '1. Add passenger')          #Add passenger
    print(Fore.LIGHTWHITE_EX + '2. Remove passenger')       #Remove passenger
    print(Fore.LIGHTWHITE_EX + '3. Search')                 #Search
    print(Fore.LIGHTWHITE_EX + '4. Sort')                   #Sort
    print(Fore.LIGHTWHITE_EX + '5. Exit', end='\n\n')       #Exit

    option = input(Fore.LIGHTWHITE_EX + 'Please select the desired option: ')

    if option == '5':               #Exit
        print(Fore.CYAN + 'Have a good fly. Goodbye!')
        break

    elif option == '1':             #Add passenger
        while True:
            print(Fore.LIGHTCYAN_EX+'\nIf you want to exit the "Add passenger" section, you can enter "exit" in any part of the program and return to the menu.')
            Name = passenger_name()         #name-passenger
            if Name is None:
                break

            Gender = passenger_gender()         #gender-passenger
            if Gender is None:
                continue

            Age = passenger_age()               #age_passenger
            if Age is None:
                continue

            Marriage = passenger_marriage()     #marriage-passenger
            if Marriage is None:
                continue

            Airline = passenger_airline()          #airline-passenger
            if Airline is None:
                continue

            Origin = passenger_origin()             #origin-passenger
            if Origin is None:
                continue

            Destination = passenger_destination()       ##destination-passenger
            if Destination is None:
                continue

            if Origin == Destination:
                print(Fore.RED + 'Warning! Origin and destination must be different. Try again later.')
                continue


            if check_fly(Airline, Origin, Destination):
                if Airline not in Travel_information:
                    Travel_information[Airline] = []

                Travel_information[Airline].append({
                    'Name': Name,
                    'Gender': Gender,
                    'Age': Age,
                    'Marriage': Marriage,
                    'Origin': Origin,
                    'Destination': Destination
                })

                registered_names.add(Name)

                print(Fore.LIGHTBLACK_EX + '\nAIRLINE DATA:')
                for airline_name, users in Travel_information.items():
                    for info in users:
                        print(Fore.LIGHTMAGENTA_EX + f'Airline: {airline_name}, info: {info}')
                break
            else:
                print(Fore.RED + '\nNo flights available from the selected origin to destination. Please enter your name again.')

    elif option == '2':         #Remove passenger
        remove_airline()

    elif option == '3':         #Search
        search_airline()

    elif option == '4':         #Sort
        sorting_airlines()

    else:
        print(Fore.RED + 'Invalid option. Please choose again.')

f.close()
