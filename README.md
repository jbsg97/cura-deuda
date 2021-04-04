# Cura Deuda Project
REST API para cura deuda, obtiene datos de SEPOMEX para despues mostrarlo en una api en formato json

Para iniciar proyecto clonan este repositorio en su maquina local, para hacerlo funcionar se requiere Docker y Docker-Compose, una vez obtenido el proyecto ingresan en la carpeta raiz  e ingresan el siguiente comando:
```console
docker-compose up
```

Ya que se termine de construir, alimentamos la base de datos, el "seed script" se encuentra dentro de la carpeta MSSQL, la base de datos fue creada en mssql, las credenciales son las siguientes:
- username : sa
- password : Password123*

Una vez que la base de datos este alimentada, accedemos a la api de la siguiente manera:
(http://localhost:8000)

Esta sera nuestro url, ahora para los endpoints:
Nota: Para crear nuevos registro se debe otener token, ya que esta validado usando flask-jwt-extended.
___

Assentamientos

:arrow_forward: **Endpoint** : `http://localhost:8000/api/settlements`

:arrow_forward: **Metodo**: `GET y POST`

:arrow_forward: **Parametros**:   `postal_code, settlement, municipality, state`

:arrow_forward: **Función**: `Crear y Mostrar todos los estados, puede filtrar por codigo postal, nombre del asentamiento, municipio y estado usando los query params.`
___

___

Estados

:arrow_forward: **Endpoint** : `http://localhost:8000/api/states`

:arrow_forward: **Metodo**: `GET y POST`

:arrow_forward: **Parametros**:   `state`

:arrow_forward: **Función**: `Crear y Mostrar todos los estados, puede buscar un estado en especifico usando el query param.`
___

___

Municipios

:arrow_forward: **Endpoint** : `http://localhost:8000/api/municipality`

:arrow_forward: **Metodo**: `GET y POST`

:arrow_forward: **Parametros**:   `municipality`

:arrow_forward: **Función**: `Crear y Mostrar todos los municipios, puede buscar un municipio en especifico usando el query param.`
___

___

Tipos de asentamientos

:arrow_forward: **Endpoint** : `http://localhost:8000/api/settlements/types`

:arrow_forward: **Metodo**: `GET y POST`

:arrow_forward: **Parametros**:   `settlement_type`

:arrow_forward: **Función**: `Crear y Mostrar todos los tipos de asentamientos, puede buscar un tipo de asentamiento en especifico usando el query param.`
___

___

Usuarios

:arrow_forward: **Endpoint** : `http://localhost:8000/api/users`

:arrow_forward: **Metodo**: `GET y POST`

:arrow_forward: **Función**: `Crear y Mostrar los usuarios registrados ademas de poder crear nuevos usuarios.`
___

___

Autenticación(Obtener token)

:arrow_forward: **Endpoint** : `http://localhost:8000/api/auth`

:arrow_forward: **Metodo**: `POST`

:arrow_forward: **Función**: `Obtener token para poder crear nuevos elementos en los demas endpoints, se pide "username" y "password" dentro del body.`
___
