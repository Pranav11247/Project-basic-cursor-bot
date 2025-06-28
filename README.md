# Project-basic-cursor-bot
# Summarizer using SambaNova + pyautogui

This script automates text selection on screen and uses the SambaNova API to summarize the selected content in one line using Llama-4-Maverick.

## Features

- Automates mouse and keyboard to select and copy text
- Calls a SambaNova-hosted LLM to summarize the copied content
- Prints the result to console

## Requirements

- Python 3.8+
- [SambaNova API access](https://api.sambanova.ai/)
- OpenAI SDK (`pip install openai`)
- pyautogui, pyperclip
