# ETAPA 1: Compilação (O Construtor)
FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y \
    build-essential cmake git libasound2-dev libjack-jackd2-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Comando para compilar o aooserver (ajuste o caminho se o CMakeLists estiver em outro lugar)
RUN mkdir build && cd build && cmake .. && make aooserver

# ETAPA 2: Execução (A Instância Leve)
FROM ubuntu:22.04
WORKDIR /root/
# Copia apenas o binário gerado na etapa anterior
COPY --from=builder /app/build/aooserver /usr/local/bin/aooserver
RUN apt-get update && apt-get install -y libstdc++6 && apt-get clean

EXPOSE 10999/udp
ENTRYPOINT ["aooserver"]
CMD ["-p", "10999"]