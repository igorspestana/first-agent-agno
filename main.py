
import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Configura o agente com a chave de API
agent = Agent(
    model=Gemini(
        id=os.environ['DEFAULT_MODEL'],
        api_key=os.environ['GOOGLE_API_KEYS']
    ),
)

agent.print_response("Qual é o país com a maior densidade populacional atualmente?", stream=True)