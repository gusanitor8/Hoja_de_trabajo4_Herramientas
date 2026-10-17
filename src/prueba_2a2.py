
import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():
    url = "http://127.0.0.1:8001/mcp"

    async with streamable_http_client(url) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            print("Conectado al servidor MCP")

            herramientas = await session.list_tools()

            print("\nHerramientas disponibles:")
            for herramienta in herramientas.tools:
                print(f"- {herramienta.name}")

            print("\nEjecutando buscar_faq...")

            resultado = await session.call_tool(
                "buscar_faq",
                arguments={
                    "pregunta": "¿Cuál es el peso máximo permitido para saltar?"
                }
            )

            print("\nResultado de la herramienta:")
            print(resultado)

            print("\nEjecutando consultar_clima...")

            resultado = await session.call_tool(
                "consultar_clima",
                arguments={
                    "fecha": "2026-10-25"
                }
            )

            print("\nResultado de la herramienta:")
            print(resultado)

            print("\nEjecutando calendarizar_cita...")

            resultado = await session.call_tool(
                "calendarizar_cita",
                arguments={
                    "fecha": "2026-10-25", 
                    "nombre_cliente": "Cliente", 
                }
            )

            print("\nResultado de la herramienta:")
            print(resultado)



if __name__ == "__main__":
    asyncio.run(main())
