seats=350
total_bookings=0
rejected_bookings=0
sold_tickets=0
while seats>0:
    ##Taking only valid ticket number
    tickets_num=int(input("Enter number of tickets (1-15, or 0 to exit): "))
    if tickets_num==0:
        break
    ##Checking for seats
    if tickets_num < 1 or tickets_num > 15:
        print("BOOKING REJECTED - You can only book between 1 and 15 tickets.\n")
        rejected_bookings += 1
        continue
    if tickets_num > seats:
        print(f"BOOKING REJECTED - Not enough seats. Only {seats} remaining.\n")
        rejected_bookings += 1
        continue
    valid_ages=True
    for i in range(tickets_num):
        age=int(input("ages: "))
        ##Checking Age restrictions
        if age < 12:
            valid_ages = False
            break
    ##Finalized Booking seats
    if valid_ages:
        print(f"BOOKING CONFIRMED - {tickets_num} tickets\n")
        seats -= tickets_num
        sold_tickets+= tickets_num
        total_bookings += 1
    else:
        print("BOOKING REJECTED - Age restriction\n")
        rejected_bookings += 1
##Printing Output:Final Report
print("FINAL REPORT")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {sold_tickets}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {seats}")