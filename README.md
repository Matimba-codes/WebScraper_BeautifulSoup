# WebScraper_BeautifulSoup
A README.md file for WebScraper_BeautifulSoup on GitHub:

# Rotten Tomatoes Review Scrapper

This project is a web scraper that fetches movie and series reviews from Rotten Tomatoes. It utilizes the Python libraries requests and BeautifulSoup to retrieve and parse HTML data from Rotten Tomatoes' website. The scraper prompts the user to enter the title of the movie or series they want to review and then displays the following information:

**For Movies:**

- Critics Consensus
- Movie Description
- Audience Score
- Tomatometer Score
- Most Recent Critic Review

**For Series:**

- Series Description
- Tomatometer Score and Certified Status for Each Season
- Series Consensus for Each Season
- Overall Audience Score
- Overall Tomatometer Score

## Usage

To use this scraper, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4
    ```
3. Open a terminal window and navigate to the project directory.
4. Run the scraper using the following command:
    ```bash
    python scraper.py
    ```
5. Follow the prompts to enter the title of the movie or series you want to review.

## Contributing

Contributions to this project are welcome! Please feel free to open pull requests with your suggested improvements.

## License

This project is licensed under the MIT License.
