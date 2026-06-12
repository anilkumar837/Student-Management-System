# movie ticket booking project

user_name = "ANIL KUMAR"
password = "12345"

# MOVIES DETAILS STORAGE

movies = []
shows = []
seats = []
bookings = []

while True:

    print('\n<<<<<<<<<< WELL COME TO MOVIE TICKET BOOKING >>>>>>>>>>')
    print("\n1. ADMIN")
    print("2. USER")
    print("3. EXIT")

    role = input("ENTER YOUR OPTION(1/2/3): ")

    # ---------------- ADMIN SECTION ----------------

    if role == "1":

        while True:
            name = input('\nENTER USERNAME NAME: ')
            pwd = input('ENTER PASSWORD: ')

            if user_name == name and password == pwd:
                print('\n<<<LOGIN SUCCESSFUL>>>')
                break
            else:
                print('\nxxx--INVALID DETAILS TRY AGAIN--xxx')

        while True:

            print("\n----- ADMIN SECTION -----")
            print("1. ADD MOVIE")
            print("2. ADD SHOW")
            print("3. MANAGE SEATS")
            print("4. DELETE MOVIE")
            print("5. VIEW ALL BOOKINGS")
            print("6. EXIT")

            choice = input("ENTER YOUR OPTION(1/2/3/4/5/6): ")

   # Add Movie
            if choice == "1":

                movie = input("ENTER MOVIE NAME: ")
                movies.append(movie)

                print("\n---MOVIE ADDED SUCCESSFULLY---")

    # Add Show
            elif choice == "2":

                if len(movies) == 0:
                    print("xx--N0 MOVIES AVAILABLE--xx")
                else:

                    print("\n LIST OF MOVIES ARE:")
                    for i in range(len(movies)):
                        print(i + 1, ".", movies[i])

                    movie_no = int(input("ENTER MOVIE NUMBER: "))
                    show_time = input("ENTER SHOW TIME: ")

                    shows.append([movies[movie_no - 1], show_time])

                    print("SHOW IS ADDED SUCCESSFULLY")

    # Manage Seats
            elif choice == "3":

                total_seats = int(input("ENTER NUMBER OF SEATS: "))

                seats.clear()

                for i in range(total_seats):
                    seats.append("AVAILABLE")

                print("\n<<SEATS CREATED SUCCESSFULLY>>")

            # Delete Movie
            elif choice == "4":

                if len(movies) == 0:
                    print("X-----NO MOVIES AVAILABLE CURRENTLY-----X")
                else:

                    print("\n THE MOVIES ARE:")
                    for i in range(len(movies)):
                        print(i + 1, ".", movies[i])

                    delete_no = int(input("ENTER MOVIE NUMBER TO DELETE: "))

                    movies.pop(delete_no - 1)

                    print("\n-----MOVIE HAS DELETED-----")

            # View Bookings
            elif choice == "5":

                if len(bookings) == 0:
                    print("\nNO BOOKINGS AVAILABLE YET")
                else:

                    print("\n BOOKING DETAILS ARE:")

                    for i in range(len(bookings)):
                        print(bookings[i])

            # Exit Admin
            elif choice == "6":
                break

            else:
                print("INVALID OPTION TRY AGAIN!!")

    # ---------------- USER SECTION ----------------

    elif role == "2":

        while True:

            print("\n----- USER MENU -----")
            print("1. VIEW MOVIES")
            print("2. VIEW SHOW TIME")
            print("3. SELECT SEATS")
            print("4. BOOK TICKET")
            print("5. VIEW BOOKING")
            print("6. EXIT")

            choice = input("ENTER YOUR CHOISE: ")

     # View Movies
            if choice == "1":

                if len(movies) == 0:
                    print("\nX---NO MOVIES ARE AVAILABLE---X")
                else:

                    print("\nAVAILABLE MOVIES ARE:")

                    for i in range(len(movies)):
                        print(i + 1, ".", movies[i])

     # View Show Times
            elif choice == "2":

                if len(shows) == 0:
                    print("\nNO SHOWS ARE AVAILABLE NOW")
                else:

                    print("\nSHOW TIMINGS ARE:")

                    for i in range(len(shows)):
                        print(i + 1, ".", shows[i][0], "-", shows[i][1])

            # Select Seats
            elif choice == "3":

                if len(seats) == 0:
                    print("SEATS ARE NOT CREATED BY ADMIN ")
                else:

                    print("\nSEATS STATUS")

                    for i in range(len(seats)):
                        print("Seats", i + 1, ":", seats[i])

            # Book Ticket
            elif choice == "4":

                if len(shows) == 0:
                    print("NO SHOWS ARE AVAILABLE")

                elif len(seats) == 0:
                    print("SEATS ARE NOT AVAILABLE")

                else:

                    name = input("ENTER YOUR NAME: ")

                    print("\nSHOWS ARE:")

                    for i in range(len(shows)):
                        print(i + 1, ".", shows[i][0], "-", shows[i][1])

                    show_no = int(input("Select Show Number: "))

                    print("\nSeat Status")

                    for i in range(len(seats)):
                        print("Seat", i + 1, ":", seats[i])

                    seat_no = int(input("Select Seat Number: "))

                    if seats[seat_no - 1] == "Available":

                        seats[seat_no - 1] = "Booked"

                        booking = [
                            name,
                            shows[show_no - 1][0],
                            shows[show_no - 1][1],
                            "Seat " + str(seat_no)
                        ]

                        bookings.append(booking)

                        print("\n<<<<<Ticket Booked Successfully>>>>>")

                    else:
                        print("\nx---Seat Already Booked---x")

            # View Booking
            elif choice == "5":

                if len(bookings) == 0:
                    print("\n x-----No Booking Found-----x")

                else:

                    name = input("ENTER CUSTOMER NAME: ")

                    found = 0

                    for i in range(len(bookings)):

                        if bookings[i][0] == name:

                            print("\nCustomer :", bookings[i][0])
                            print("Movie    :", bookings[i][1])
                            print("Show     :", bookings[i][2])
                            print("Seat     :", bookings[i][3])

                            found = 1

                    if found == 0:
                        print("/n----BOOKINGS NOT FOUND----")

            # Back
            elif choice == "6":
                break

            else:
                print("Invalid Choice")

    # ---------------- EXIT ----------------

    elif role == "3":

        print("THANK YOU VISIT AGAIN")
        break

    else:
        print("Invalid Role")
