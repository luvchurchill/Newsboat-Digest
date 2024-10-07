# Newsboat Feed Summarizer with Google Gemini

This project uses Google Gemini to generate summaries of your unread Newsboat feeds. It extracts unread articles from your Newsboat database, cleans the HTML content, and then sends them to the Gemini API for summarization.

## Prerequisites

* **Newsboat:**  This script assumes you are using Newsboat and that your database is located at `$HOME/.newsboat/cache.db`.
* **Python 3:** Make sure you have Python 3 installed.
* **Google Gemini API Key:** You need a Gemini API key. You can obtain one from [Google's AI Studio]
(https://aistudio.google.com/app/).  Set the environment variable `GEMINI_API_KEY` to your key's value.
* **Required Python Packages:** Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. **Create a python virtual environment and install dependencies:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Make `summarize.sh` executable:**

```bash
chmod +x summarize.sh
```

3. **Run the script:**

```bash
./summarize.sh
```

The script will extract unread articles from your Newsboat database, send them to Gemini for summarization, and save the summaries to `summaries.md`.

## Configuration

* **Database Path:** The Newsboat database path is hardcoded to `$HOME/.newsboat/cache.db`.  You can modify the `DB_FILE` variable in `summarize.sh` if your database is located elsewhere.
* **Gemini API Key:** Set your Gemini API key in the `GEMINI_API_KEY` environment variable.
* **Chunking and Timeout:** The `gemini.py` script sends the articles to the Gemini API in chunks to avoid timeout issues. The `chunk_size` and `sleep_duration` parameters in `send_chunked_message` within  `gemini.py` control the chunk size and the delay between chunks respectively. You may want to adjust these values depending on your API key limitations (e.g., if you have a paid key with higher rate limits).
* **System Prompt:** The `feed_summary_system_prompt` variable in `gemini.py` contains the instructions given to the Gemini model.  You can modify this prompt to tailor the summarization behavior.
* **Model:** The `model_name` in `gemini.py` is set to  `gemini-1.5-flash`. You might want to adjust this depending on availability and your preference.

## Troubleshooting

* **`sqlite3.OperationalError: unable to open database file`:** Ensure the script has read access to the database file and that the path is correct.
* **`sh: 12: [[: not found`:** Make sure you are running the `summarize.sh` script with Bash (e.g., `bash summarize.sh` or `./summarize.sh` after making it executable with `chmod +x`).
* **API Errors:**  Check the Gemini API documentation for error codes and troubleshooting tips.

## License


Copyright (C) 2024  luvchurchill

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.