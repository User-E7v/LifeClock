import datetime
import os
import random
from dateutil.relativedelta import relativedelta

def get_birth_date():
    while True:
        try:
            year = int(input("Enter birth year (YYYY): "))
            month = int(input("Enter birth month (1-12): "))
            day = int(input("Enter birth day (1-31): "))
            birth_date = datetime.date(year, month, day)
            if birth_date <= datetime.date.today():
                return birth_date
            print("Birth date cannot be in the future. Try again.")
        except ValueError:
            print("Invalid date. Please enter valid numbers.")

def calculate_age_details(birth_date):
    today = datetime.date.today()
    delta = relativedelta(today, birth_date)
    
    total_days = (today - birth_date).days
    total_weeks = total_days // 7
    total_months = delta.years * 12 + delta.months
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    total_seconds = total_minutes * 60
    
    next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)
    days_until_birthday = (next_birthday - today).days
    
    return {
        'years': delta.years,
        'months': delta.months,
        'days': delta.days,
        'total_days': total_days,
        'total_weeks': total_weeks,
        'total_months': total_months,
        'total_hours': total_hours,
        'total_minutes': total_minutes,
        'total_seconds': total_seconds,
        'days_until_birthday': days_until_birthday,
        'next_birthday': next_birthday
    }

def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

def get_chinese_zodiac(year):
    zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", 
               "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return zodiacs[(year - 4) % 12]

def get_weekday_name(date):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]
    return weekdays[date.weekday()]

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

def get_life_stage(age):
    if age < 2:
        return "Infant"
    elif age < 4:
        return "Toddler"
    elif age < 6:
        return "Preschooler"
    elif age < 12:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 40:
        return "Young Adult"
    elif age < 60:
        return "Middle Age"
    elif age < 80:
        return "Senior"
    else:
        return "Elder"

def get_health_tips(age):
    if age < 18:
        return "Focus on balanced nutrition and regular exercise for growth"
    elif age < 40:
        return "Maintain work-life balance and build healthy habits"
    elif age < 60:
        return "Monitor health regularly and reduce stress"
    else:
        return "Stay active, maintain social connections, and regular check-ups"

def get_fun_fact(total_days):
    facts = [
        f"You have slept approximately {int(total_days * 8 / 24)} days in your life",
        f"Your heart has beaten about {int(total_days * 24 * 60 * 70):,} times",
        f"You have spent about {int(total_days / 365.25 * 2):,} days eating",
        f"The average person blinks about {int(total_days * 24 * 60 * 20):,} times",
        f"You have taken approximately {int(total_days * 24 * 60 * 20):,} breaths"
    ]
    return random.choice(facts)

def generate_wisdom():
    wisdoms = [
        "Life is not measured by the number of breaths we take, but by moments that take our breath away",
        "The purpose of life is to live it, taste it, experience it",
        "Every day is a new beginning, take a deep breath and start again",
        "The greatest gift of life is friendship, and I have received it",
        "Life is like riding a bicycle, to keep balance you must keep moving"
    ]
    return random.choice(wisdoms)

def print_separator(char="=", length=50):
    print(char * length)

def display_ascii_art(age):
    if age < 10:
        art = """
        ╔══════════════════════════╗
        ║ * Y O U N G   S T A R *  ║
        ╚══════════════════════════╝
        """
    elif age < 20:
        art = """
        ╔══════════════════════════╗
        ║ * G O L D E N   A G E *  ║
        ╚══════════════════════════╝
        """
    elif age < 40:
        art = """
        ╔══════════════════════════╗
        ║ * P R I M E   T I M E *  ║
        ╚══════════════════════════╝
        """
    elif age < 60:
        art = """
        ╔══════════════════════════╗
        ║ * S A G E   A G E     *  ║
        ╚══════════════════════════╝
        """
    else:
        art = """
        ╔══════════════════════════╗
        ║ * L E G E N D A R Y   *  ║
        ╚══════════════════════════╝
        """
    print(art)

