
import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.reasoning import ReasoningTools

# Carrega as variáveis de ambiente
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Configura o agente com a chave de API
agent = Agent(
    model=Gemini(
        id=os.environ['DEFAULT_MODEL'],
        api_key=os.environ['GOOGLE_API_KEYS']
    ),
    instructions=[
        "Use tabelas para organizar as informações.",
        "Inclua apenas a tabela na resposta. Sem nenhum outro texto."
    ],
    tools=[
        ReasoningTools(add_instructions=True),
        GoogleSearchTools()
    ],
)

agent.print_response(
    "Faça um comparativo entre os países da Europa e os países da América Latina, com base na densidade populacional.", 
    stream=True,
    show_tool_calls=True,
    show_function_calls=True,
    stream_intermediate_steps=True,
)