from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, asdict
from typing import List
import csv

@dataclass
class Vacancy:
    title: str
    company: str
    location: str

def fetch_html(url: str) -> BeautifulSoup:
    """Fetch HTML content from a given URL and return the BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests
    return BeautifulSoup(response.content, 'html.parser')

def extract_job_categories(soup: BeautifulSoup) -> List[str]:
    """Extract job category URLs from the main RocketJobs.pl page."""
    categories_div = soup.select_one('div.css-4k04cs div.css-1k0qr6v div.css-1jmm92x div.css-5hh74a div.css-138ir5g div.css-1sg36r4 div.css-14rp0mq div.css-bi6kiv div.css-8e6m8o')
    if categories_div:
        return [category['href'] for category in categories_div.select('li a')]
    return []

def extract_job_postings(soup: BeautifulSoup) -> List[Vacancy]:
    """Extract job postings from the BeautifulSoup object."""
    job_postings = []
    job_listings = soup.find_all('div', class_='css-1sg36r4')
    for job_listing in job_listings:
        title_element = job_listing.find('h3', class_='css-162lmgr')
        company_element = job_listing.find('span', class_='css-5yy118')
        location_element = job_listing.find('span', class_='css-5aysv1')
        if title_element and company_element and location_element:
            job_postings.append(Vacancy(
                title=title_element.text.strip(),
                company=company_element.text.strip(),
                location=location_element.text.strip()
            ))
    return job_postings

def get_pagination_links(soup: BeautifulSoup) -> List[str]:
    """Extract pagination links from the BeautifulSoup object."""
    pagination = soup.find("ul", class_="css-musp26")
    if pagination:
        return [link["href"] for link in pagination.find_all("a")]
    return []

def crawl_rocketjobs(url: str) -> List[Vacancy]:
    """Crawl RocketJobs.pl to extract job listings, handling pagination."""
    all_jobs = []
    try:
        soup = fetch_html(url)
        job_postings = extract_job_postings(soup)
        all_jobs.extend(job_postings)
        
        pagination_links = get_pagination_links(soup)
        for page_link in pagination_links[1:]:  # Skip the first link (current page)
            full_url = f"{url}{page_link}"
            soup = fetch_html(full_url)
            job_postings = extract_job_postings(soup)
            all_jobs.extend(job_postings)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while crawling the URL: {e}")

    return all_jobs

def save_to_csv(vacancies: List[Vacancy], filename: str):
    """Save a list of Vacancy instances to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'company', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for vacancy in vacancies:
            writer.writerow(asdict(vacancy))

# Example usage
starting_url = 'https://rocketjobs.pl/wszystkie-lokalizacje/marketing/ecommerce'
job_postings = crawl_rocketjobs(starting_url)

# Print or process the extracted job postings
for job in job_postings:
    print(f"Title: {job.title}")
    print(f"Company: {job.company}")
    print(f"Location: {job.location}")
    print("---")

# Save the job postings to a CSV file
save_to_csv(job_postings, 'job_postings.csv')
