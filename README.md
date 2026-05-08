# Engajar para Transformar

## Tema do Projeto

Conexão Escola: campanha de engajamento escolar com uso de indicadores e plataforma digital.

## Sobre o projeto

Este projeto é um site simples feito com Flask para apresentar a proposta Conexão Escola. A aplicação usa:

- Python
- Flask
- Templates HTML em `templates/`
- Arquivos estáticos em `static/`

Atualmente, a aplicação possui uma rota principal (`/`) que renderiza a página inicial.

## Estrutura do projeto

```text
Projeto_site-main/
├── app.py
├── README.md
├── static/
│   ├── script.js
│   ├── style.css
│   └── img/
└── templates/
	└── index.html
```

## Requisitos

- Python 3.9 ou superior
- Python com suporte a `pip`

## Instalação

Clone ou abra a pasta do projeto e, no terminal, execute:

```bash
python3 -m pip install flask
```

Se estiver no Windows:

```bash
python -m pip install flask
```

Esse comando instala o Flask, que é a biblioteca usada para criar e executar o servidor do projeto. Sem ele, o arquivo `app.py` não vai rodar, porque o Python não reconhecerá o import do Flask.

Foi usado `python3 -m pip` em vez de apenas `pip` porque esse formato chama o instalador diretamente pelo Python correto, evitando problemas quando existe mais de uma instalação de Python ou quando o comando `pip` do sistema está apontando para outro programa.

## Como executar

Para iniciar o projeto da forma mais simples, rode:

```bash
python3 app.py
```

Esse comando executa diretamente o arquivo principal da aplicação. Ao fazer isso, o Flask sobe um servidor local e disponibiliza o site no navegador.

Use esse comando quando:

- você quiser apenas abrir o projeto localmente de forma simples
- estiver testando alterações básicas no site
- quiser seguir exatamente a estrutura atual do projeto

Depois, abra no navegador:

```text
http://127.0.0.1:5000
```

## Modo de desenvolvimento com Flask

Outra forma de executar é usando o comando do próprio Flask:

```bash
export FLASK_APP=app.py
python3 -m flask run
```

No Windows:

```bash
set FLASK_APP=app.py
python -m flask run
```

O comando `export FLASK_APP=app.py` informa ao Flask qual arquivo contém a aplicação. Em seguida, `python3 -m flask run` inicia o servidor com base nesse arquivo usando o Flask instalado no mesmo Python do projeto.

Esse modo é útil quando:

- você quer rodar o projeto usando o padrão do Flask
- futuramente quiser usar mais comandos da ferramenta Flask
- quiser separar com mais clareza o arquivo da aplicação e a execução do servidor

Para este projeto escolar, se a ideia for só rodar o site localmente, `python3 app.py` já é suficiente. O `flask run` é uma alternativa, não uma obrigação.

## Objetivo do projeto

O projeto surge da necessidade de promover maior engajamento dos alunos, incentivando o sentimento de pertencimento e responsabilidade.

### Objetivo geral

Desenvolver uma campanha de engajamento escolar baseada em gestão e indicadores, com apoio de uma plataforma digital.

### Objetivos específicos

- Identificar causas da desmotivação
- Criar estratégias de engajamento
- Desenvolver indicadores de acompanhamento
- Aplicar ações no ambiente escolar
- Avaliar resultados

## Resultados esperados

- Redução de atrasos
- Maior uso de uniforme
- Melhoria no comportamento
- Aumento do engajamento
- Participação ativa dos alunos
