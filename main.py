
import os
from fastapi import FastAPI
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

# Carrega as variáveis de ambiente
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

router = FastAPI()

class Body(BaseModel):
    message: str

storage = SqliteStorage(table_name="agno_sessions", db_file="tmp/agents.db")
memory = Memory(
    db=SqliteMemoryDb(table_name="agno_memory", db_file="tmp/memory.db"),
    model=Gemini(
        id=os.environ['DEFAULT_MODEL'],
        api_key=os.environ['GOOGLE_API_KEYS']
    ),
)

# Configura o agente com a chave de API
agent = Agent(
    session_id="s_125",
    user_id="u_2",
    model=Gemini(
        id=os.environ['DEFAULT_MODEL'],
        api_key=os.environ['GOOGLE_API_KEYS']
    ),
    add_history_to_messages=True,
    storage=storage,
    memory=memory,
    enable_agentic_memory=True,
)

@router.post('/run')
async def run(body: Body):
    response = agent.run(body.message)
    return {"response:", response.content}