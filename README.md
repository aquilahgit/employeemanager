# Django Coding Test

## Para iniciar o projeto
```sh
git clone git@github.com:aquilahgit/employeemanager.git
cd employeemanager
docker-compose up
```

## Para acessar o projeto
[Link para o admin do projeto!](http://localhost:8000/admin/)

Para logar use login: `admin` e passoword: `q1w2e3r4`.

## Listar usuários
```sh
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

## Adicionar usuário
```sh
curl -d "department=Mobile&name=Aquila2&email=aquila@luizalabs.com.br" -X POST http://localhost:8000/employee/
```

## Remover usuário
```sh
curl -X DELETE http://localhost:8000/employee/{:id}
```

#### Observações
> O arquivo `db.sqlite3` foi versionado propositalmente.
> Não foi usado nenhum framework para geração da api.
