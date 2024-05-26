# joboard-crawler
## Project Overview

A simple scraper for a job website in Poland and Germany. A Python script for scraping job listings from various websites.

     ## Features

     - Parses job listings from multiple sources.
     - Retrieves job titles, salaries, contract types, and locations.
     - Supports websites like oferta.gov.pl, OLX, RocketJobs, GoWork, and Praca.pl.
     ```


## Setup
```
pipenv install
pipenv shell
```

## Running Script

```buildoutcfg
python crawler.py
```
     ## Installation

     1. Clone the repository.
     2. Install required Python packages

     ## Usage

     - The script will scrape job listings from different websites and create a list of job details.
     - Modify the URLs in the script to target specific websites.

     ## Code Structure

     - `parse_oferta_gov_pl()`: Scrapes job listings from oferta.gov.pl.
     - `parse_olx_pl()`: Retrieves job details from OLX.
     - Google Collab .ipynb files

     Contributions are welcome! Feel free to open an issue or submit a pull request.
