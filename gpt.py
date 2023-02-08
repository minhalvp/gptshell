import openai
import subprocess
import platform
import typer
from typing import List
import os

# openai.api_key = "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"
if 'OPENAI_API' not in os.environ:
  key = input("Enter your OpenAI API key:") 
  os.environ['OPENAI_API'] = key

openai.api_key = os.environ['OPENAI_API']

app = typer.Typer()

@app.command()
def text(text: List[str]):
  text = " ".join(text)

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Convert this text to a programmatic {platform.system()} command: {text}",
    temperature=.5,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.2,
    presence_penalty=0.0,
  )

  response = response['choices'][0]['text']
  print(response)
  proc = subprocess.run(["powershell", "-Command", response], capture_output=True)
  print(proc.stdout.decode("utf-8"))

if __name__ == "__main__":
  app()