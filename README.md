# STOCK360

Bem-vindo ao Sistema de Gestão de Estoque (STOCK360), um projeto desenvolvido em Django e Bootstrap 5 para facilitar o gerenciamento de estoque. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install django
```

## Rodar o projeto

Após instalar as dependências, aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

Agora o projeto jã pode ser inicializado com o comando:
```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000/brands/list/](http://localhost:8000/brands/list/)
