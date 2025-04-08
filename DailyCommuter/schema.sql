DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;


CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE subway_alerts (
    alert_id TEXT,
    agency_id TEXT,
    route_id INTEGER,
    alert_text TEXT,
    description_text TEXT
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