import psycopg2
from band import Band
from concert import Concert
from venue import Venue

def setup_database_connection():
    return psycopg2.connect(
        dbname="concert",
        user="cindy",
        password="CODEWITHME",
        host="localhost"
    )

def setup_initial_data(conn):
    with conn.cursor() as cursor:
        # Insert a band
        cursor.execute("""
        INSERT INTO bands (id, name, hometown) VALUES (1, 'Morgan Heritage', 'Anfield')
        ON CONFLICT (id) DO NOTHING;
        """)

        # Insert a venue
        cursor.execute("""
        INSERT INTO venues (id, title, city) VALUES (1, 'Visa Palace', 'Liverpool')
        ON CONFLICT (id) DO NOTHING;
        """)

def main():
    try:
        conn = setup_database_connection()
        
        # Set up initial data
        setup_initial_data(conn)

        band = Band(band_id=1, name="Morgan Heritage", hometown="Anfield", conn=conn)
        band.play_in_venue("Visa Palace", "1961-02-09")

        concert = Concert(concert_id=1, band_id=1, venue_id=1, date="1961-02-09", conn=conn)
        print(concert.introduction())

        venue = Venue(venue_id=1, title="Visa Palace", city="Liverpool", conn=conn)
        print(venue.most_frequent_band())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
