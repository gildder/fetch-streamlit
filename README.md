# MCP Fetch Web Explorer

[![GitHub](https://img.shields.io/badge/GitHub-gildder-181717?style=flat&logo=github)](https://github.com/gildder)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)

Una aplicación web interactiva que utiliza MCP Fetch Server para analizar y extraer información de sitios web. Esta aplicación combina el poder del Model Context Protocol con una interfaz de usuario amigable construida con Streamlit.

## Características

- 🌐 Análisis de cualquier URL web
- 📊 Múltiples tipos de análisis:
  - Resumen de contenido
  - Extracción de datos clave
  - Análisis completo
- 🚀 Interfaz de usuario intuitiva y responsive
- 💡 Resultados detallados y formateados

## Requisitos

- Python 3.11+
- pip
- Streamlit
- OpenAI API Key

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/gildder/mcp-use-tutorial.git
cd mcp-use-tutorial/fetch-streamlit
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura tu API key de OpenAI:
Crea un archivo `.env` y añade tu API key:
```
OPENAI_API_KEY=tu_api_key_aqui
```

## Uso

Para ejecutar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado.

## Cómo usar

1. Ingresa la URL del sitio web que deseas analizar
2. Selecciona el tipo de análisis que deseas realizar
3. Haz clic en "Analizar"
4. Espera mientras se procesa la solicitud
5. ¡Revisa los resultados!

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## Autor

👤 **Gildder Guerrero**

* GitHub: [@gildder](https://github.com/gildder)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

---

Si te gusta este proyecto, por favor dale una ⭐️!
