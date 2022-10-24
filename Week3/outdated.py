months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    formatted_date = validate_date()
    print(formatted_date)
    
def validate_date():
    date = input("Date: ")
    
    while True:
        try:
            if (',') in date and ("/") not in date:
                date = date.split(', ')
                year = date[1]
                month_day = date[0].split(" ")
                day = month_day[1].zfill(2)
                month_index = months.index(month_day[0]) + 1
                
                if int(day) > 31:
                    date = input("Date: ")
                formatted = f"{year}-{month_index:02}-{day:02}"
                return formatted
            elif ('/') in date:
                if date.isalnum():
                    date = input("Date: ")
                
                if " " in x:
                    date = date.split()
                
                date = date.split('/')
                
                
                month = date[0].zfill(2)
                day = date[1].zfill(2)
                year = date[2]
                
                if int(day) > 31 or int(month) > 12:
                    date = input("Date: ")
                
                formatted = f"{year}-{month}-{day}"
                return formatted
            
        except ValueError:
            date = input("Date: ")
        else:
            continue
            
        
main()