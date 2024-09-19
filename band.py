class Band:
    def __init__(self, band_id: int, name: str, hometown: str, conn):
        self.band_id = band_id
        self.name = name
        self.hometown = hometown
        self.conn = conn

    def play_in_venue(self, venue_title: str, date: str):
        venue_id = self.get_venue_id(venue_title)
        if venue_id is None:
            print(f"Venue '{venue_title}' not found.")
            return None

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO concerts (band_id, venue_id, date) VALUES (%s, %s, %s) RETURNING id",
                    (self.band_id, venue_id, date)
                )
                concert_id = cursor.fetchone()[0]
                print(f"{self.name} played at {venue_title} on {date}. Concert ID: {concert_id}")
                return {"concert_id": concert_id, "venue_title": venue_title, "date": date}
        except Exception as e:
            print(f"Error occurred while trying to play in venue: {e}")
            return None

    def get_venue_id(self, venue_title: str) -> int:
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id FROM venues WHERE title = %s", (venue_title,))
            result = cursor.fetchone()
            return result[0] if result else None
