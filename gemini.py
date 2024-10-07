import argparse
import google.generativeai as genai
import os
import signal
import sys
import time


def signal_handler(sig, frame):
    """Exit gracefully with ctrl-c"""
    print("\n Bye... ")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 16384,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]
feed_summary_system_prompt = "You will be provided with a feed of articles, you should summarize them for the user. You should not summarize all of them, rather use your judgment to give a mix of important articles, interesting ideas, and some random ones., summaries should be on the shorter side, unless there is value in making it longer, use your judgement."


def send_chunked_message(convo, text, chunk_size=64000, sleep_duration=10):
    for i in range(0, len(text), chunk_size):
        chunk = text[i : i + chunk_size]
        convo.send_message(chunk)
        print(convo.last.text, end="")
        time.sleep(sleep_duration)  # Introduce delay
    print()


def main():
    parser = argparse.ArgumentParser(description="Use Googles Gemini through the API")
    parser.add_argument("-c", "--chunked-file", type=str, help="File to send in chunks")
    args = parser.parse_args()
    system_prompt = feed_summary_system_prompt
    try:
        with open(args.chunked_file, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=system_prompt,
        safety_settings=safety_settings,
    )
    convo = model.start_chat(history=[])
    send_chunked_message(convo, file_content)  # Send chunked content
    

if __name__ == "__main__":
    main()
