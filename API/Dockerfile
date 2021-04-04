FROM ubuntu:latest


# Instalar conector Mssql ODBC 17
RUN apt-get update \
&& apt-get install curl -y \
&& apt-get install g++ -y \
&& apt-get update && apt-get install -y gnupg \
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
&& curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
&& apt-get update \
&& ACCEPT_EULA=Y apt-get install msodbcsql17 -y \
&& apt-get install unixodbc-dev -y

# Arreglar problema de SSL
RUN chmod +rwx /etc/ssl/openssl.cnf \
    && sed -i 's/TLSv1.2/TLSv1/g' /etc/ssl/openssl.cnf \
    && sed -i 's/SECLEVEL=2/SECLEVEL=1/g' /etc/ssl/openssl.cnf \
    && apt-get install wget \
    && wget https://www.openssl.org/source/latest.tar.gz -O openssl-1.1.1h.tar.gz \
    && tar -zxvf openssl-1.1.1h.tar.gz \
    && apt-get install build-essential -y
RUN cd openssl-1.1.1k \
    && ./config \
    && make \
    && make install \
    && ldconfig

# Copiar proyecto al contenedor e instalar dependencias
WORKDIR /API
COPY . .
RUN apt install python3-pip -y \
    && pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "gunicorn", "--workers=9", "--bind=0.0.0.0:8000", "app:app" ]