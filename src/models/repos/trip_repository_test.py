import pytest
import uuid
from datetime import datetime, timedelta
from .trip_repository import TripsRepository
from src.models.settings.db_connection_handle import db_connection_handler

db_connection_handler.connect()

@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trip_rep = TripsRepository(conn)

    trips_info = {
        "id":str(uuid),
        "destination":"Capitólio",
        "start_date": datetime.strptime("09-07-24","%d-%m-%y"),
        "end_date":  datetime.strptime("09-07-24","%d-%m-%y") + timedelta(days=5),
        "owner_name": "Ariel",
        "owner_email": "mymail@email.com"
    }

    trip_rep.create_trip(trips_info)