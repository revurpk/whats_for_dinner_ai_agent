#  Copyright (c) 2025 Pradyumna K Revur

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.meal_prep_agent import meal_prep_agent
from .sub_agents.recipe_search_agent import recipe_search_agent

MODEL = "gemini-2.5-pro"

whats_for_dinner = LlmAgent(
    name="whats_for_dinner",
    model=MODEL,
    description=(
        "guide users through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. help them "
        "analyze a market ticker, develop trading strategies, define "
        "execution plans, and evaluate the overall risk."
    ),
    instruction=prompt.WHATS_FOR_DINNER_PROMPT,
    output_key="whats_for_dinner_output",
    tools=[
        AgentTool(agent=data_analyst_agent),
        AgentTool(agent=trading_analyst_agent),
        AgentTool(agent=execution_analyst_agent),
        AgentTool(agent=risk_analyst_agent),
    ],
)

root_agent = whats_for_dinner
