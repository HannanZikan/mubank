TODO:

    -[ ] implementar regras de negócio
        [x] Toda criação de transaction tipo 1 TEM que incrementar o campo wallet.ammount onde receiving_wallet_id = wallet.user id e decrementar o campo wallet.ammount onde transfer_wallet_id = wallet.user_id
        [x] Toda criação de transaction tipo 2 TEM que incrementar o campo wallet.ammount onde receiving_wallet_id = wallet.user_id
        [x] Toda criação de transaction tipo 3 TEM que decrementar o campo wallet.ammount onde transfer_wallet_id = wallet.user_id

    -[ ] implementar endpoints para criação de usuário

    -[ ] implementar autenticação com JWT

    -[ ] implementar banco de dados postgreSQL

    -[ ] implementar dockerização

    -[ ] implementar testes automatizados

    -[ ] implementar linter

    -[ ] fazer o redme com as instruções para rodar o projeto
