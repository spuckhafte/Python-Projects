class CarGame:
    print("----------------------------------------------------------------------------------------------------------")
    print('\nThis is a car!')
    instructions = ('''Instructions:
start - car starts.
stop  - car stops.
quit  - exit car.
help  - get these instructions again.
fast  - increase speed.
boost - increase speed fast.
slow  - decrease speed.
break - decrease speed to 0 kmph.
check - checks the state of car.
''')
    print(f'\n{instructions}')
    print("Car is stopped !")
    response = ""
    started = False
    speed = 0
    while True:
        response = input('\n-> ').lower()
        if response == 'start':
            if started:
                print('Car is already started..!')
                print(f'Speed: {speed} kmph')
            else:
                started = True
                print('Car is starting........started!')
                print(f'Speed: 0 kmph')

        elif response == 'fast':
            if started:
                if speed < 200:
                    speed = speed + 5
                    print(f'Speed: ({speed} kmph)')
                else:
                    print("Can't exceed 200 kmph..!")

            else:
                print("Car is stopped..first start it !")

        elif response == 'boost':
            if started:
                if speed < 200:
                    speed += 10
                    if speed >= 200:
                        print("Can't exceed 200 kmph..!")
                        speed = speed - 10
                    else:
                        print(f'Speed: ({speed} kmph)')
                else:
                    print("Can't exceed 200 kmph..!")

        elif response == 'stop':
            if not started:
                print(f'Car is already is stopped !')
            elif speed != 0:
                print("First reduce speed of the car to 0 kmph !")
            else:
                started = False
                print(f'Car is stopping..........stopped !')

        elif response == 'slow':
            if started:
                if speed > 0 and speed != 0:
                    speed = speed - 5
                    print(f'Speed: ({speed} kmph)')
                else:
                    print("Can't decrease below 0 kmph ")
            else:
                print("Car is stopped !")

        elif response == "break":
            if started:
                if speed > 0 and speed != 0:
                    speed = speed - speed
                    print(f'Speed: {speed} kmph')
                else:
                    print("Speed already 0 kmph !")
            else:
                print("Car is stopped !")

        elif response == 'check':
            if started:
                print(f'Speed: {speed} kmph !')
                print("Status: Car is Started !")
            else:
                print('Status: Car is not started !')

        elif response == 'quit':
            if started:
                print("Car is started.....not safe to exit now......first stop the car !")
            else:
                print('You have exit the car !')
                break
        elif response == "help":
            print(instructions)
        else:
            print("Not the right command...try again!!!")
# End
