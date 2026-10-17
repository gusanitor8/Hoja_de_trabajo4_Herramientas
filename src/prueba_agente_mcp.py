
import asyncio

from agents import Agent, Runner, ModelSettings
from agents.mcp import (
    MCPServerStreamableHttp,
    create_static_tool_filter,
)
from common.groq_model import MODEL


async def main():

    async with MCPServerStreamableHttp(
        name="ParachuteMCP",
        params={
            "url": "http://127.0.0.1:8001/mcp"
        },
        cache_tools_list=True,
        tool_filter=create_static_tool_filter(
            allowed_tool_names=["buscar_faq"]
        ),
    ) as servidor_mcp:

        agente = Agent(
            name="AgenteAtencionClienteMCP",
            instructions=(
                "Eres un especialista en preguntas frecuentes "
                "de Parachute S.A. Utiliza buscar_faq para "
                "responder. No inventes información. "
                "Responde en español."
            ),
            mcp_servers=[servidor_mcp],
            model=MODEL,
            model_settings=ModelSettings(
                tool_choice="required"
            ),
        )

        resultado = await Runner.run(
            agente,
            "¿Cuál es el peso máximo permitido para saltar?"
        )

        print("\nRespuesta del agente:")
        print(resultado.final_output)


if __name__ == "__main__":
    asyncio.run(main())
