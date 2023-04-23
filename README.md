# Flask API

Esta página apresenta uma simples API Flask. O principal conceito desta prática é o de *Object Relational Mapper* (ORM). ORM provê maneiras de mapear tabelas em classes, já que cada registro da tabela será um objeto da classe definida. Isso permite que os desenvolvedores usem uma maneira mais natural de interagir com o banco sem a necessidade de escrever SQL diretamente. O SQLAlchemy é uma biblioteca que provê uma interface para se trabalhar com ORM.

- Importe esse probjeto para sua conta e abra-o no Codespace.

- Para esta prática, iremos precisar da imagem do Postgres. No terminal, digite:

   1. `docker pull postgres`

- Agora, iremos construir o conteiner da imagem criada:

   2. `docker run --name postgresql -e "POSTGRES_PASSWORD=admin123" -p 5432:5432 -d postgres`

- Criamos um conteiner chamado *postgresql*, configuramos a porta local 5432 na máquina local, que será mapeada para a porta 5432 do conteiner, além de configurar a senha *admin123* para o usuário padrão *postgres*. Este conteiner estará em execução.

- Se você precisa relembrar alguns comandos de gerenciamento de conteiner, veja as práticas passadas, pois na descrição dessas práticas há detalhes sobre os principais comandos para o Docker. Veja se o conteiner criado está em execução.

- A partir desse momento, o banco pode ser acessado. Vamos fazer um pequeno teste de acesso ao banco (conteiner postgresql). Na linha de comando, digite o comando abaixo, mas atenção ao *id-do-container-postgres*, que deverá ser o ID do respectivo conteiner.

   3. `docker exec -it id-do-container-postgres bash`

- O acesso ao container foi concedido, sito é, você fez um acesso ao conteiner com o postgres. Agora, acesse o gerenciador com o usuário 'postgres':

   4. `psql -U postgres`

- O acesso ao gerenciador de bancos foi concedido, por meio do usuário *postgres*. Os seguintes comandos serão úteis no próximo passo.
   - **\l**: lista todos os bancos
   - **\c database-name**: usa o banco 'database-name'
   - **\dt**: lista todas as tabelas
   - **quit** sai do gerenciador do banco

- O arquivo *help.txt* possui algumas instruções SQL que devemos usar para replicar a prática. Então, faça:

   1. Crie o banco 'productsapi'
   2. Altere o gerenciador para o banco criado
   3. Crie a tabela 'products'
   4. Insira um registro na tabela criada
   5. Faça um SELECT "*" e confira o resgistro criado

## Execução da aplicação

O terminal atual estará ocupado com o gerenciador do banco. Abra um novo terminal.

Basta executar nossa aplicação Flask, que já está configurada para acessar o banco. Explore bem o arquivo *app.py* para entender a conexão com o banco. Lembre do arquivo .env criado com as variáveis de acesso.

- Execute o arquivo *app.py*:

      1. `python3 app.py`

- Acesse o endereço localhost na porta 5000 (localhost:5000) para visualizar a aplicação. Atenção às rotas.

- Use o Postman para criar as requisições necessárias para que você perceba todas as funcionalidades da API. Lembre-se de mudar a visibilidade da API para 'público', assim ela será visível fora do codespace.

   1. Faça uma requisição para cada rota, que não seja via GET. Lembre-se que algumas requisições precisam de dados enviados para a API, pelo 'body' da requisição. Esse dado deverá ser um objeto JSON. Sempre confira o resultado da sua requisição realizando um GET via browser, ou até mesmo você poderá conferir no primeiro terminal que está alocado para máquina com o postgres.
   2. Perceba nas rotas que não há uma única linha SQL. O que há é o SQLAlchemy realizando todo o mapeamento Classe :arrows_counterclockwise: Tabela. 
   3. Existem boas discussões sobre o uso de ferramentas ORM. Pesquise mais e conheça bem os dois mundos: 'ORM vs escrever SQL' no ambiente de um Desenvolvedor.

- Apresente para o professor o resultado das suas requisições e, após, lembre-se de desligar sua máquina alocada no codespace.

- Pratique e estude bastante. Somente praticando, repetindo e pesquisando, para fixarmos essas tecnologias que usamos no dia-a-dia. :rocket: