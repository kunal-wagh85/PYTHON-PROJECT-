"""Simple XYZ Travel bus ticket counter project."""

SEAT_CAPACITY = 40

ROUTES = {
    "R1": {
        "destination": "Mumbai",
        "departure": "06:00 PM",
        "adult_fare": 450,
        "child_fare": 225,
        "available_seats": SEAT_CAPACITY,
    },
    "R2": {
        "destination": "Nashik",
        "departure": "06:45 PM",
        "adult_fare": 500,
        "child_fare": 250,
        "available_seats": SEAT_CAPACITY,
    },
    "R3": {
        "destination": "Chhatrapati Sambhajinagar",
        "departure": "07:30 PM",
        "adult_fare": 650,
        "child_fare": 325,
        "available_seats": SEAT_CAPACITY,
    },
    "R4": {
        "destination": "Kolhapur",
        "departure": "08:15 PM",
        "adult_fare": 600,
        "child_fare": 300,
        "available_seats": SEAT_CAPACITY,
    },
    "R5": {
        "destination": "Solapur",
        "departure": "09:00 PM",
        "adult_fare": 450,
        "child_fare": 225,
        "available_seats": SEAT_CAPACITY,
    },
    "R6": {
        "destination": "Nagpur",
        "departure": "09:45 PM",
        "adult_fare": 1000,
        "child_fare": 500,
        "available_seats": SEAT_CAPACITY,
    },
}

CANCELLATION_NOTE = "Cancellation is allowed up to 24 hours before departure. Contact XYZ Travel to cancel."


def show_routes(routes):
    print("\nXYZ TRAVEL - PUNE DEPARTURES")
    print("These are sample routes and sample fares.")
    print("-" * 55)

    for route_code in routes:
        route = routes[route_code]
        print(route_code, "| Pune to", route["destination"])
        print("Departure:", route["departure"])
        print("Adult fare: Rs.", route["adult_fare"], "| Child fare: Rs.", route["child_fare"])
        print("Seats available:", route["available_seats"])
        print("-" * 55)


def book_ticket(routes, bookings):
    show_routes(routes)

    route_code = input("Enter the route code: ").strip().upper()

    if route_code not in routes:
        print("That route code was not found.")
        return

    route = routes[route_code]

    passenger_name = input("Enter passenger name: ").strip()
    if passenger_name == "":
        print("Passenger name cannot be blank.")
        return

    adult_text = input("Number of adults: ").strip()
    child_text = input("Number of children: ").strip()

    if not adult_text.isdigit() or not child_text.isdigit():
        print("Please enter whole numbers for adults and children.")
        return

    adult_count = int(adult_text)
    child_count = int(child_text)
    passenger_count = adult_count + child_count

    if passenger_count == 0:
        print("Enter at least one passenger.")
        return

    if passenger_count > route["available_seats"]:
        print("There are not enough seats on this route.")
        return

    adult_total = adult_count * route["adult_fare"]
    child_total = child_count * route["child_fare"]
    total_fare = adult_total + child_total

    print("\nFare summary")
    print("Adult fare:", adult_count, "x Rs.", route["adult_fare"], "= Rs.", adult_total)
    print("Child fare:", child_count, "x Rs.", route["child_fare"], "= Rs.", child_total)
    print("Total fare: Rs.", total_fare)

    confirmation = input("Confirm booking? (y/n): ").strip().lower()
    if confirmation != "y":
        print("Booking was not made.")
        return

    booking_id = "XYZ-" + str(len(bookings) + 1)

    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "route_code": route_code,
        "adult_count": adult_count,
        "child_count": child_count,
        "passenger_count": passenger_count,
        "total_fare": total_fare,
    }

    bookings.append(booking)
    route["available_seats"] = route["available_seats"] - passenger_count

    print("\n" + "=" * 55)
    print("XYZ TRAVEL - BUS TICKET")
    print("=" * 55)
    print("Booking ID:", booking["booking_id"])
    print("Passenger:", booking["passenger_name"])
    print("Route:", booking["route_code"], "- Pune to", route["destination"])
    print("Departure:", route["departure"])
    print("Adults:", booking["adult_count"], "x Rs.", route["adult_fare"], "= Rs.", adult_total)
    print("Children:", booking["child_count"], "x Rs.", route["child_fare"], "= Rs.", child_total)
    print("Total passengers:", booking["passenger_count"])
    print("Total fare: Rs.", booking["total_fare"])
    print("-" * 55)
    print("Policy:", CANCELLATION_NOTE)
    print("Seats remaining:", route["available_seats"])
    print("=" * 55)


def main():
    bookings = []

    while True:
        print("\nXYZ Travel Bus Ticket Counter")
        print("1. View routes")
        print("2. Book a ticket")
        print("3. Exit")

        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            show_routes(ROUTES)
        elif choice == "2":
            book_ticket(ROUTES, bookings)
        elif choice == "3":
            print("Thank you for using XYZ Travel.")
            break
        else:
            print("Please choose 1, 2, or 3.")


main()
