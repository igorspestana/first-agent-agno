# O que é o uv?
Claro. uv é uma ferramenta de linha de comando para o ecossistema Python, projetada para ser
  extremamente rápida.

  Ela funciona como um instalador e resolvedor de pacotes Python e também como um gerenciador de 
  ambientes virtuais.

  Aqui estão os pontos-chave sobre o uv:

   1. Velocidade Extrema: É o seu maior diferencial. Foi escrita em Rust e é significativamente mais
      rápida que ferramentas tradicionais como pip para instalar, atualizar e resolver dependências. Isso
      é possível através de um resolvedor avançado e uso inteligente de cache global.

   2. Ferramenta "Tudo em Um": Busca substituir e unificar a funcionalidade de várias ferramentas que um
      desenvolvedor Python usa no dia a dia:
       * pip (para instalar pacotes)
       * venv ou virtualenv (para criar ambientes virtuais)
       * pip-tools (para compilar e travar arquivos requirements.txt)

   3. Compatibilidade: É projetada para ser um substituto direto (drop-in replacement) para pip e venv na
      maioria dos casos de uso comuns. Por exemplo, em vez de pip install <pacote>, você pode usar uv pip 
      install <pacote>.

   4. Desenvolvedor Confiável: É criada pela Astral, a mesma empresa por trás do ruff, um linter
      extremamente popular e rápido para Python. Isso confere grande credibilidade ao projeto.

  Em resumo, uv é uma ferramenta moderna que visa simplificar e acelerar drasticamente o fluxo de
  trabalho de desenvolvimento em Python, oferecendo uma experiência mais rápida e integrada para
  gerenciar dependências e ambientes.

# Instalar o uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# Iniciar o uv
```
uv init
```

# Criar um ambiente virtual
```
uv venv .venv
```

O comando uv venv .venv usa a ferramenta uv para criar um novo ambiente virtual (virtual environment)
  para Python com o nome .venv no diretório atual.

  Em detalhes:
   * uv: É uma ferramenta moderna e muito rápida para instalação de pacotes e gerenciamento de ambientes
     Python.
   * venv: É o comando específico do uv para criar um ambiente virtual.
   * .venv: É o nome do diretório que será criado para armazenar o ambiente virtual. Este é um nome
     convencional e uma boa prática.

  Em resumo, este comando prepara um ambiente limpo e isolado para o seu projeto Python, onde você pode
  instalar bibliotecas sem afetar sua instalação global do Python ou outros projetos.

# Ativar o ambiente virtual
```
source .venv/bin/activate
```

O comando source .venv/bin/activate ativa o ambiente virtual .venv, fazendo com que o Python e os pacotes instalados no ambiente virtual sejam usados em vez dos pacotes instalados globalmente.

# Desativar o ambiente virtual
```
deactivate
```

O comando deactivate desativa o ambiente virtual .venv, fazendo com que o Python e os pacotes instalados globalmente sejam usados em vez dos pacotes instalados no ambiente virtual.

# Instalar pacotes
```
uv add agno fastapi google-genai
```

O comando uv add agno fastapi google-genai usa a ferramenta uv para instalar os pacotes agno, fastapi e google-genai no ambiente virtual ativo.

# Instalar tools
```
uv add googlesearch-python pycountry
```

Para utilizar a tool GoogleSearchTools, é necessário instalar o pacote googlesearch-python e pycountry.

# Uso de memória

## Como funciona a memória no código?

O código utiliza **dois mecanismos de memória complementares**, que trabalham juntos para fornecer contexto e inteligência ao agente:

---

### 1. Memória de Conversa (Histórico)

- **Arquivo:** `tmp/agents.db`
- **Configuração:**
  ```python
  storage = SqliteStorage(table_name="agno_sessions", db_file="tmp/agents.db")

  agent = Agent(
      # ...
      add_history_to_messages=True,
      storage=storage,
      # ...
  )
  ```
- **O que faz:**  
  Armazena o histórico bruto da conversa (mensagens enviadas e respostas do agente) em um banco SQLite.
- **Como funciona:**  
  O parâmetro `add_history_to_messages=True` faz com que o agente inclua automaticamente as mensagens anteriores no prompt a cada nova interação, garantindo contexto de conversa.
- **Analogia:**  
  Funciona como o histórico de um chat, permitindo "rolar para cima" e ver o que foi dito antes.

---

### 2. Memória Agêntica (O "Cérebro" do Agente)

- **Arquivo:** `tmp/memory.db`
- **Configuração:**
  ```python
  memory = Memory(
      db=SqliteMemoryDb(table_name="agno_memory", db_file="tmp/memory.db"),
      model=Gemini(...)  # Usa um modelo para processar a memória
  )

  agent = Agent(
      # ...
      memory=memory,
      enable_agentic_memory=True,  # Ativa a memória agêntica
      # ...
  )
  ```
- **O que faz:**  
  Vai além do histórico: utiliza um modelo de linguagem (Gemini) para extrair fatos e informações importantes da conversa, salvando-os de forma estruturada.
- **Como funciona:**  
  1. Ao receber uma frase como "Meu nome é Pedro, e eu tenho 26 anos.", o agente não apenas armazena a frase.
  2. Com `enable_agentic_memory=True`, o objeto `memory` é ativado e usa o modelo Gemini para entender o significado.
  3. Fatos principais são extraídos, como `nome_do_usuario = Pedro` e `idade_do_usuario = 26`.
  4. Esses fatos são salvos organizadamente no banco `memory.db`.
- **Analogia:**  
  Funciona como o cérebro de uma pessoa: não memoriza cada palavra, mas sim os conceitos e fatos importantes.

---

### Resumo do Fluxo

Quando você executa o código:

1. `agent.print_response("Meu nome é Pedro, e eu tenho 26 anos.")`
   - A frase é salva no histórico (`agents.db`).
   - A memória agêntica extrai e salva os fatos (nome = Pedro, idade = 26) em `memory.db`.
2. `agent.print_response("Qual é o meu nome?")`
   - O agente consulta primeiro a memória agêntica (`memory.db`).
   - Encontra o fato `nome = Pedro` e responde: "Seu nome é Pedro."

---

**Resumo:**  
Você possui um sistema de memória em duas camadas:
- Um histórico de chat para contexto imediato.
- Um banco de dados de fatos para conhecimento permanente e estruturado.