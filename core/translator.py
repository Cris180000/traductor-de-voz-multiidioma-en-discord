"""
Traducción de texto usando deep_translator (Google Translate).
IMPORTANTE: Usar deep_translator, NO googletrans 3.x (es inestable).
"""

from deep_translator import GoogleTranslator
from utils.logger import obtener_logger

logger = obtener_logger(__name__)


class Traductor:
    def __init__(self):
        # Caché simple para no traducir el mismo texto dos veces
        self._cache: dict[str, str] = {}

    def traducir(
        self,
        texto: str,
        idioma_destino: str = "es",
        idioma_origen: str = "auto",
    ) -> str:
        """
        Traduce texto al idioma destino.

        Args:
            texto: Texto a traducir.
            idioma_destino: Código ISO 639-1 (ej: "es", "en", "fr").
            idioma_origen: "auto" para detección automática, o código ISO.

        Returns:
            Texto traducido, o el texto original si falla.
        """
        if not texto or not texto.strip():
            return ""

        clave_cache = f"{texto}|{idioma_origen}|{idioma_destino}"
        if clave_cache in self._cache:
            return self._cache[clave_cache]

        try:
            traductor = GoogleTranslator(source=idioma_origen, target=idioma_destino)
            resultado = traductor.translate(texto)
            self._cache[clave_cache] = resultado
            logger.debug(f"Traducido [{idioma_origen}→{idioma_destino}]: {resultado}")
            return resultado

        except Exception as e:
            logger.error(f"Error de traducción: {e}")
            return texto  # Devolver original si falla
