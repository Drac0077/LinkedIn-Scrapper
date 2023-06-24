import sys
from bs4 import BeautifulSoup

def scrape_data(html_code):
    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        scraped_data = []
        
        # Extract name and title
        name = soup.find('h1').text.strip()
        title = soup.find('p').text.strip()
        scraped_data.append(f"Name: {name}")
        scraped_data.append(f"Title: {title}")
        
        # Extract about section
        about = soup.find('section', {'h2': 'About'}).find('p').text.strip()
        scraped_data.append(f"About: {about}")
        
        # Extract experience section
        experience_section = soup.find('section', {'h2': 'Experience'})
        experience_list = experience_section.find('ul').find_all('li')
        
        for experience in experience_list:
            company = experience.find('h3').text.strip()
            position = experience.find('p').text.strip()
            duration = experience.find_all('p')[1].text.strip()
            scraped_data.append(f"Company: {company}")
            scraped_data.append(f"Position: {position}")
            scraped_data.append(f"Duration: {duration}")
            scraped_data.append('-' * 20)
        
        return scraped_data
    
    except Exception as e:
        print(f"Failed to scrape data from HTML code. Error: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <html_code>")
        return
    
    html_code = sys.argv[1]
    scraped_data = scrape_data(html_code)
    
    if scraped_data:
        print("Scrapped data from HTML code:")
        for data in scraped_data:
            print(data)

if __name__ == '__main__':
    main()
