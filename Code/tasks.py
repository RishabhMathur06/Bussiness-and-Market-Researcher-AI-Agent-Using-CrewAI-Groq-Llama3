from crewai import Task
from tools import tool
from agents import market_researcher, entreprenuer_agent

# Task for market researcher
task_market_researcher = Task(
   description=(
       "Analyze the strengths, weaknesses, opportunities, and threats (SWOT analysis) of the business idea {idea}"
        "Estimate market size and growth potential."
        "Assess the feasibility of the business model."
        "Give your insights for creating a Business Plan."
   ) ,
   expected_output=(
       "A detailed market research report for the mentioned idea {idea}"
        "Include references to external data for market analysis."
   ),
   tools=[tool],
   agent=market_researcher,
)

# Task for entreprenuer
task_entreprenuer = Task(
   description=(
       "Create the marketing plan and business plan for {idea}"
        "Ensure that there are no discrepancies for the generated plans"
        "There should be no inconsistencies in either of the plans"
        "Verify that all important concepts of business and marketing plans are covered."
   ),
   expected_output=(
       "Output should contain two main things: a final business plan for the {idea}\n"
        "A final marketing plan for the {idea}"
   ),
   tools=[tool],
   agent=entreprenuer_agent,
   output_file='idea-analysis.md'
)