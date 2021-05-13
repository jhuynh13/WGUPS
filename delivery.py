import csvreader
import datetime

# Complexity is O(n^3)
# This function runs the route simulation by manually loading the truck then
# running the dynamic nearest neighbor algorithm on each truck
def start():

    # Retrieve data from csv files on packages and address distances
    addresses = csvreader.getAddresses()
    distances = csvreader.getDistances()
    packages = csvreader.getPackages()

    # Manually load trucks with packages
    truck1 = [packages.get_package(0),packages.get_package(12),packages.get_package(13),packages.get_package(14),
    packages.get_package(15),packages.get_package(18),packages.get_package(19),packages.get_package(28),
    packages.get_package(29),packages.get_package(30),packages.get_package(33),packages.get_package(36),
    packages.get_package(39),packages.get_package(1),packages.get_package(3),packages.get_package(4)]

    truck2 = [packages.get_package(2),packages.get_package(5),packages.get_package(17),packages.get_package(24),
    packages.get_package(27),packages.get_package(31),packages.get_package(35),packages.get_package(37),
    packages.get_package(6),packages.get_package(7),packages.get_package(9),packages.get_package(10),
    packages.get_package(11),packages.get_package(16)]

    truck3 = [packages.get_package(8),packages.get_package(20),packages.get_package(21),packages.get_package(22),
    packages.get_package(23),packages.get_package(25),packages.get_package(26), packages.get_package(32),
    packages.get_package(34),packages.get_package(38)]

    distance_total = 0
    trucks = [truck1,truck2,truck3]

    #Truck 1 start at hub at 8 AM
    curr = '4001 South 700 East'
    total_time = datetime.datetime(2021, 4, 24, 8, 0, 0)
    #Truck 2 leaves at 9:05 AM
    total_time2 = datetime.datetime(2021, 4, 24, 9, 5, 0)

    # Complexity is O(n^3)
    for i in range(0,3):

        #Truck 1 leaves at 08:00:00
        if i == 0:
            # Keep finding routes until truck is empty
            while len(trucks[i]) != 0:

                # Retrieve route data
                result = csvreader.getRoute(curr,trucks[i],total_time)

                # Remove package from truck
                for x in trucks[i]:
                    if int(x.id) == int(result[1]):
                        trucks[i].remove(x)

                curr = result[2]
                
                # Accumulate distance and time
                distance_total = distance_total + result[0]
                total_time = total_time + result[3]

            #Back to hub after a truck is empty
            result = csvreader.getDistance(curr,'4001 South 700 East',total_time)
            curr = '4001 South 700 East'
            distance_total = distance_total + result[0]
            total_time = result[1]
        
        #Truck 2 leaves at 09:05:00
        else:
            # Keep finding routes until truck is empty
            while len(trucks[i]) != 0:

                # Retrieve route data
                result = csvreader.getRoute(curr,trucks[i],total_time2)

                # Remove package from truck
                for x in trucks[i]:
                    if int(x.id) == int(result[1]):
                        trucks[i].remove(x)

                curr = result[2]
                
                # Accumulate distance and time
                distance_total = distance_total + result[0]
                total_time2 = total_time2 + result[3]

            #Back to hub after a truck is empty
            result = csvreader.getDistance(curr,'4001 South 700 East',total_time2)
            curr = '4001 South 700 East'
            distance_total = distance_total + result[0]
   

    print('\nWelcome to WGUPS!\n')
    print('Deliveries were completed in', round(distance_total,4) ,'miles\n')



   

       

        


    

