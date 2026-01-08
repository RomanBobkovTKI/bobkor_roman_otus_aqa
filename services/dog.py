from models.dog import DogRandom, Dogs
from services.base_client import BaseClient


class DogService(BaseClient):
    def get_random_dog(self):
        response = self.get("breed/hound/images/random")
        data = response.json()

        return DogRandom(**data)

    def get_dog_by_breed_without_params(self):
        response = self.get("breed/hound/images")
        data = response.json()

        return Dogs(**data)

    def get_dog_by_breed(self, breed):
        response = self.get(f"breed/{breed}/images/random")
        data = response.json()

        return DogRandom(**data)

    def get_dog_by_count(self, count):
        response = self.get(f"breed/hound/images/random/{count}")
        data = response.json()

        return Dogs(**data)
