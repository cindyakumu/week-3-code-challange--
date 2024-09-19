class Concert:
    def __init__(self, concert_id: int, band_id: int, venue_id: int, date: str, conn):
        self.concert_id = concert_id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        self.conn = conn

    def introduction(self) -> str:
        return f"Concert ID: {self.concert_id}, Band ID: {self.band_id}, Venue ID: {self.venue_id}, Date: {self.date}"

    def __str__(self) -> str:
        return self.introduction()

    def __repr__(self) -> str:
        return f"<Concert(concert_id={self.concert_id}, band_id={self.band_id}, venue_id={self.venue_id}, date='{self.date}')>"
