class Venue:
    def __init__(self, venue_id: int, title: str, city: str, conn):
        self.venue_id = venue_id
        self.title = title
        self.city = city
        self.conn = conn

    def most_frequent_band(self) -> str:
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                SELECT b.name, COUNT(c.id) AS concert_count
                FROM concerts c
                JOIN bands b ON c.band_id = b.id
                WHERE c.venue_id = %s
                GROUP BY b.name
                ORDER BY concert_count DESC
                LIMIT 1;
                """, (self.venue_id,))
                result = cursor.fetchone()
                if result:
                    band_name, concert_count = result
                    return f"The most frequent band is {band_name} with {concert_count} concerts."
                else:
                    return "No concerts found."
        except Exception as e:
            return f"Error occurred: {e}"
