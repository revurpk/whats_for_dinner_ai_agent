#  Copyright (c) 2025 Pradyumna K Revur

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.meal_prep_agent import meal_prep_agent
from .sub_agents.nutrition_info_agent import nutrition_info_agent
from .sub_agents.recipe_search_agent import recipe_search_agent

MODEL = "gemini-2.5-flash"

whats_for_dinner = LlmAgent(
    name="whats_for_dinner",
    model=MODEL,
    description=(
        "guide users through a structured process to receive meal prep "
        "advice by orchestrating a series of expert subagents."
    ),
    instruction=prompt.WHATS_FOR_DINNER_PROMPT,
    output_key="whats_for_dinner_output",
    tools=[
        AgentTool(agent=recipe_search_agent),
        AgentTool(agent=meal_prep_agent),
        AgentTool(agent=nutrition_info_agent),
    ],
)

root_agent = whats_for_dinner
