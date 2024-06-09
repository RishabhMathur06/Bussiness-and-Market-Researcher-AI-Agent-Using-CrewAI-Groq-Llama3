from crewai import Crew, Process
from tasks import task_entreprenuer, task_market_researcher
from agents import market_researcher, entreprenuer_agent

crew = Crew(
    agents=[market_researcher, entreprenuer_agent],
    tasks=[task_market_researcher, task_entreprenuer],
    verbose=2,
    max_rpm=29
)

result = crew.kickoff(
    inputs={"idea":"oversized tshirts in Mumbai India"}
)
print(result)
