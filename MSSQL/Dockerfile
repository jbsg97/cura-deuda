FROM mcr.microsoft.com/mssql/server:2019-latest
COPY . .

HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=10 \
    CMD ./opt/mssql-tools/bin/sqlcmd -S -U sa -P Password123* -i setup.sql || exit 1