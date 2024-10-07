import sqlite3
import sys
from bs4 import BeautifulSoup

def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator='\n', strip=True)  # Extract text, handle whitespace

def extract_and_clean_unread_items(db_path, output_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT T2.title, T2.content
            FROM rss_feed AS T1
            INNER JOIN rss_item AS T2
              ON T1.rssurl = T2.feedurl
            WHERE
              T2.unread = 1;
        """)

        with open(output_file, 'w', encoding='utf-8') as f:  # Specify encoding for proper handling of characters
            for row in cursor:
                title = clean_html(row[0])
                content = clean_html(row[1])

                f.write(f"Title: {title}\n\n")
                f.write(f"Content: {content}\n\n{'=' * 80}\n\n") # Separator between items

    finally:
        conn.close()


if __name__ == "__main__":
    db_path = sys.argv[1]
    output_file = sys.argv[2]
    extract_and_clean_unread_items(db_path, output_file)
