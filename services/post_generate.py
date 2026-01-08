from faker import Faker

fake = Faker()


def get_random_post():
    return {
        "userId": fake.random_int(min=0, max=10),
        "title": fake.sentence(),
        "body": fake.sentence(),
    }
