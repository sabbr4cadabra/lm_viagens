from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler
from uuid import uuid4 as uuid
from faker import Faker  # gerar dados aleatórios
import pytest # type: ignore

db_connection_handler.connect()
trip_id = str(uuid())
link_id = str(uuid())
faker = Faker()


# @pytest.mark.skip(
#     reason="Interactive with database, not use 'cause errors from unique constraints they can occur"
# ) 
def test_registry_link():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "algum.com.br",
        "title": faker.word(),
    }

    links_repository.registry_link(links_infos)


@pytest.mark.skip(
    reason="Interactive with database, not use 'cause errors from unique constraints they can occur"
)
def test_find_links_from_trip():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    response = links_repository.find_links_from_trip(trip_id)
    print()
    print(response)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)