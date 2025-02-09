'''Install and use the datetime module to print the current date and time in the format:
YYYY-MM-DD HH:MM:SS

🔹 Hint: Use datetime.datetime.now().strftime() for formatting.'''

from datetime import datetime  

# Get current date and time
current_time = datetime.now()

# Format it as YYYY-MM-DD HH:MM:SS
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print("Current Date and Time:", formatted_time)


#Explanation
'''1️⃣ datetime.now() fetches the current date and time.
   2️⃣ .strftime("%Y-%m-%d %H:%M:%S") formats it in the required YYYY-MM-DD HH:MM:SS format.
   3️⃣ print() displays the formatted date and time.'''''



'''strftime fucntion-date fromat 


%Y	Full year (4 digits)	2025
%y	Short year (last 2 digits)	25
%m	Month (01-12)	02
%d	Day of the month (01-31)	09
%H	Hour (24-hour format)	14
%I	Hour (12-hour format)	02
%p	AM/PM	PM
%M	Minute (00-59)	30
%S	Second (00-59)	45
%A	Full weekday name	Sunday
%a	Short weekday name	Sun
%B	Full month name	February
%b	Short month name	Feb

'''