from faker import Faker

fake = Faker()


def get_random_user():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "birth_date": fake.date(pattern="%m/%d/%Y"),
    }
