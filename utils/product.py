from faker import Faker

fake = Faker()


def get_random_product():
    return {
        "product_name": fake.word().title() + " " + fake.word().title(),
        "summary": fake.sentence(nb_words=6),
        "description": fake.paragraph(nb_sentences=3),
    }