def print_header():
    print_separator("=", 60)
    print("  A G E   I N   D A Y S   C A L C U L A T O R  ")
    print_separator("=", 60)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_header()
    print("\nEnter your birth date to calculate your exact age in days.\n")
    
    birth_date = get_birth_date()
    details = calculate_age_details(birth_date)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_header()
    
    display_ascii_art(details['years'])
    
    zodiac_sign = get_zodiac_sign(birth_date.month, birth_date.day)
    chinese_zodiac = get_chinese_zodiac(birth_date.year)
    birth_season = get_season(birth_date.month)
    life_stage = get_life_stage(details['years'])
    weekday_born = get_weekday_name(birth_date)
    fun_fact = get_fun_fact(details['total_days'])
    health_tip = get_health_tips(details['years'])
    wisdom = generate_wisdom()
    
    print(f"\n  BIRTH DATE        : {birth_date.strftime('%B %d, %Y')}")
    print(f"  TODAY             : {datetime.date.today().strftime('%B %d, %Y')}")
    print(f"  DAY OF WEEK BORN  : {weekday_born}")
    print_separator("-", 60)
    
    print(f"\n  EXACT AGE         : {details['years']} years, {details['months']} months, {details['days']} days")
    print(f"  TOTAL DAYS        : {details['total_days']:,} days")
    print(f"  TOTAL WEEKS       : {details['total_weeks']:,} weeks")
    print(f"  TOTAL MONTHS      : {details['total_months']:,} months")
    print(f"  TOTAL HOURS       : {details['total_hours']:,} hours")
    print(f"  TOTAL MINUTES     : {details['total_minutes']:,} minutes")
    print(f"  TOTAL SECONDS     : {details['total_seconds']:,} seconds")
    print_separator("-", 60)
    
    print(f"\n  NEXT BIRTHDAY     : {details['next_birthday'].strftime('%B %d, %Y')}")
    print(f"  DAYS UNTIL BDAY   : {details['days_until_birthday']} days")
    print_separator("-", 60)
    
    print(f"\n  ZODIAC SIGN       : {zodiac_sign}")
    print(f"  CHINESE ZODIAC    : {chinese_zodiac}")
    print(f"  SEASON OF BIRTH   : {birth_season}")
    print(f"  LIFE STAGE        : {life_stage}")
    print_separator("-", 60)
    
    print(f"\n  FUN FACT          : {fun_fact}")
    print_separator("-", 60)
    
    print(f"\n  HEALTH TIP        : {health_tip}")
    print_separator("-", 60)
    
    print(f"\n  WISDOM            : {wisdom}")
    print_separator("-", 60)
    
    if details['days_until_birthday'] == 0:
        print("\n   HAPPY BIRTHDAY! Today is your special day! ")
    elif details['days_until_birthday'] <= 7:
        print(f"\n   Your birthday is in {details['days_until_birthday']} days! Start celebrating!")
    
    print("\n  " + "=" * 56)
    print("  Thank you for using Age in Days Calculator!")
    print("  " + "=" * 56 + "\n")
    
    save_data = input("Save results to file? (y/n): ").lower()
    if save_data == 'y':
        filename = f"age_report_{birth_date.strftime('%Y%m%d')}.txt"
        try:
            with open(filename, 'w') as f:
                f.write("AGE IN DAYS CALCULATOR - DETAILED REPORT\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"BIRTH DATE: {birth_date.strftime('%B %d, %Y')}\n")
                f.write(f"WEEKDAY BORN: {weekday_born}\n\n")
                for key, value in details.items():
                    if key not in ['next_birthday']:
                        f.write(f"{key.replace('_', ' ').upper()}: {value}\n")
                f.write(f"NEXT BIRTHDAY: {details['next_birthday'].strftime('%B %d, %Y')}\n")
                f.write(f"\nZODIAC: {zodiac_sign}\n")
                f.write(f"CHINESE ZODIAC: {chinese_zodiac}\n")
                f.write(f"SEASON OF BIRTH: {birth_season}\n")
                f.write(f"LIFE STAGE: {life_stage}\n\n")
                f.write(f"FUN FACT: {fun_fact}\n")
                f.write(f"HEALTH TIP: {health_tip}\n")
                f.write(f"WISDOM: {wisdom}\n")
            print(f"\nReport saved as '{filename}'")
        except IOError:
            print("\nError: Could not save the report file.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again with valid inputs.")