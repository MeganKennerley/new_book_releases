from bs4 import BeautifulSoup
import requests
import csv


def get_book():
    url = YOUR BOOK WEBSITE
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    book_card = soup.find_all(class_="coverWrapper")

    link_list = []
    book_list = []
    i = 0

    for book in book_card:
        i += 1
        if i == 10:
            break
        link = book.find("a")
        details_href = link['href']
        link_list.append(details_href)

    for link in link_list:
        url = f"{link}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        name_raw = soup.find(class_="Text__title1")
        if name_raw is None:
            continue
        name = name_raw.text

        author_raw = soup.find(class_="ContributorLink__name")
        author = author_raw.text

        rating_raw = soup.find(class_="RatingStatistics__rating")
        rating = rating_raw.text

        book_list.append([name, author, rating])

    return book_list


def create_csv():
    book_list = get_book()

    with open('new_books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["name", "author", "rating"]

        writer.writerow(field)
        for book in book_list:
            writer.writerow([book])


def main():
    create_csv()


if __name__ == "__main__":
    main()