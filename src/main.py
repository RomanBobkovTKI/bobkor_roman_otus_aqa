import json
import csv

def get_users_from_file(filename):
    result = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = f.read()
        users_list = json.loads(reader)

        for user in users_list:
            result.append({
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age']
            })

    return result

def get_books_list(filename):
    result = []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        books_list = list(reader)

        for book in books_list:
            result.append({
                'title': book['Title'],
                'author': book['Author'],
                'genre': book['Genre'],
                'pages': book['Pages'],
            })

    return result

def save_users_to_file(filename, users_list):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(users_list, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    users = get_users_from_file('users.json')
    users_count = len(users)
    books = get_books_list('books.csv')
    books_count = len(books)
    print(users_count, books_count)

    if books_count <= users_count:
        raise ValueError('Количество книг должно быть больше количества пользователей')

    base = books_count // users_count
    remainder = books_count % users_count

    book_index = 0

    for i, user in enumerate(users):
        num_books = base + (1 if i < remainder else 0)

        user_books = books[book_index: book_index + num_books]
        user['books'] = user_books

        book_index += num_books

    save_users_to_file('result.json', users)