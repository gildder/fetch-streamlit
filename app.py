import asyncio
import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

# Configuración de la página
st.set_page_config(page_title="MCP Fetch Web Explorer", page_icon="🌐", layout="wide")

# Cargar variables de entorno
load_dotenv()


# Función para procesar la consulta
async def process_query(url, query_type):
    # Crear MCPClient desde el archivo de configuración
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "fetch_mcp.json")
    )

    # Crear LLM
    llm = ChatOpenAI(model="gpt-4")

    # Crear agente
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        if query_type == "Resumir contenido":
            prompt = f"Fetch the content from {url} and provide a comprehensive summary of the main points"
        elif query_type == "Extraer datos clave":
            prompt = f"Fetch the content from {url} and extract key information, facts, and statistics"
        else:  # Análisis completo
            prompt = f"Fetch the content from {url} and provide a detailed analysis including main topics, key points, and important conclusions"

        result = await agent.run(prompt, max_steps=30)
        return result
    finally:
        if client.sessions:
            await client.close_all_sessions()


# Título y descripción
st.title("🌐 MCP Fetch Web Explorer")
st.markdown(
    """
Esta aplicación te permite explorar y analizar contenido web usando el MCP Fetch Server.
Simplemente ingresa una URL y selecciona el tipo de análisis que deseas realizar.
"""
)

# Entrada de URL y tipo de análisis
with st.form("web_analysis_form"):
    url = st.text_input("URL del sitio web", placeholder="https://ejemplo.com")
    analysis_type = st.selectbox(
        "Tipo de análisis",
        ["Resumir contenido", "Extraer datos clave", "Análisis completo"],
    )

    submit_button = st.form_submit_button("Analizar")

# Procesar la solicitud cuando se envía el formulario
if submit_button and url:
    with st.spinner("Procesando la URL..."):
        try:
            result = asyncio.run(process_query(url, analysis_type))

            # Mostrar resultados
            st.success("¡Análisis completado!")

            with st.expander("Ver resultados", expanded=True):
                st.markdown("### Resultados del análisis")
                st.write(result)

        except Exception as e:
            st.error(f"Error al procesar la URL: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center'>
    <p>Desarrollado por <a href='https://github.com/gildder'>Gildder</a> |
    Usando MCP Fetch Server y Streamlit</p>
</div>
""",
    unsafe_allow_html=True,
)
