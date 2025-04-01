# Configuración en Streamlit Cloud

Este documento explica cómo configurar correctamente esta aplicación en Streamlit Cloud para evitar errores como el AttributeError relacionado con Chroma.

## Pasos para configurar en Streamlit Cloud

1. Inicia sesión en [Streamlit Cloud](https://streamlit.io/cloud)
2. Despliega la aplicación desde tu repositorio GitHub
3. En el panel de la aplicación, ve a **Configuración de la aplicación** (ícono ⚙️)
4. Selecciona **Secrets**
5. Agrega las siguientes variables en formato TOML:

```toml
[general]
# Configuración de OpenAI (OBLIGATORIO)
OPENAI_API_KEY = "tu-api-key-de-openai"

# Configuración de Pinecone (OBLIGATORIO)
PINECONE_API_KEY = "tu-api-key-de-pinecone" 
PINECONE_ENVIRONMENT = "us-east-1"
PINECONE_INDEX_NAME = "timbre"

# Otras configuraciones (según necesites)
LANGCHAIN_API_KEY = "tu-api-key-de-langchain"
TAVILY_API_KEY = "tu-api-key-de-tavily"
EMAIL_REMITENTE = "tu-email@example.com"
EMAIL_DESTINATARIO = "tu-email@example.com"
EMAIL_PASSWORD = "tu-password"
```

6. Guarda la configuración
7. Reinicia tu aplicación desde el panel

## Solución de problemas comunes

### Error AttributeError relacionado con Chroma

Si ves un error como:
```
AttributeError: This app has encountered an error. The original error message is redacted to prevent data leaks.
```

**Causa**: La aplicación está intentando usar Chroma en Streamlit Cloud, pero no está configurado correctamente.

**Solución**: La aplicación ahora usa exclusivamente Pinecone para almacenar y recuperar embeddings en Streamlit Cloud. Asegúrate de configurar correctamente las variables de Pinecone en los secretos de Streamlit.

### Error con Pinecone

Si ves errores relacionados con Pinecone:

1. Verifica que la API key de Pinecone sea correcta
2. Asegúrate de que el índice especificado (`timbre` por defecto) exista en tu cuenta de Pinecone
3. Verifica que el índice tenga la dimensión correcta (1536 para embeddings de OpenAI)

## Consideraciones importantes

- Los archivos locales o directorios (como `.chroma/`) no persisten en Streamlit Cloud entre ejecuciones
- Si necesitas almacenar datos persistentes, usa servicios en la nube como Pinecone
- Las claves API y otras credenciales deben configurarse como secretos, no en archivos de código

Para más información, consulta la [documentación oficial de Streamlit Cloud](https://docs.streamlit.io/streamlit-cloud). 