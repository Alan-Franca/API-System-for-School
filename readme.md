# API de Gestão Escolar com FastAPI

Uma API RESTful completa desenvolvida com FastAPI para gerenciar alunos, cursos e matrículas em uma instituição de ensino. O projeto utiliza SQLAlchemy para o mapeamento objeto-relacional com um banco de dados SQLite e Pydantic para validação de dados.

A aplicação também inclui uma interface frontend simples em HTML e JavaScript para interagir com os endpoints, e está configurada para ser executada facilmente com Docker.

## ✨ Funcionalidades

-   **Gestão de Alunos**:
    -   Criar, ler, atualizar e deletar (CRUD) alunos.
    -   Buscar alunos por ID, nome (busca parcial) ou email.
-   **Gestão de Cursos**:
    -   Criar, ler e atualizar cursos.
    -   Buscar cursos por código.
-   **Gestão de Matrículas**:
    -   Realizar a matrícula de um aluno em um curso.
    -   Consultar todos os cursos em que um aluno está matriculado (por nome do aluno).
    -   Consultar todos os alunos matriculados em um curso (por código do curso).
-   **Interface Web**:
    -   Um painel de controle (`index.html`) para testar todas as funcionalidades da API diretamente do navegador.
-   **Containerização**:
    -   Configuração completa com `Dockerfile` e `docker-compose.yml` para fácil execução.
-   **CI/CD**:
    -   Workflow de Integração Contínua com GitHub Actions para construir a imagem Docker a cada push na branch `main`.

## 🛠️ Tecnologias Utilizadas

-   **Backend**: Python 3.10+
-   **Framework**: FastAPI
-   **Banco de Dados**: SQLite com SQLAlchemy
-   **Validação de Dados**: Pydantic
-   **Servidor ASGI**: Uvicorn
-   **Containerização**: Docker e Docker Compose

## 📋 Pré-requisitos

-   [Python 3.10 ou superior](https://www.python.org/downloads/)
-   [Docker](https://www.docker.com/get-started/) (para o método de execução com container)

## 🚀 Como Começar

Você pode executar o projeto de duas maneiras: localmente com um ambiente virtual Python ou usando Docker.

### 1. Executando com Docker (Recomendado)

Este é o método mais simples e rápido.

1.  **Clone o repositório:**
    ```bash
    git clone [https://URL-DO-SEU-REPOSITORIO.git](https://URL-DO-SEU-REPOSITORIO.git)
    cd api-system-for-school
    ```

2.  **Suba o container com Docker Compose:**
    ```bash
    docker-compose up --build
    ```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

### 2. Executando Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://URL-DO-SEU-REPOSITORIO.git](https://URL-DO-SEU-REPOSITORIO.git)
    cd api-system-for-school
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação com Uvicorn:**
    ```bash
    uvicorn app:app --reload
    ```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

## 📄 Documentação e Testes

Com a aplicação em execução, você pode acessar a documentação interativa gerada automaticamente pelo FastAPI (via Swagger UI) para visualizar e testar todos os endpoints:

-   **Documentação Interativa**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **Painel de Controle Front-end**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📡 Endpoints da API

### Alunos (`/alunos`)

| Método   | Endpoint                  | Descrição                                 |
| :------- | :------------------------ | :---------------------------------------- |
| `GET`    | `/alunos`                 | Lista todos os alunos.                    |
| `GET`    | `/alunos/{aluno_id}`      | Busca um aluno pelo seu ID.               |
| `GET`    | `/alunos/nome/{nome_aluno}` | Busca um ou mais alunos por nome.         |
| `POST`   | `/alunos`                 | Cria um novo aluno.                       |
| `PUT`    | `/alunos/{aluno_id}`      | Atualiza um aluno existente.              |
| `DELETE` | `/alunos/{aluno_id}`      | Deleta um aluno.                          |

### Cursos (`/cursos`)

| Método | Endpoint                 | Descrição                           |
| :----- | :----------------------- | :---------------------------------- |
| `GET`  | `/cursos`                | Lista todos os cursos.              |
| `GET`  | `/cursos/{codigo_curso}` | Busca um curso pelo seu código.     |
| `POST` | `/cursos`                | Cria um novo curso.                 |
| `PUT`  | `/cursos/{codigo_curso}` | Atualiza um curso pelo seu código.  |

### Matrículas (`/matriculas`)

| Método | Endpoint                         | Descrição                                                 |
| :----- | :------------------------------- | :-------------------------------------------------------- |
| `POST` | `/matriculas`                    | Realiza uma nova matrícula.                               |
| `GET`  | `/matriculas/aluno/{nome_aluno}`   | Lista os cursos de um aluno pelo nome dele.               |
| `GET`  | `/matriculas/curso/{codigo_curso}` | Lista os alunos de um curso pelo código do curso.       |
