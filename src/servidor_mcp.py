from mcp.server import MCPServer
import logging 
from common import faq_service, weather_service, citas_service


mcp = MCPServer("ParachuteMCP")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("ParachuteMCP")


@mcp.tool()
def buscar_faq(pregunta: str) -> dict: 
    logger.info("Ejecutando herramienta: buscar_faq")

    try: 
        resultado = faq_service.buscar_faq(pregunta)
        logger.info("Finalizo herramiento: buscar_faq")
        return resultado

    except Exception: 
        logger.exception("Error en buscar_faq")
        raise


@mcp.tool()
def consultar_clima(fecha:str) -> dict: 
    logger.info("Ejecuntado herramienta: consultar_clima")

    try: 
        resultado = weather_service.consultar_clima(fecha)
        logger.info("Finalizo herramienta: consultar_clima")
        return resultado

    except Exception:
        logger.exception("Error en consultar_clima")

@mcp.tool()
def calendarizar_cita(fecha: str, nombre_cliente: str = "Cliente") -> dict: 
    logger.info("Ejecuntado herramienta: calendarizar_cita")

    try:
        resultado = citas_service.calendarizar_cita(fecha, nombre_cliente)
        logger.info("Finalizo herramienta: calendarizar_cita")
        return resultado
    
    except Exception:
            logger.exception("Error en calendarizar_cita")


if __name__ == "__main__":
    logger.info("Iniciando servidor MCP")

    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8001,
        stateless_http=True,
        json_response=True,
    )
