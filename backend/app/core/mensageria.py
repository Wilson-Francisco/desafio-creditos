import json
from datetime import datetime

import aio_pika


RABBITMQ_URL = "amqp://guest:guest@localhost:5679/"


async def enviar_evento_auditoria(tipo_consulta: str, termo_buscado: str) -> None:
    """Envia um evento de auditoria de forma assíncrona para a fila do RabbitMQ."""
    try:
        # Estabelece conexão com o broker do Docker Desktop
        connection = await aio_pika.connect_robust(RABBITMQ_URL)

        async with connection:
            channel = await connection.channel()

            # Declara a fila de auditoria (garante que ela exista)
            queue = await channel.declare_queue("auditoria_creditos", durable=True)

            # Monta o payload do log de auditoria
            payload = {
                "evento": "CONSULTA_REALIZADA",
                "tipo_filtro": tipo_consulta,
                "termo_pesquisado": termo_buscado,
                "data_hora": datetime.now().isoformat(),
            }

            # Publica a mensagem na fila
            await channel.default_exchange.publish(
                aio_pika.Message(
                    body=json.dumps(payload).encode(),
                    delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
                ),
                routing_key=queue.name,
            )
    except Exception as e:
        # Em produção, salvaríamos em um log de fallback.
        # No desafio, mantemos um print para depuração simples.
        print(f"Erro ao enviar evento de auditoria para a fila: {str(e)}")
