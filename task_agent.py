import os
from dotenv import load_dotenv
# from google import genai
from openai import OpenAI


load_dotenv()

# Configure with your API Key
client = OpenAI(api_key=os.getenv("GOOGLE_API_KEY"),
base_url="https://generativelanguage.googleapis.com/v1beta/openai")


#load env
load_dotenv()

#read task from file 

def read_tasks(filepath):
   with open(filepath, 'r') as f:
      return f.read()


def summarize_tasks(tasks):
   prompt = f"""
   You are a smart task summarizer and planning agent. 
   Given a list of tasks , categorize them into 3 prority buckets
   - High Priority
   - Medium Priority
   - Low Priority

    Task:
    {tasks}

   Return the response in the format:

   High Priority:
   - Task 1
   - Task 2
   - Task 3

   Medium Priority:
   - Task 1
   - Task 2
   - Task 3

   Low Priority:
   - Task 1
   - Task 2
   - Task 3
   """
   response = client.chat.completions.create(
      model="gemini-2.0-flash",
      messages=[
         {"role": "user", "content": prompt}
      ]
   )
   return response.choices[0].message.content

if __name__ == "__main__":
   tasks = read_tasks("task.txt")
   summary = summarize_tasks(tasks)
   print("\nTask Summary:\n")
   print(summary)
      