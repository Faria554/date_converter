def us_to_standard_date(date_str):
    # Check if the date string is in the MM/dd/yyyy format
    if '/' in date_str:
        # Split the date string into month, day, and year components
        date_parts = date_str.split('/')
        if len(date_parts) != 3:
            raise ValueError("Invalid date format: must be MM/dd/yyyy")
            
        month, day, year = date_parts
    else:
        # Split the date string into month, day, and year components
        date_parts = date_str.split(' ')
        if len(date_parts) != 3 or date_parts[1][-1] != ',':
            raise ValueError("Invalid date format: must be MMM DD, yyyy")
            
        month = date_parts[0]
        day = date_parts[1][:-1]
        year = date_parts[2]
        
        # Convert the day component to a zero-padded string if necessary
        day = day.zfill(2)

    # Reorder the components into the standard format (day/month/year)
    standard_date = f"{day}/{month}/{year}"
    
    return standard_date

date_str = input("Enter a date (MM/dd/yyyy or MMM DD, yyyy): ")
try:
    standard_date = us_to_standard_date(date_str)
    print(f"Standard date: {standard_date}")
except ValueError as e:
    print(f"Error: {e}")