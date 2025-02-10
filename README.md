# Indicium Tech Code Challenge

A resolução do desafio foi desenvolvida em um ambiente linux usando ambiente virtual Python e container Docker Postgres.

## Como executar

# Passo 1: preparando as ferramentas

Crie seu virtual environment seguindo as instruções específicas de sua versão python na pasta raiz do projeto e ative o docker compose com 
```docker compose up -d``` ou ```docker-compose up -d``` (depende da versão instalada).

Instale o meltano usando ```pip install meltano``` com seu virtual environment ativo.

Entre no diretório do projeto meltano em ```./indicium-project```.

Execute ```meltano invoke airflow scheduler```.

# Passo 2: executando os pipelines
## step 1:

Execute ```meltano run extract-data-to-output```. Isso irá adicionar todas as entidades providas pelo banco de dados northwind ao filesystem solicitado pelo desafio, que é descrito por ```./output/postgres/nome-da-table/data-de-extracao/data.csv```. O arquivo csv também sera extraído nesse comando, e estará em ```./output/csv/data-de-extracao/data.csv```.

Essa etapa copia todas as tabelas do banco de dados e todo o conteudo do arquivo *.csv presentes no repositório do desafio.

## step 2:

Execute ```export CURRENT_DATE=$(date +'%Y-%m-%d')```. Isso irá adicionar a data atual a uma variável de ambiente exposta para que seja usada na indexação dos arquivos no filesystem criado pelo step 1.

Execute ```meltano run step-2-exec-write-db```. Isso irá copiar todos os dados do diretorio output do dia atual de cada uma das entidades (incluindo a exportação do arquivo *.csv separado do banco de dados da northwind), preenchendo em modo "overwrite" o banco de dados paralelo (target) para análise. Use a interface de sua preferência (como pgAdmin) usando os valores usuário, senha e database presentes no arquivo docker compose.

# Conclusões

## Notas do autor
Configurar as ferramentas pela primeira vez foi um desafio considerável, com uma curva íngrime de aprendizado, consumindo uma quantia relevante do tempo de desenvolvimento. Compreender a modularidade do meltano, sua relação com as etapas do pipeline (extract, load, orchestrate) e o processo de automacao usando jobs com suas respectivas tasks foi importante para o meu desenvolvimento pessoal no ingresso do mundo de engenharia de dados. O conjunto, como um todo, para o intervalo de entrega, provou-se ter uma quantia grande de conteudos e acredito que me sai bem dentro do que consegui fazer (considerando que foi uma semana bem maluca).

O desafio não foi completamente vencido, como podem notar pela ausência da capacidade de executar os comandos usando datas anteriores como argumento e ausência da exigência de dependência para a execução dos pipelines entre si (step 2 não depende do step 1), porém fiquei orgulhoso com meu rendimento paralelo à universidade e monitoria em uma semana bem caótica. Outro ponto que posso trazer seria que vários processos poderiam ser automatizados atraves de bash files (processo de instalação e exportação da variável que expõe o dia atual), assim como o uso de DAG customizada no airflow (qual tentei implementar sem sucesso, onde uso BashCommand seguido de um DAG trigger; e os jobs e suas tasks foram gerados automaticamente pelo meltano no Airflow webserver/scheduler). 

Agradeço a oportunidade e a proposta de desafio, pois independente da minha colocação como aprovado ou não, foi um ótimo projeto de aprendizado e acrescentou muito ao meu dicionário de programador.
