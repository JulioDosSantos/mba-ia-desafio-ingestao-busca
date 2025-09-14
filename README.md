# Desafios Técnicos - MBA IA - Ingestão e Busca Semântica com LangChain e Postgres

## Objetivo

### 1. Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
### 2. Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências do projeto, siga os passos abaixo:

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   **Opção A - A partir do `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

   **Opção B - Instalação direta dos pacotes principais:**
   ```bash
   pip install langchain langchain-openai langchain-google-genai langchain-community langchain-text-splitters langchain-postgres psycopg[binary] python-dotenv beautifulsoup4 pypdf && pip freeze > requirements.txt
   ```
   Este comando também instalará todas as dependências automaticamente e gerará o arquivo `requirements.txt`.

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais obtidas conforme instruções abaixo

4. **Subir o banco de dados:**

    ```bash
    docker compose up -d
    ```

5. **Executar ingestão do PDF:**

    ```bash
    python src/ingest.py
    ```

6. **Rodar o chat:**

    ```bash
    python src/chat.py
    ```  

## Requisitos para Execução dos Códigos

Para executar os códigos fornecidos no curso, é necessário criar chaves de API (API Keys) para os serviços da OpenAI e do Google Gemini. Abaixo, fornecemos instruções detalhadas para a criação dessas chaves.

### Criando uma API Key na OpenAI

1. **Acesse o site da OpenAI:**

   [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

2. **Faça login ou crie uma conta:**

   - Se já possuir uma conta, clique em "Log in" e insira suas credenciais.
   - Caso contrário, clique em "Sign up" para criar uma nova conta.

3. **Navegue até a seção de API Keys:**

   - Após o login, clique em "API Keys" no menu lateral esquerdo.

4. **Crie uma nova API Key:**

   - Clique no botão "Create new secret key".
   - Dê um nome para a chave que a identifique facilmente.
   - Clique em "Create secret key".

5. **Copie e armazene sua API Key:**

   - A chave será exibida uma única vez. Copie-a e cole no arquivo `.env` na variável `OPENAI_API_KEY`.

Para mais detalhes, consulte o tutorial completo: [Como Gerar uma API Key na OpenAI?](https://hub.asimov.academy/tutorial/como-gerar-uma-api-key-na-openai/)

### Criando uma API Key no Google Gemini

1. **Acesse o Google AI Studio:**

   [https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR)

2. **Faça login com sua conta Google:**

   - Utilize sua conta Google para acessar o AI Studio.

3. **Navegue até a seção de chaves de API:**

   - No painel de controle, clique em "API Keys" ou "Chaves de API".

4. **Crie uma nova API Key:**

   - Clique em "Create API Key" ou "Criar chave de API".
   - Dê um nome para a chave que a identifique facilmente.
   - A chave será gerada e exibida na tela.

5. **Copie e armazene sua API Key:**

   - Copie a chave gerada e cole no arquivo `.env` na variável `GOOGLE_API_KEY`.

Para mais informações, consulte a documentação oficial: [Como usar chaves da API Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR)

**Nota:** Certifique-se de não compartilhar suas chaves de API publicamente e de armazená-las em locais seguros, pois elas concedem acesso aos serviços correspondentes.