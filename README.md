TODO:

    -[x] implementar regras de negócio
        [x] Toda criação de transaction tipo 1 TEM que incrementar o campo wallet.ammount onde receiving_wallet_id = wallet.user id e decrementar o campo wallet.ammount onde transfer_wallet_id = wallet.user_id
        [x] Toda criação de transaction tipo 2 TEM que incrementar o campo wallet.ammount onde receiving_wallet_id = wallet.user_id
        [x] Toda criação de transaction tipo 3 TEM que decrementar o campo wallet.ammount onde transfer_wallet_id = wallet.user_id

    -[x] implementar endpoints para criação de usuário

    -[x] implementar autenticação com JWT
        -[x] implementar login
        -[ ] implementar redefinir senha
        -[x] implementar permissões de usuário
    
    -[ ] implementar população automática do bdd

    -[ ] implementar banco de dados postgreSQL

    -[ ] implementar dockerização

    -[ ] implementar testes automatizados

    -[ ] implementar linter

    -[ ] fazer o redme com as instruções para rodar o projeto
