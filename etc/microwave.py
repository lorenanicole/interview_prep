from datetime import timedelta

class Microwave:
    def __init__(self):
        # self.timer = 0
        self.start_pushed = False
        self.time_entered = ""
    
    def receive_input(self):
        while not self.start_pushed:
            user_input = input()
            if user_input.isnumeric():
                if len(user_input) > 1:
                    user_input = ""
                    continue
                self.time_entered += user_input
                self.display_time()
            elif user_input.lower() == 'start':
                self.start_pushed = True
            elif len(self.time_entered) > 4:
                self.display_error()
                self.reset_time()
    
        if not self.validate_time():
            self.display_err()
        else:
            self.execute_timer()
        
        self.start_pushed = False
        self.time_entered = ""
    
    def display_time(self):
        if len(self.time_entered) == 4:
            print(f"{self.time_entered[0]}{self.time_entered[1]}:{self.time_entered[2]}{self.time_entered[3]}")
        elif len(self.time_entered) == 3:
            print(f"0{self.time_entered[0]}:{self.time_entered[1]}{self.time_entered[2]}")
        elif len(self.time_entered) == 2:
            print(f"00:{self.time_entered}")
        elif len(self.time_entered) == 1:
            print(f"00:0{self.time_entered[0]}")
        elif len(self.time_entered) == 0:
            print(f"00:00")
        else:
            print(f'ERRR')
            self.reset_time()
    
    def display_err(self):
        print(f'ERRR')
    
    def reset_time(self):
        self.time_entered = ""
    
    def validate_time(self):
        if len(self.time_entered) == 4:
            m = int(self.time_entered[0:2])
            s = int(self.time_entered[2:])
        elif len(self.time_entered) == 3:
            m = int(self.time_entered[0])
            s = int(self.time_entered[1:])
        elif len(self.time_entered) > 0 and len(self.time_entered) < 3:
            m = 0
            s = self.time_entered  

        if int(m) > 59 or int(s) > 59:
            return False
    
        return True

    def execute_timer(self):
        num_seconds = self.convert_to_seconds()

        while num_seconds > -1:
            minutes, seconds = divmod(num_seconds, 60)
            if minutes < 10:
                minutes = f'0{minutes}'
            if seconds < 10:
                seconds = f'0{seconds}'
            print(f'{minutes}:{seconds}')
            num_seconds -= 1
    
    def convert_to_seconds(self):
        if len(self.time_entered) == 4:
            m = int(self.time_entered[0:2])
            s = int(self.time_entered[2:])
        elif len(self.time_entered) == 3:
            m = int(self.time_entered[0])
            s = int(self.time_entered[1:])
        elif len(self.time_entered) > 0 and len(self.time_entered) < 3:
            m = 0
            s = self.time_entered

        num_seconds = int(timedelta(minutes=int(m), seconds=int(s)).total_seconds())
        
        return num_seconds

        




microwave = Microwave()
while True:
    microwave.receive_input()