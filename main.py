from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8000/mcp",
    "transport": "streamable-http",
}

# Using Gemini LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

try:
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools: {[tool.name for tool in tools]}")

        scraper_agent = Agent(
            role="Scraper Agent",
            goal="Scrape the website for getting the porfolio information of SoftwareOne Company",
            backstory="You are a web scraper agent that can scrape the website for getting the {portfolio_type} porfolio information of SoftwareOne Company. the website is https://www.softwareone.com/es-co/{portfolio_type}",
            verbose=True,
            tools=tools,
            llm=llm,
        )

        scraper_task = Task(
            description="Scrape the website for getting the {portfolio_type} porfolio information of SoftwareOne Company. the website is https://www.softwareone.com/es-co/{portfolio_type}",
            expected_output="The {portfolio_type} of SoftwareOne Company offers the following services: Cloud Services, Digital Transformation, Cybersecurity, IT Services.",
            agent=scraper_agent,
        )

        crew = Crew(
            agents=[scraper_agent],
            tasks=[scraper_task],
            verbose=True,
            process=Process.sequential,
        )

        result = crew.kickoff(
            inputs={
                "portfolio_type": "Digital Workplace Services"
            }
        )
        print(result)
except Exception as e:
    print(f"Error: {e}")