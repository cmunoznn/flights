
--DATA FLIGHTS TABLE CREATION

CREATE TABLE IF NOT EXISTS  bronze.flights (
    id BIGSERIAL PRIMARY KEY,
    fr24_id TEXT,
    flight TEXT,
    callsign TEXT,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    track INTEGER,
    alt INTEGER,
    gspeed INTEGER,
    vspeed INTEGER,
    squawk TEXT,
    timestamp TIMESTAMPTZ,
    source TEXT,
    hex TEXT,
    type TEXT,
    reg TEXT,
    painted_as TEXT,
    operating_as TEXT,
    orig_iata TEXT,
    orig_icao TEXT,
    dest_iata TEXT,
    dest_icao TEXT,
    eta TIMESTAMPTZ,
    recorded_at TIMESTAMPTZ
);


--DROP TABLE bronze.flights;
--DELETE FROM bronze.flights;

select * from bronze.flights
;


