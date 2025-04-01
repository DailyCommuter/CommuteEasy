# API URLs for all except for bus updates which has an API key. (Stored in .env)
TRAIN_UPDATE_BASE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"
ACESR_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-ace"
BDFM_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-bdfm"
G_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-g"
NQRW_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-nqrw"
L_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-l"
NUMBERS_AND_S_FEED_URL = TRAIN_UPDATE_BASE_URL
SIR_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-si"
LIRR_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-lirr"
METRO_NORTH_FEED_URL = f"{TRAIN_UPDATE_BASE_URL}-mnr"


# Discovery (static) service information
BUS_TRIP_UPDATES_URL = "https://gtfsrt.prod.obanyc.com/tripUpdates?key="
BUS_VEHICLE_POSITIONS_URL = "https://gtfsrt.prod.obanyc.com/vehiclePositions?key="
BUS_ALERTS_URL = "https://gtfsrt.prod.obanyc.com/alerts?key="
# TODO confirm urls for OneBusAway API and possibly SIRI API?


SERVICE_ALERT_BASE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2F"
ALL_SERVICE_ALERTS_URL_GTFS = f"{SERVICE_ALERT_BASE_URL}all-alerts"
ALL_SERVICE_ALERTS_URL_JSON = f"{SERVICE_ALERT_BASE_URL}all-alerts.json"
SUBWAY_ALERTS_URL_GTFS = f"{SERVICE_ALERT_BASE_URL}subway-alerts"
SUBWAY_ALERTS_URL_JSON = f"{SERVICE_ALERT_BASE_URL}subway-alerts.json"
BUS_ALERTS_URL_GTFS = f"{SERVICE_ALERT_BASE_URL}bus-alerts"
BUS_ALERTS_URL_JSON = f"{SERVICE_ALERT_BASE_URL}bus-alerts.json"
LIRR_ALERTS_URL_GTFS = f"{SERVICE_ALERT_BASE_URL}lirr-alerts"
LIRR_ALERTS_URL_JSON = f"{SERVICE_ALERT_BASE_URL}lirr-alerts.json"
METRO_NORTH_ALERTS_URL_GTFS = f"{SERVICE_ALERT_BASE_URL}mnr-alerts"
METRO_NORTH_ALERTS_URL_JSON = f"{SERVICE_ALERT_BASE_URL}mnr-alerts.json"


ELEV_ESCAL_BASE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene"
ELEV_ESCAL_CURRENT_OUTAGES_XML = f"{ELEV_ESCAL_BASE_URL}.xml"
ELEV_ESCAL_CURRENT_OUTAGES_JSON = f"{ELEV_ESCAL_BASE_URL}.json"
ELEV_ESCAL_UPCOMING_OUTAGES_XML = f"{ELEV_ESCAL_BASE_URL}_upcoming.xml"
ELEV_ESCAL_UPCOMING_OUTAGES_JSON = f"{ELEV_ESCAL_BASE_URL}_upcoming.json"
ELEV_ESCAL_EQUIPMENTS_XML = f"{ELEV_ESCAL_BASE_URL}_equipments.xml"
ELEV_ESCAL_EQUIPMENTS_OUTAGES_JSON = f"{ELEV_ESCAL_BASE_URL}_equipments.json"