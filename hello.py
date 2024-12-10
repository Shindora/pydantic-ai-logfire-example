import os
from typing import cast
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from dotenv import load_dotenv
from pydantic_ai.models.openai import OpenAIModel

load_dotenv(".env")
logfire.configure(token=os.getenv("LOGFIRE_TOKEN", None))


class MyModel(BaseModel):
    city: str
    country: str


model = OpenAIModel("gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
agent = Agent(model, result_type=MyModel)

if __name__ == "__main__":
    result = agent.run_sync("The windy city in the US of A.")
    print(result.data)
    print(result.cost())
