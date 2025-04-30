DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS subway_alerts;
DROP TABLE IF EXISTS trip_update;
DROP TABLE IF EXISTS stop_update;
DROP TABLE IF EXISTS vehicle_update;
DROP TABLE IF EXISTS subway_stops;
DROP TABLE IF EXISTS subway_routes;
DROP TABLE IF EXISTS subway_trips;
DROP TABLE IF EXISTS subway_stop_times;
DROP TABLE IF EXISTS routes;


CREATE TABLE user (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE subway_alerts (
    alert_id TEXT,
    agency_id TEXT,
    route_id TEXT,
    stop_id TEXT,
    alert_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE trip_update (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_id TEXT NOT NULL UNIQUE,
    trip_id TEXT,
    start_tm TEXT,
    start_dt TEXT,
    route_id TEXT
);


CREATE TABLE stop_update (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_update_id INTEGER NOT NULL,
    arrival INTEGER,
    departure INTEGER,
    stop_id TEXT,
    direction TEXT,
    FOREIGN KEY (trip_update_id) REFERENCES trip_update(id)
);


CREATE TABLE vehicle_update (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_update_id INTEGER NOT NULL,
    timestmp INTEGER,
    curr_stop_id TEXT,
    FOREIGN KEY (trip_update_id) REFERENCES trip_update(id)
);


CREATE TABLE subway_stops (
    global_stop_id TEXT PRIMARY KEY,
    parent_station_global_stop_id TEXT NOT NULL,
    route_type INTEGER NOT NULL,
    rt_stop_id TEXT NOT NULL,
    stop_lat REAL,
    stop_lon REAL,
    stop_name TEXT NOT NULL,
    wheelchair_boarding INTEGER
);


CREATE TABLE subway_routes (
    route_id TEXT PRIMARY KEY,
    route_short_name TEXT NOT NULL,
    route_long_name TEXT NOT NULL,
    route_color TEXT NOT NULL
);


-- Maps each trip to a route (a trip is a specific instance of a vehicle's movement)
CREATE TABLE subway_trips (
    trip_id	TEXT PRIMARY KEY,
    route_id INTEGER NOT NULL,
    service_id TEXT NOT NULL,
    trip_headsign TEXT NOT NULL,
    direction INTEGER NOT NULL,
    shape_id TEXT NOT NULL,
    FOREIGN KEY (route_id) REFERENCES subway_routes(route_id)
);


-- Maps each stop to a trip (defines the stop sequence in a trip)
CREATE TABLE subway_stop_times (
    trip_id	TEXT NOT NULL,
    stop_id	TEXT NOT NULL,
    arrival_time TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    stop_sequence INTEGER NOT NULL,
    PRIMARY KEY (trip_id, stop_sequence),
    FOREIGN KEY (trip_id) REFERENCES subway_trips(trip_id),
    FOREIGN KEY (stop_id) REFERENCES subway_stops(gtfs_stop_id)
);


CREATE TABLE routes (
	routeid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    route_name TEXT NOT NULL,
	start_address TEXT NOT NULL,
	end_address TEXT NOT NULL,
	arrival_time TEXT NOT NULL,
	start_lat REAL,
	start_lon REAL,
	end_lat REAL,
	end_lon REAL,
	userid INTEGER NOT NULL,
    bestTime INTEGER,
    estimateTime INTEGER,
    FOREIGN KEY (userid) REFERENCES user(userid)
);

CREATE TABLE points (
    pointid INTEGER PRIMARY KEY AUTOINCREMENT,
    routeid INTEGER NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL,
    name TEXT,
    type INTEGER,
    FOREIGN KEY (routeid) REFERENCES routes(routeid) ON DELETE CASCADE
);
