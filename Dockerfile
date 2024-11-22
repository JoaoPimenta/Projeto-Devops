# Usar uma imagem base oficial do Python
FROM python:3.9-slim
# Definir o diretório de trabalho
WORKDIR /app
# Copiar dependências
COPY requirements.txt /app/
# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos da API para o container
COPY . /app/
# Expor a porta 1313
EXPOSE 1313
# Comando para rodar a aplicação
CMD ["python", "app.py"]