import json

from faker import Faker

fake = Faker()


def get_user():
    return {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "address": {
            "street": fake.street_address(),
            "suite": fake.building_number(),
            "city": fake.city(),
            "zipcode": fake.zipcode(),
            "geo": {"lat": fake.random_int(min=0, max=15), "lng": fake.random_int(min=0, max=15),},
        },
        "phone": fake.phone_number(),
        "website": fake.url(),
        "company": {
            "name": fake.company(),
            "catchPhrase": fake.catch_phrase(),
            "bs": fake.bs(),
        },
    }