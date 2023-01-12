
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password



class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to_des):
        self.coach = coach
        self.driver =driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to_des = to_des
        self.seat = ["Empty" for i in range(20)]


class PhitronCompany:
    total_bus = 5
    total_bus_list = [] #dummy database
    def install(self):
        bus_no = int(input("Enter a bus number: "))
        flag = 1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                flag = 0
                print("Bus already installed")
                break
        if flag:
            bus_driver = input("enter bus driver name: ")
            bus_arrival = input("enter bus arrival time: ")
            bus_departure = input("enter departure time: ")
            bus_from = input("enter leaving place: ")
            bus_to = input("enter destination: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\n Bus installed successful")


class BusCounter(PhitronCompany):
    user_list = [] #user database
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter Bus Number: "))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger =  input("Enter your Name: ")
                seat_no = int(input("Enter your seat number: "))
                if seat_no> self.bus_seat:
                    print("Only 20 seats are available")
                elif bus['seat'][seat_no-1] != 'Empty':
                    print("Seat already booked")
                else:
                    bus['seat'][seat_no -1] = passenger
        
        for bus in self.total_bus_list:
            print(bus['seat'])

    def showBusInfo(self):
        bus_no = int(input("Enter bus no: "))
        for bus in self.total_bus_list:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus Number: {bus_no} \t\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t To: {bus['to_des']}")





company = PhitronCompany()
company.install()

bus = BusCounter()
bus.showBusInfo()
bus.reservation()
    

