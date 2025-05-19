from dataclasses import dataclass

@dataclass
class Route:
    id: int = None  # Optional: will be auto-assigned by DB
    start_address: str = ""
    end_address: str = ""
    start_lat: float = 0.0
    start_lon: float = 0.0
    end_lat: float = 0.0
    end_lon: float = 0.0
    arrival_time: str = ""
    userid: int = 0

    @property
    def start_coord(self):
        return(self.start_lat, self.start_lon)

    @property
    def end_coord(self):
        return(self.end_lat, self.end_lon)