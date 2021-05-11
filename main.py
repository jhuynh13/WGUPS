# Johnny Huynh
# Student ID: 001552351

import delivery
import csvreader
import datetime

# This is the main claass that will call functions from other classes and run
# the route simulation. It also displays the command line prompts for user.
class main:

    # Runs the route simulation
    delivery.start()

    # Retrieve updated data on packages
    hashtable = csvreader.getPackages()

    time_parse = []
    parser = ""
    parser2 = ""
    user_input = None

    # Command line prompts to ask users for specific data of packages
    print('What would you like to do?\n')
    print('Check a package status at a specified time (Press 1)\n')
    print('Check all package statuses at a specified time (Press 2)\n')
    print('Quit (Press 3)\n')
    choice = input('Enter your choice:\n')

    while choice != '3':
        if choice == '1':

            parser2 = input('Enter a valid package id ')
            parser = input('Enter the time in this format 00:00:00 (Hours:Minutes:Seconds)\n')
            time_parse = parser.split(':')

            # Parse user input into a datetime object for comparison with package datetime object
            user_input = datetime.datetime(2021, 4, 24, int(time_parse[0]), int(time_parse[1]),
                int(time_parse[2]))

            # Complexity is O(1)
            if hashtable.lookup(int(parser2)).timestamp > user_input:
                print('Package ID',parser2, 'is not delivered yet\n')
            else:
                print('Package ID',parser2, 'has been delivered\n')
            
        elif choice == '2':
            
            parser = input('Enter the time in this format 00:00:00 (Hours:Minutes:Seconds)\n')
            time_parse = parser.split(':')

            # Parse user input into a datetime object for comparison with package datetime object
            user_input = datetime.datetime(2021, 4, 24, int(time_parse[0]), int(time_parse[1]),
                int(time_parse[2]))

            # Complexity is O(n)
            for x in range (1,41):

                # Complexity is O(1)
                package_time = hashtable.lookup(x).timestamp

                print('Package ID',hashtable.lookup(x).id, 'Delivery status:')
                if(user_input < package_time):
                    print('Not Delivered Yet')
                    print('ETA is', package_time)
                else:
                    print('Delivered on', package_time)
                
                print('\n')
             
        else:
            print('Invalid input, please input 1,2, or 3')
        choice = input('Enter your choice: ')

    exit()

