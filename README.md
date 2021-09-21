# Sistema de Gerenciamento de Dados em Django
## Desafio proposto pela empresa IGS usando a tecnologia Django, Django REST API, CRUD e Docker!
<p style='text-align: center;margin-top: 0px;'>
    <img src='./static/img/igs_logo.png' style='width: 40%;margin-top: 0px;'>
</p>

- ## 🔧 Instalação com docker(Recomendado)
### 1. Instale o Docker Desktop (for windows or for linux) que vem com o docker e o docker-compose.
### 2. Inicialize o docker
### 3. Abra o cmd como administrador na pasta raiz do projeto
### 4. Execute o comando `docker-compose up`
### 5. Aguarde a criação da imagem
### 6. Pronto! Agora é só abrir a url `http://localhost:8000/` e usar o app Django
&nbsp;

- ## 📌 Documentação da API
## Listar funcionários
<span style='background-color: #61AFFE;padding:3px 10px;margin-right: 10px;border-radius: 5px;font-weight: bold;'>GET</span> http://localhost:8080/<strong>employee/</strong>

### Headers
```
Content-Type: application/json
```

### No request body;
<br>

### Status Code: <span style='font-weight: bold;color: #49CC90'>200 OK</span>

### Response: 
```json
{
    "status" : 1,
    "message" : "Successfully generated employee list!",
    "data" : [
        {
            "id": 6,
            "name": "Tatiane Laura",
            "email": "tatiane.laura@gmail.com",
            "department": "Developer"
        },
        {
            "id": 3,
            "name": "Felipe Morais De Almeida",
            "email": "felipe.morais@gmail.com",
            "department": "Tester"
        }
    ]
}
```
<br>

## Pegar funcionário pelo id
<span style='background-color: #61AFFE;padding:3px 10px;margin-right: 10px;border-radius: 5px;font-weight: bold;'>GET</span> http://localhost:8080/<strong>employee/<span style='color: #61AFFE'>{id}</span>/</strong>

### Headers
```
Content-Type: application/json
```

### No request body;
<br>

### Status Code: <span style='font-weight: bold;color: #49CC90'>200 OK</span>

### Response(example: id = 6): 
```json
{
    "status" : 1,
    "message" : "Employee has been found!",
    "data" : {
            "id": 6,
            "name": "Tatiane Laura",
            "email": "tatiane.laura@gmail.com",
            "department": "Developer"
    }
}
```
<br>

## Adicionar novo funcionário
<span style='background-color: #49CC90;padding:3px 10px;margin-right: 10px;border-radius: 5px;font-weight: bold;'>POST</span> http://localhost:8080/<strong>employee/<span style='color: #49CC90'>{id}</span>/</strong>

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
    "name": "Joao Pedro Andrade",
    "email": "joaopedro@gmail.com",
    "department": "Java Developer"
}
```
<br>

### Status Code: <span style='font-weight: bold;color: #49CC90'>200 OK</span>

### Response:
```json
{
  "status": 1,
  "message": "Employee has been added successfully!"
}
```
<br>

## Alterar funcionário pelo id
<span style='background-color: #FCA130;padding:3px 10px;margin-right: 10px;border-radius: 5px;font-weight: bold;'>PUT</span> http://localhost:8080/<strong>employee/<span style='color: #FCA130'>{id}</span>/</strong>

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
    "name": "Joao Pedro Andrade",
    "email": "joaopedro@gmail.com",
    "department": "Java Developer"
}
```
<br>

### Status Code: <span style='font-weight: bold;color: #49CC90'>200 OK</span>

### Response(example: id = 6): 
```json
{
    "status": 1,
    "message": "Employee has been updated successfully!",
    "data": {
        "id": 6,
        "name": "Joao Pedro Andrade",
        "email": "joaopedro@gmail.com",
        "department": "Java Developer"
    }
}
```
<br>

## Deletar funcionário pelo id
<span style='background-color: #F93E3E;padding:3px 10px;margin-right: 10px;border-radius: 5px;font-weight: bold;'>DELETE</span> http://localhost:8080/<strong>employee/<span style='color: #F93E3E'>{id}</span>/</strong>

### Headers
```
Content-Type: application/json
```

### No request body;
<br>

### Status Code: <span style='font-weight: bold;color: #49CC90'>200 OK</span>

### Response:
```json
{
    "status": 1,
    "message": "Employee has been deleted successfully!"
}
```
