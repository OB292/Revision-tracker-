import re

#main menu
def menu(): 
    print("*****************")
    print("revision")
    print("*****************")
    print("If you would like to start a revision session, select option 1")
    print("If you would like to load revision statistics, select option 2")
    print("If you would like to exit then input 3")

#allows the selsection of different options listed in the main menu
    while True:
        choice = input("Please input your choice: ")
        if choice == "1":
            startrevision()
            break
        elif choice =="2":
            viewstats()
            break
        elif choice =="3":
          exit()
        else:
            print("Invalid input, please try again.")

#startrevision opening message
def startrevision():
  print ("**************")
  print("Time to revise!")
  print ("**************")

  while True: 

    import time

    class Stopwatch:
        def __init__(self):
            self.start_time = None
            self.end_time = None

#stopwatch menu
        def usage(self):
            print("\n----------- STOPWATCH -----------")
            print("|-> s      : start the stopwatch |")
            print("|-> Ctrl+C : stop the stopwatch  |")
            print("----------- STOPWATCH -----------")

        def start(self):
            self.start_time = time.time()

#starts the stopwatch with s 
        def start_countdown(self, seconds_countdown=3):
            user_input = input("\n-> Press 's' when you're ready to start: ")
            while seconds_countdown > 0:
                print(f"\rStarting in {seconds_countdown}...", end="")
                time.sleep(1)
                seconds_countdown -= 1
            print("\rGO !", end="")

#stops the stopwatch with ctrl s and writes the result in a text file, returns to main menu
        def stop(self):
            self.end_time = time.time()
            print(f"\n\nTotal elapsed time: {(self.end_time - self.start_time):.3f} seconds\n")
            file =open("stats.txt","a") 
            file.write(f"\n\nTotal elapsed time: {(self.end_time - self.start_time):.3f} seconds\n")
            file.close()
            menu()
            exit(0)
            
#shows time when stopwatch is running
        def run(self):
            self.usage()
            self.start_countdown()
            self.start()
            try:
                while True:
                    print(f"\rElapsed time: {(time.time() - self.start_time):.0f} seconds", end="")
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop()

    if __name__ == "__main__":
        stopwatch = Stopwatch()
        stopwatch.run()
        break

# menu for viewing saved revision stats
def viewstats():
    print("****************")
    print("View statistics?")
    print("****************")
    stats=input("Would you like to load previous revision statistics?")
    if stats == 'yes':

        # Read the file and extract numbers
        with open('stats.txt', 'r') as file:
            data = file.read()
            numbers = re.findall(r'\d+\.\d+', data)

        # Adds the extracted numbers
        total_seconds = sum(map(float, numbers))

        # Outputs total number of seconds spent revising
        print(f'You have spent {total_seconds} seconds revising!')
        menu()
    else:
        menu()

     
menu()
viewstats()