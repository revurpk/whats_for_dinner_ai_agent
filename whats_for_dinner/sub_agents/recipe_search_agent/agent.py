#  Copyright (c) 2025 Pradyumna K Revur

"""recipe_search_agent for finding recipes using google search"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

recipe_search_agent = Agent(
    model='gemini-2.5-flash',
    name='recipe_search_agent',
    instruction=prompt.RECIPE_SEARCH_PROMPT,
    output_key="recipe_search_output",
    tools=[google_search],
)
