from factory import Factory, Faker

from app.work.models import Work
from app.photo.models import Photo


class PhotoFactory(Factory):
    class Meta:
        model = Photo

    id = Faker("random_int")
    image_url = Faker("word")
    work_id = Faker("random_int")
    created_at = Faker("date_object")
    updated_at = Faker("date_object")
    deleted_at = Faker("date_object")


class WorkFactory(Factory):
    class Meta:
        model = Work

    id = Faker("random_int")
    work = Faker('word')
    image_url = Faker("url")
    created_at = Faker("date_object")
    updated_at = Faker("date_object")
    deleted_at = Faker("date_object")