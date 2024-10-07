#!/bin/bash


# Copyright (C) 2024  luvchurchill

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Set paths and filenames
DB_FILE="$HOME/.newsboat/cache.db"  # Path to your SQLite database
ARTICLES_FILE="unread_articles.txt"  # Temporary file to store extracted articles
SUMMARIES_FILE="summaries.md" # File to store the summaries

# Extract unread articles from the database using the Python script
python3 extract_and_clean.py "$DB_FILE" "$ARTICLES_FILE"

# Check if article extraction was successful
if [[ $? -ne 0 ]]; then
    echo "Error extracting articles. Exiting."
    exit 1
fi

# Generate summaries using the Gemini script with chunking
python3 gemini.py -c "$ARTICLES_FILE" > "$SUMMARIES_FILE"


# Optional: remove the temporary articles file
# rm "$ARTICLES_FILE"

echo "Summaries written to $SUMMARIES_FILE"
