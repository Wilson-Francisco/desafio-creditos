# 🚀 Desafio Técnico – Sistema de Consulta de Créditos Constituídos

Este repositório contém a entrega final de um desafio técnico de nível Pleno/Sênior, consistindo em uma solução completa de ponta a ponta que integra um Back-end robusto em **Python (FastAPI)**, uma infraestrutura de dados e mensageria via **Docker Desktop (PostgreSQL e RabbitMQ)**, e um Front-end moderno e performático em **Angular (Zoneless)**.

Toda a esteira de integração foi blindada por **Testes Unitários (Pytest)** e protegida por um pipeline automatizado de **CI/CD (GitHub Actions)** que valida a qualidade de estilo (Ruff) e checagem de tipos estáticos (Mypy) a cada integração.

---

## 🛠️ Tecnologias e Arquitetura do Ecossistema

### Back-end (Python & FastAPI)
- **Python 3.13+** com tipagem estática rigorosa monitorada pelo `mypy`.
- **FastAPI** para exposição de endpoints assíncronos de alta performance.
- **SQLAlchemy 2.0** utilizando o padrão *Declarative Mapping* e injeção de dependências para gerenciamento de sessões do banco de dados.
- **Pydantic v2** para validação de esquemas de entrada/saída e conversão nativa de dados para os contratos *camelCase* solicitados.

### Front-end (Angular)
- **Angular 22+** com arquitetura baseada em componentes *Standalone*.
- Mecanismo de renderização assíncrona estável **Zoneless Change Detection**, eliminando a necessidade física do legado `zone.js` e melhorando a performance de detecção de eventos no navegador.
- Interface 100% responsiva com suporte mobile, tratamento visual de estados (`carregando`, `erroMensagem`) e barramentos amigáveis para erro 404.

### Infraestrutura & DevOps (Docker Desktop)
- **PostgreSQL 15** populado automaticamente na primeira inicialização através de scripts DDL/DML isolados em volume físico.
- **RabbitMQ 3 (Management)** atuando como broker de mensageria assíncrona.
- *Nota de DX (Developer Experience):* As portas externas padrão do Windows foram redirecionadas (Postgres na `5439` e RabbitMQ na `5679` e `15679`) para evitar conflitos com serviços locais residuais do sistema operacional.

---

## 📂 Estrutura do Projeto

```text
desafio-creditos/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de CI/CD (GitHub Actions)
├── .vscode/
│   └── settings.json          # Configurações de DX e auto-format do VS Code
├── backend/
│   ├── app/
│   │   ├── api/               # Endpoints e Controladores HTTP
│   │   ├── core/              # Configurações ambientais e Mensageria
│   │   ├── db/                # Sessão e Conexão do SQLAlchemy
│   │   ├── models/            # Modelos de Dados do Banco
│   │   ├── repositories/      # Padrão Repository (Acesso a dados)
│   │   ├── schemas/           # DTOs e Schemas do Pydantic
│   │   └── services/          # Camada Service (Regras de negócio)
│   ├── tests/                 # Suíte de Testes Unitários (Pytest)
│   ├── pyproject.toml         # Configurações do Ruff e Mypy
│   └── requirements.txt       # Dependências de Produção e Testes
└── frontend/
    ├── src/
    │   ├── app/
    │   │   ├── services/      # Serviços de Consumo HTTP da API
    │   │   ├── app.html       # Template visual da busca e tabelas
    │   │   ├── app.css        # Estilos encapsulados do layout
    │   │   └── app.ts         # Lógica e controle de estado do componente
    │   └── main.ts            # Ponto de entrada do bootstrapping do Angular
    └── angular.json           # Configurações globais do projeto Angular
```

---

## 🧪 Suíte de Testes e Qualidade de Código

O projeto foi submetido a rigorosos validadores estáticos locais e remotos (CI/CD) para garantir conformidade máxima com a PEP 8:

1. **Análise Estática e Linter (Ruff):** Formatação automatizada e checagem de erros de sintaxe ou imports não utilizados executados através do comando:
   ```bash
   ruff check .
   ```
