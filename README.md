# Sistema de Cadastro e Login

Este projeto é um sistema simples de cadastro e login utilizando Flask e SQLite. O sistema permite que os usuários se cadastrem e façam login em uma aplicação web.

## Funcionalidades

- **Cadastro de Usuário**: O usuário pode criar uma conta fornecendo seu nome de usuário, e-mail, senha e confirmação de senha. As senhas devem coincidir e ter no mínimo 3 caracteres.
- **Login de Usuário**: Após o cadastro, o usuário pode fazer login utilizando seu nome de usuário e senha.
- **Validação de Campos**: O sistema valida se todos os campos foram preenchidos corretamente e exibe mensagens de erro caso algo esteja incorreto.
- **Banco de Dados**: Utiliza SQLite para armazenar informações de cadastro de usuários.

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém a lógica da aplicação Flask.
- **templates/**: Diretório que contém os arquivos HTML para as páginas de login e cadastro.
- **Sistema_cadastros.db**: Banco de dados SQLite onde as informações dos usuários são armazenadas.

## Requisitos

- Python 3.x
- Flask
- SQLite

## Instalação

1. **Instalar dependências**: Para rodar o projeto, você precisa ter o Flask instalado. Caso não tenha o Flask instalado, use o seguinte comando:

   ```bash
   pip install flask
   ```

2. **Configuração do Banco de Dados**: O banco de dados será criado automaticamente na primeira execução do sistema.

3. **Executar a Aplicação**: Execute o arquivo `app.py` para iniciar o servidor.

   ```bash
   python app.py
   ```

4. **Acessar a aplicação**: Abra um navegador e vá até o endereço `http://127.0.0.1:5000/`. Você verá a página de login, onde pode se cadastrar ou fazer login.

## Funcionamento do Código

### Classe `BackEnd`

A classe `BackEnd` contém os seguintes métodos principais:

- **conecta_db()**: Estabelece a conexão com o banco de dados SQLite.
- **desconecta_db()**: Fecha a conexão com o banco de dados.
- **cria_tabela()**: Cria a tabela de usuários no banco de dados, se ainda não existir.
- **cadastrar_usuario()**: Realiza o cadastro de um novo usuário, realizando validações como preenchimento dos campos e verificação de senha.
- **verifica_login()**: Verifica se o nome de usuário e a senha informados existem no banco de dados.

### Roteamento Flask

- **`/login`**: Página de login, onde o usuário informa seu nome de usuário e senha. Se o login for bem-sucedido, é redirecionado para a página de login novamente.
- **`/cadastro`**: Página de cadastro, onde o usuário fornece nome de usuário, e-mail, senha e confirmação de senha. Caso o cadastro seja bem-sucedido, é redirecionado para a página de login.

### Flash Messages

- São usadas mensagens de feedback para informar o usuário sobre o sucesso ou falha em ações como login e cadastro.

## Como Usar

1. Acesse a página de login (`/login`) para fazer login ou se cadastrar.
2. Se você não tiver uma conta, vá para a página de cadastro (`/cadastro`), insira suas informações e confirme o cadastro.
3. Após o cadastro, você será redirecionado para a página de login, onde poderá fazer login com suas credenciais.

## Exemplo de Fluxo

1. **Acessar a página de login**:
    - Na primeira vez, você verá uma opção de se cadastrar.
   
2. **Cadastrar-se**:
    - Preencha o nome de usuário, e-mail, senha e confirmação de senha. Se os dados forem válidos, você será redirecionado para o login.
   
3. **Fazer login**:
    - Após o cadastro, entre com suas credenciais de nome de usuário e senha para acessar o sistema.

## Tecnologias Usadas

- **Flask**: Framework web em Python para criar a aplicação.
- **SQLite**: Banco de dados relacional utilizado para armazenar as informações de cadastro.
- **HTML**: Estrutura das páginas de login e cadastro.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


---

**Nota**: Este sistema é um exemplo simples e pode ser aprimorado com funcionalidades adicionais como validação de e-mail, criptografia de senha e melhorias de segurança.
