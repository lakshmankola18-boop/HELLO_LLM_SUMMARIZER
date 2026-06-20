# main.py
# This script uses the Hugging Face transformers library to run an AI model locally.
# It uses a pre-trained model to summarize a piece of text.

import os
# We import 'pipeline' from the transformers library. 
# A pipeline is a high-level helper that handles all the complex parts 
# of loading a model and preparing the data for us.
from transformers import pipeline

def main():
    print("Loading the AI summarization model... This might take a few seconds.")
    # Initialize the summarization pipeline.
    # By simply passing "summarization", the pipeline automatically downloads
    # and uses a small, default model (usually 'sshleifer/distilbart-cnn-12-6') 
    # perfectly suited for this task.
    summarizer = pipeline("summarization")
    print("Model loaded successfully!\n")

    # Ask the user if they want to type/paste text or read from sample.txt
    print("How would you like to provide the text?")
    print("1: Type or paste it here")
    print("2: Read from sample.txt")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        # Prompt the user to enter their text. 
        # (Note: input() reads a single line. For multiple lines, a file is better, but this works for a simple paste!)
        text = input("\nPaste your text here to summarize (press Enter when done):\n")
    else:
        # Check if sample.txt exists before trying to read it
        if os.path.exists("sample.txt"):
            print("\nReading text from 'sample.txt'...")
            with open("sample.txt", "r", encoding="utf-8") as f:
                text = f.read()
        else:
            print("\nError: 'sample.txt' not found!")
            return

    # Check if we actually have text to summarize
    if not text or len(text.strip()) == 0:
        print("No text provided. Exiting.")
        return
        
    print("\n--- Original Text ---")
    print(text)
    print("---------------------\n")
    
    print("Generating summary...")
    
    # Run the summarizer on our text!
    # We can control the output size using max_length and min_length.
    # This ensures the summary isn't too long or too short.
    # The output is a list of dictionaries, so we take the first element [0] 
    # and grab the value for the key "summary_text".
    try:
        summary_result = summarizer(text, max_length=60, min_length=15, do_sample=False)
        summary = summary_result[0]["summary_text"]
        
        print("\n=== AI SUMMARY ===")
        print(summary)
        print("==================\n")
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        # Sometimes if the text is too short, the model might complain about min_length/max_length
        print("Tip: Make sure the input text is long enough (at least a few sentences).")

if __name__ == "__main__":
    main()