2. **Checagem de Tipos Estáticos (Mypy):** Validação estrita das assinaturas de métodos e retornos de rotas executada através do comando:
   ```bash
   mypy .
   ```
3. **Testes Unitários (Pytest + Mocks):** Testes focados estritamente no isolamento da camada de serviços (`CreditoService`). Toda a comunicação de infraestrutura (Banco de Dados e Mensageria) foi substituída por dublês de testes reais através de `unittest.mock.MagicMock`, garantindo que a suíte execute sem conexões físicas de rede. Execute localmente com:
   ```bash
   pytest
   ```

---

## 🔄 Funcionamento do Pipeline de CI/CD

O arquivo de configuração do **GitHub Actions** (`.github/workflows/ci.yml`) intercepta automaticamente qualquer evento de **Push** ou **Pull Request** direcionado à branch principal `main`. O pipeline monta um ambiente isolado em nuvem e executa obrigatoriamente as seguintes fases:
- **Fase 1:** Setup do Python 3.13 e Cache de dependências.
- **Fase 2:** Verificação estrita de estilo e formatação via **Ruff** (O build quebra se houver violação da PEP 8).
- **Fase 3:** Verificação estrita de tipos via **Mypy**.
- **Fase 4:** Execução de testes automatizados via **Pytest** (O merge é bloqueado se algum teste unitário falhar).

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de possuir instalado em sua máquina local:
- **Docker Desktop** (Ativo e rodando)
- **Python 3.13+**
- **Node.js** (Versão LTS atual)

### 1. Inicializar a Infraestrutura (Docker)
Na raiz do projeto (`desafio-creditos`), execute o comando abaixo para subir o banco de dados e a mensageria em segundo plano:
```bash
docker compose up -d
```
*A tabela `credito` será criada e populada automaticamente com os 3 registros de testes fornecidos no escopo do edital.*

### 2. Inicializar o Back-end Python (FastAPI)
Navegue até a pasta `backend`, ative o seu ambiente virtual (`.venv`) e instale as dependências:
```bash
cd backend
python -m venv .venv
# Ative o ambiente de acordo com o seu SO (ex: Windows PowerShell):
.venv\Scripts\Activate.ps1

# Instale os pacotes
pip install -r requirements.txt

# Inicie o servidor ASGI localmente na porta 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
*A documentação Swagger interativa poderá ser acessada em: **http://localhost:8000/docs***

### 3. Inicializar o Front-end (Angular)
Abra um novo terminal na pasta `frontend`, injete o caminho do Node se necessário e suba o servidor de desenvolvimento:
```bash
cd frontend
# No Windows, se o comando npx não for reconhecido de imediato, adicione o PATH:
\$env:Path += ";C:\Program Files\nodejs"

# Inicie o servidor com o host numérico estável para evitar bloqueios de rede do Windows
npx ng serve --host 127.0.0.1
```
*A aplicação visual de consulta estará de pé e disponível no endereço: **http://127.0.0***

---

## 📩 Desafio Extra Implementado: Auditoria com Mensageria Assíncrona

Toda vez que uma consulta é realizada com sucesso através dos endpoints da API, a rota faz uso do recurso nativo **`BackgroundTasks`** do FastAPI para despachar uma notificação assíncrona.
- A função `enviar_evento_auditoria` abre uma conexão robusta com o **RabbitMQ** através da biblioteca **`aio-pika`** e publica um payload contendo o tipo de busca realizada, o termo pesquisado e o carimbo de data/hora na fila `auditoria_creditos`.
- Como o disparo ocorre em background, o ciclo de vida da requisição HTTP não é bloqueado, garantindo uma resposta em milissegundos para o usuário no front-end enquanto a auditoria roda de forma desacoplada em segundo plano.
- O painel visual administrativo do RabbitMQ para acompanhar a fila pode ser acessado localmente pelo link: **http://127.0.0** (Usuário: `guest` / Senha: `guest`).
