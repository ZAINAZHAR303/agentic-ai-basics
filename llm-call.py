from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

import os
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Simple text invocation
result = llm.invoke("Sing a ballad of LangChain.")
print(result.content)

# Multimodal invocation with gemini-pro-vision
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "What's in this image?",
        },
        {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
    ]
)
result = llm.invoke([message])
print(result.content)






# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv
# import os
# load_dotenv()

# llm = GoogleGenerativeAI(
#      model="gemini-1.5-flash",
#      google_api_key=GOOGLE_API_KEY
# )

# result = llm.invoke("What is the capital of pakistan?")

# print(result)

