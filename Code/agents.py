from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import tool

load_dotenv()

import os

llama = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

market_researcher = Agent(
    role="Senior market researcher",
    goal="Ensure the business {idea} is backed by solid research and data \n"
    "Carry out a comprehensive and realistic research for the given {idea}."
    "Provide insights of your research to the enterpeneur.",
    backstory="You are an expert market researcher skilled at validating business ideas"
              "You are skilled at doing market research for a given {idea}"
              "You have worked with numerous startups and established companies, helping them identify market trends and develop successful business strategies."
              "Your expertise lies in giving research reports for a given {idea}.",
    allow_designation=False,
    verbose=True,
    llm=llama
)

entreprenuer_agent = Agent(
    role="Experienced Entrepreneur",
    goal="Create a marketing plan and business plan for {idea}",
    backstory="You have built more than 10 successful companies."
              "You are skilled at creating business ideas and marketing plans"
              "You possess high experience in crafting business and marketing plans"
              "You need to make sure that proper business plan and marketing plan is generated for {idea}",
    verbose=True,
    allow_designation=False,
    llm=llama
)