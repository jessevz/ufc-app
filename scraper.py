import requests
from bs4 import BeautifulSoup
from database import *
import time
from datetime import datetime
from event import Event, Fight

def main():
    db = SimpleSQLiteDB()
    db.create_tables()

    url = "http://ufcstats.com/statistics/events/completed?page=all"

    response = requests.get(url)

# Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <i> tags with the specific class 'b-statistics__table-content'
        elements = soup.find_all('i', class_='b-statistics__table-content')

        for idx, element in enumerate(elements[1:]):
            info = element.text.strip().splitlines()
            date = info[-1].lstrip()
            event_name = info[0]

            date_object = datetime.strptime(date, "%B %d, %Y")
            unix_timestamp = int(time.mktime(date_object.timetuple()))

            detail_link = element.findChild("a").get("href")
            # print(f"date: {unix_timestamp} event: {event_name} detail link: {detail_link}")

            detail_response = requests.get(detail_link)
            if detail_response.status_code == 200: #this only works for completed fights, upcoming fights have to first search for the fighter column specifically
                detail_soup = BeautifulSoup(detail_response.content, 'html.parser')
                location_element = detail_soup.find_all('li', class_='b-list__box-list-item')[-1]
                location = location_element.text.splitlines()[-2].lstrip()
                event = Event(None, event_name, unix_timestamp, location)
                fighter_elements = detail_soup.find_all('a', class_='b-link b-link_style_black')
                for i in range(0, len(fighter_elements), 2):
                    fighter1 = fighter_elements[i].text.strip()
                    fighter2 = fighter_elements[i+1].text.strip()
                    fight = Fight(fighter1, fighter2, True)
                    event.add_fight(fight)
                    print(f"fighter1: {fighter1} fighter2: {fighter2}")
                db.add_event(event)
            else:
                print("Detail request went wrong!")

            if idx > 5:
                break

if __name__ == "__main__":
    main()
