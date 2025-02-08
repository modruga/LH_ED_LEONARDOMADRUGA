# Indicium Tech Code Challenge

Esse desafio foi preparado para ser desenvolvido em um ambiente linux usando Python.

## Como executar

# Passo 1: preparando as ferramentas

Crie seu virtual environment seguindo as instrucoes especificas de sua versao python na pasta raiz do projeto e ative o docker compose com 
```docker compose up -d``` ou ```docker-compose up -d```.

Instale o meltano usando ```pip install meltano``` com seu virtual environment ativo.

Entre no diretorio do projeto meltano em ```./indicium-project```.

Execute ```meltano invoke airflow scheduler```.

# Passo 2: executando os pipelines
## step 1:

Execute ```meltano run extract-data-to-output```. Isso ira adicionar todas as entidades providas pelo banco de dados northwind ao filesystem solicitado pelo desafio, que e descrito por ```./output/postgres/nome-da-table/data-de-extracao/data.csv```. O arquivo csv tambem sera extraido nesse comando, e estara em ```./output/csv/data-de-extracao/data.csv```.

Essa etapa copia todas as tables do banco de dados e todo o conteudo do arquivo *.csv presentes no repositorio do desafio.

## step 2:

Execute ```export CURRENT_DATE=$(date +'%Y-%m-%d')```. Isso ira adicionar a data atual a uma variavel de ambiente exposta para que seja usada na indexacao dos arquivos no filesystem criado pelo step 1.

Execute ```meltano run step-2-exec-write-db```. Isso ira copiar todos os dados do diretorio output do dia atual de cada uma das entidades (incluindo a exportacao do arquivo *.csv separado do banco de dados da northwind), preenchendo em modo "overwrite" o banco de dados paralelo (target) para analise.

# Conclusoes

## Notas do autor
Configurar as ferramentas pela primeira vez foi um desafio consideravel, consumindo uma quantia relevante do tempo de desenvolvimento. Compreender a modularidade do meltano, sua relacao com as etapas do pipeline (extract, load, orchestrate) e o processo de automacao usando jobs com suas respectivas tasks foi importante para o meu desenvolvimento pessoal no ingresso do mundo de engenharia de dados. O conjunto, como um todo, para o intervalo de entrega, provou-se ter uma quantia grande de conteudos e acredito que me sai bem dentro do que consegui fazer. O desafio nao foi completamente vencido, como podem notar pela ausencia da capacidade de executar os comandos usando datas anteriores como argumento, porem fiquei orgulhoso com meu rendimento paralelo a universidade e monitoria em uma semana bem caotica. Outro ponto que posso trazer seria que varios processos poderiam ser automatizados atraves de bash files (processo de instalacao e exportacao da variavel que expoe o dia atual), assim como o uso de DAG customizada no airflow (qual tentei implementar sem sucesso, onde uso BashCommand seguido de um DAG trigger). Agradeco a oportunidade e a proposta de desafio, pois independente da minha colocacao como aprovado ou nao, foi um otimo projeto de aprendizado e acrescentou muito ao meu dicionario de programador.
