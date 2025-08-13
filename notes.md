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