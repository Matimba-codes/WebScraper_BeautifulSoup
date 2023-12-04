# import package for fetching HTML data
import requests
# import package for parsing HTML data
from bs4 import BeautifulSoup


class movieReview:
    @staticmethod
    def get_movie_review():
        # prompt to user enters title of the movie
        movie_title = input("Which movie's review would you like to see? : ")

        # clean up the movie title by removing special characters and spaces
        # and replacing them with underscores to work with the url
        special_characters = [";", "'", ":", "!", "*", ".", "&", "%", "+", "-"]
        for character in special_characters:
            movie_title = movie_title.replace(character, "")
            movie_title = movie_title.replace(" ", "_")

        # create the URL for the Rotten Tomatoes page
        url = f"https://www.rottentomatoes.com/m/{movie_title.lower()}"

        # make a GET request to the Rotten Tomatoes page
        page = requests.get(url)

        # parse the HTML of the page using BeautifulSoup
        soup = BeautifulSoup(page.text, "html.parser")

        # success code - 200
        print(page)
        print(url)

        # print the title of the page to check if it matches the movie title
        print(soup.title.text)

        # find the critics consensus and print it out
        print("Critics Consensus")
        description = soup.find("p", class_="description")
        lines = description.find_all("span")
        for line in lines:
            print(line.text.strip())

        # find the movie description and print it out
        print("Movie Description")
        description = soup.find("div", class_="panel-body content_body")
        lines = description.find("p")
        for line in lines:
            print(line.text.strip())

        # find the critic score and the audience score with the score-board-deprecated tag
        score_board = soup.find("score-board-deprecated")

        # extract the values of the scores
        audience_score = score_board["audiencescore"]
        tomatometer_score = score_board["tomatometerscore"]
        tomatometer_state = score_board["tomatometerstate"]

        # print the scores
        print(f"Audience Score: {audience_score}%")
        print(f"Tomatometer Score: {tomatometer_score}%, Certified: {tomatometer_state}")

        # add reviews as text
        critic_name = soup.find("a", class_="critic-name").text.strip()
        critic_source = soup.find("a", class_="critic-source p--xsmall").text.strip()

        # fetch the text from the review tag
        score_board = soup.find("review-speech-balloon-deprecated")
        reviewquote = score_board["reviewquote"]

        print("The most recent critic review was made by:")
        print(f"{critic_name} from {critic_source} who wrote: {reviewquote}")


class seriesReview:
    @staticmethod
    def get_series_review():
        # prompt to user enters title of the series
        series_title = input("Which series' review would you like to see? : ")

        # clean up the series title by removing special characters and spaces
        # and replacing them with underscores to work with the url
        special_characters = [";", "'", ":", "!", "*", ".", "&", "%", "+", "-"]
        for character in special_characters:
            series_title = series_title.replace(character, "")
            series_title = series_title.replace(" ", "_")

        # create the URL for the Rotten Tomatoes page
        url = f"https://www.rottentomatoes.com/tv/{series_title.lower()}"

        # make a GET request to the Rotten Tomatoes page
        page = requests.get(url)

        # parse the HTML of the page using BeautifulSoup
        soup = BeautifulSoup(page.text, "html.parser")

        # success code - 200
        print(page)
        print(url)

        # print the title of the page to check if it matches the movie title
        print(soup.title.text)

        # find the series description and print it out
        print("Series Description")
        description = soup.find("div", class_="content")
        lines = description.find("p")
        for line in lines:
            print(line.text.strip())

        season_list_items = soup.find_all("season-list-item")

        # Iterate through each season list item
        for season_list_item in season_list_items:
            # extract the season title
            season_title = season_list_item["seasontitle"]

            # extract the percentage and state of the tomato
            percentage = season_list_item["tomatometerscore"]
            state = season_list_item["tomatometerstate"]

            # extract the season list item consensus
            consensus = season_list_item["consensus"]

            # print the season details
            print(f"Season: {season_title}")
            print(f"Tomatometer Score: {percentage}%, Certified: {state}")
            print(f"Consensus: {consensus}")
            print("--------")

        # find the critic score and the audience score with the score-board-deprecated tag
        score_board = soup.find("score-board-deprecated")

        # extract the values of the scores
        audience_score = score_board["audiencescore"]
        tomatometer_score = score_board["tomatometerscore"]
        tomatometer_state = score_board["tomatometerstate"]

        # print the scores
        print(f"Overall Rating For The Entire Series")
        print(f"Audience Score: {audience_score}%")
        print(f"Tomatometer Score: {tomatometer_score}%, Certified: {tomatometer_state}")


if __name__ == "__main__":
    # prompt to user enters title of the movie or series they want
    print("Web Scraping - Reviews From Rotten Tomatoes")
    reviewType_selection = input("Would you like to the review of a movie or a series?: ")

    if reviewType_selection == "movie":
        movieReview.get_movie_review()
    elif reviewType_selection == "series":
        seriesReview.get_series_review()
