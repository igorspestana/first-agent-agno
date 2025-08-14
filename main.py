
import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.storage.sqlite import SqliteStorage

storage = SqliteStorage(table_name="agno_sessions", db_file="tmp/agents.db")

# Carrega as variáveis de ambiente
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Configura o agente com a chave de API
agent = Agent(
    session_id="s_124",
    id="u_1",
    model=Gemini(
        id=os.environ['DEFAULT_MODEL'],
        api_key=os.environ['GOOGLE_API_KEYS']
    ),
    add_history_to_messages=True,
    storage=storage,
)

if __name__ == "__main__":
    # agent.print_response("Meu nome é Pedro, e eu tenho 26 anos.")
    agent.print_response("Qual é o meu nome?")
    agent.print_response("Qual é a minha idade?")