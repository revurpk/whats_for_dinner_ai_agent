#  Copyright (c) 2025 Pradyumna K Revur

"""What's for dinner: provide recipe choices for a nutritious meal"""

import os

import google.auth

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "False")

from . import agent
