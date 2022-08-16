import json
import ast
import json
from naver_core import *


class TourDto(object):
    def __init__(self, value):
        # from Frontend
        tour = value.get("tour") or None
        logistic = value.get("logistic") or None
        arrival_date = logistic.get("arrival_date") or None
        departure_date = logistic.get("departure_date") or None
        customer = value.get("customer") or None
        destinations = value.get("destinations") or None
        day = (departure_date - arrival_date).days + 1
        # to DataBase
        self.tour_id = tour.get("code")
        self.valid = logistic.get("until_date")
        self.destination_country_id = tour.get("country")
        self.purposes = (tour.get("purposes"))
        self.accomodation_type_id = tour.get("accomodation_type")
        self.arrival_date = logistic.get("arrival_date")
        self.departure_date = logistic.get("departure_date")
        self.passengers = tour.get("passengers")
        self.days = day
        self.nights = self.days - 1
        self.description = tour.get("travel_code")
        self.client_id = customer.get("client_dni")
        self.tour = json.dumps(tour, indent=4, sort_keys=True, default=str)
        self.customer = json.dumps(
            customer, indent=4, sort_keys=True, default=str)
        self.logistic = json.dumps(
            logistic, indent=4, sort_keys=True, default=str)
        self.destinations = json.dumps(destinations)
        self.detail = json.dumps(
            self.toDict(), indent=4, sort_keys=True, default=str)

    # to DataBase
    def toDict(self):
        return {
            "tour_id": self.tour_id,
            "destinations": self.destinations,
            "valid": self.valid,
            "destination_country_id": self.destination_country_id,
            "purposes": self.purposes,
            "accomodation_type_id": self.accomodation_type_id,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "passengers": self.passengers,
            "days": self.days,
            "nights": self.nights,
            "description": self.description,
            "client_id": self.client_id,
            "tour": self.tour,
            "customer": self.customer,
            "logistic": self.logistic,
        }

    # from DataBase
    def __dict__(self):
        return {
            "tour_id": self.tour_id,
            "destinations": self.destinations,
            "valid": self.valid,
            "destination_country_id": self.destination_country_id,
            "purposes": self.purposes,
            "accomodation_type_id": self.accomodation_type_id,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "passengers": self.passengers,
            "days": self.days,
            "nights": self.nights,
            "description": self.description,
            "client_id": self.client_id,
            "detail": self.detail,
            "tour": self.tour,
            "customer": self.customer,
            "logistic": self.logistic,
        }
