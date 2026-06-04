"""
Sistema de logging centralizado para el proyecto.
"""

import logging
import sys


def obtener_logger(nombre: str) -> logging.Logger:
    """
    Devuelve un logger configurado con el nombre del módulo.

    Args:
        nombre: Nombre del módulo (usar __name__).
    """
    logger = logging.getLogger(nombre)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="[%(levelname)s] %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
