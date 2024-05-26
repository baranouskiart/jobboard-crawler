# joboard-crawler


1. ** Project Overview**

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


2. **Installation and Usage**:
   - Provide clear instructions on how to install and run your project.
   - Include any prerequisites (e.g., Python version, required libraries).
   - Describe how to execute your script.
   - For example:
     ```markdown
     ## Installation

     1. Clone the repository.
     2. Install required Python packages:
        ```
        pip install beautifulsoup4 requests
        ```
     3. Run the script:
        ```
        python main.py
        ```

     ## Usage

     - The script will scrape job listings from different websites and create a list of job details.
     - Modify the URLs in the script to target specific websites.
     ```

3. **Code Structure**:
   - Briefly explain the purpose of each function in your code.
   - For example:
     ```markdown
     ## Code Structure

     - `parse_oferta_gov_pl()`: Scrapes job listings from oferta.gov.pl.
     - `parse_olx_pl()`: Retrieves job details from OLX.
     - ...
     ```

4. **Examples and Screenshots**:
   - Include examples of how to use your script.
   - If applicable, add screenshots or sample output.
   - For example:
     ```markdown
     ## Examples

     - Running `parse_oferta_gov_pl()`:
       ```
       [{'title': 'Software Engineer', 'salary': '$80,000 - $100,000', 'contract_type': 'Full-time', 'location': 'Warsaw, Poland'}, ...]
       ```

     - Screenshot of parsed job listings:
       ![Screenshot](screenshots/job_listings.png)
     ```

5. **Contributing and Contact**:
   - Encourage other developers to contribute.
   - Provide contact information (GitHub profile, email) for questions or collaboration.
   - For example:
     ```markdown
     ## Contributing

     Contributions are welcome! Feel free to open an issue or submit a pull request.
