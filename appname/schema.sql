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
  update_id TEXT,
  trip_id TEXT,
  start_tm TEXT,
  start_dt TEXT,
  route_id TEXT,
  arrival INTEGER,
  departure INTEGER,
  stop_id TEXT,
  timestmp INTEGER,
  curr_stop_id TEXT
);