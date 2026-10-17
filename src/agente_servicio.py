from agents import Runner
from agente_jerarquico import supervisor_global

async def consultar_agente(pregunta: str) -> str:
    """Esta funcion permite pasar las preguntas al agente mientras se trabaja en el servidor a2a."""

    pregunta = pregunta.strip()

    if not pregunta:
        raise ValueError("La pregunta no puede estar vacia.")

    resultado = await Runner.run(
        supervisor_global, 
        pregunta, 
    )

    if resultado.final_output is None: 
        raise RuntimeError("El agente no ha generado una respuesta.")


    return str(resultado.final_output)