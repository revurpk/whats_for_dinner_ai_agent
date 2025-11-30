#  Copyright (c) 2025 Pradyumna K Revur

"""meal_prep_agent for meal preparation instructions"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-flash"

meal_prep_agent = Agent(
    model=MODEL,
    name="meal_prep_agent",
    instruction=prompt.MEAL_PREP_PROMPT,
    output_key="meal_prep_output",
)
