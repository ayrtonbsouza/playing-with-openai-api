import streamlit as st
import openai
from dotenv import load_dotenv,find_dotenv
_ = load_dotenv(find_dotenv())
client = openai.OpenAI()

def transcribe_audio(audio_file, language='pt', response_format='text'):
  with open(audio_file, 'rb') as file:
    transcription = client.audio.transcriptions.create(
      model='whisper-1',
      language=language,
      response_format=response_format,
      file=file,
    )
  return transcription

def chat(
    message,
    model="gpt-3.5-turbo-0125",
):
  messages = [{'role': 'user', 'content': message}]
  response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,
    stream=False
  )
  return response.choices[0].message.content

def record_meetind_tab():
  st.markdown('record_meeting_tab')

def select_previous_tab():
  st.markdown('select_previous_tab')

def main():
  st.header('Welcome to meet-gpt! 🎙️', divider=True)
  record_tab, select_tab = st.tabs(['Record meeting', 'See previous transcriptions'])
  with record_tab:
    record_meetind_tab()
  with select_tab:
    select_previous_tab()

if __name__ == '__main__':
  main()