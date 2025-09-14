import os
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

MODEL_LLM="gpt-5-nano"

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS E RESPOSTAS:
Pergunta: Qual o faturamento da Empresa SuperTechIABrazil?
Resposta: O faturamento foi de 10 milhões de reais.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt():

  question = input("Digite sua pergunta: ")
  
  embeddings = OpenAIEmbeddings(
      model=os.getenv("OPENAI_EMBEDDING_MODEL")
  )

  store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
    connection=os.getenv("DATABASE_URL"),
    use_jsonb=True,
  )

  results = store.similarity_search_with_score(question, k=10)

  user = ("user", PROMPT_TEMPLATE)

  chat_prompt = ChatPromptTemplate([ user ])

  contexto = "\n".join([doc.page_content for doc, _ in results])

  messages = chat_prompt.format_messages(contexto=contexto, pergunta=question)

  for msg in messages:
    print(f"{msg.type}: {msg.content}")

  model = ChatOpenAI(model=MODEL_LLM, temperature=0.5)
  result = model.invoke(messages)

  return result.content;


if __name__ == "__main__":
  search_prompt()