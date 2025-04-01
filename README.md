# Asistente Jurídico Tributario

Aplicación de asistencia jurídica tributaria que utiliza técnicas avanzadas de Retrieval Augmented Generation (RAG) para proporcionar respuestas precisas a consultas jurídicas en el área de derecho tributario colombiano.

## Características

- **Interfaz de usuario intuitiva**: Aplicación web desarrollada con Streamlit
- **Respuestas fundamentadas**: Basadas en documentos oficiales de la DIAN
- **Biblioteca de documentos**: 
  - Timbre: Documentos sobre el Impuesto de Timbre
  - Retención: Documentos sobre Retención en la Fuente
  - IVA: Documentos sobre el Impuesto al Valor Agregado
- **Verificación de fuentes**:
  - Acceso directo a los documentos citados en las respuestas
  - Organización por categorías tributarias
  - Trazabilidad de la información jurídica
- **Buzón de Observaciones**: Sistema para recibir comentarios y sugerencias de los usuarios

## Cómo funciona - Arquitectura RAG

Este proyecto implementa un sistema de Retrieval Augmented Generation Avanzado (RAG) para proporcionar respuestas precisas sobre temas tributarios. El flujo completo del proceso es:

### 1. Ingestión de documentos
- **Recolección de fuentes**: Se descargan documentos oficiales (conceptos, normativas, jurisprudencia) directamente de la DIAN. Se usa Bs4 para extraer la información.

- **Procesamiento de documentos**: 
  - Extracción del contenido textual 
  - Limpieza y normalización del texto
  - División en "chunks" (fragmentos) más pequeños para su procesamiento eficiente

### 2. Creación de embeddings y almacenamiento
- **Generación de embeddings**: Cada fragmento de texto se convierte en un vector mediante modelos de embeddings
- **Indexación vectorial**: Los embeddings se almacenan en una base de datos vectorial (Pinecone) que permite búsquedas semánticas eficientes
- **Metadatos**: Cada embedding mantiene referencias a su documento original, facilitando la trazabilidad

### 3. Proceso de consulta y respuesta
- **Recepción de consulta**: El usuario realiza una pregunta a través de la interfaz
- **Búsqueda semántica**: 
  - La consulta se convierte en un embedding
  - Se realiza una búsqueda de similitud en la base de datos vectorial
  - Se recuperan los fragmentos más relevantes para la consulta
- **Generación contextualizada**: 
  - Los fragmentos relevantes se utilizan como contexto para un modelo de lenguaje (OpenAI)
  - El modelo genera una respuesta basada exclusivamente en el contexto proporcionado
  - Se incluyen citas y referencias a los documentos originales

### 4. Mejora continua
- **Retroalimentación**: Sistema de buzón para recibir observaciones de usuarios
- **Actualización de conocimiento**: Proceso regular de actualización con nuevos documentos de la DIAN, sentencias del Consejo de Estado (extracción con selenium)

## Estructura del Proyecto

- `Inicio.py`: Página principal con descripción general de la aplicación
- `pages/`: Directorio con páginas adicionales de la aplicación
  - `3_Timbre.py`: Página para consultas sobre Impuesto de Timbre
  - `4_Retencion.py`: Página para consultas sobre Retención en la Fuente
  - `5_Biblioteca.py`: Página para acceder a los documentos jurídicos
  - `6_Buzón_de_Observaciones.py`: Página para enviar comentarios y sugerencias
  - `7_IVA.py`: Página para consultas sobre Impuesto al Valor Agregado
- `ingest_*.py`: Scripts para la ingestión y procesamiento de documentos por categoría
- `graph/`: Directorio con definiciones de grafos LangGraph para flujos avanzados de RAG
- `data/`: Datos adicionales para la aplicación

## Flujos RAG implementados

El sistema utiliza diferentes flujos avanzados de RAG para mejorar la calidad de las respuestas:

1. **RAG básico**: Búsqueda y generación directa con el contexto recuperado
2. **RAG con reranking**: Ordenamiento adicional de documentos relevantes mediante modelos específicos
3. **RAG conversacional**: Mantiene contexto de la conversación para consultas de seguimiento
4. **RAG con verificación**: Incluye un paso de verificación para asegurar que la respuesta esté fundamentada en los documentos

## Requisitos

- Python 3.10 o superior
- Poetry (gestor de dependencias)
- Claves API para:
  - OpenAI
  - Pinecone
  - Tavily (opcional)
  - LangChain (opcional para trazabilidad)
- Cuenta de correo electrónico (para el buzón de observaciones)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/asistente-juridico-tributario.git
   cd asistente-juridico-tributario
   ```

2. Instala las dependencias con Poetry:
   ```
   poetry install
   ```

3. Crea un archivo `.env` con tus claves API (usa `.env.example` como referencia)

## Ejecución
   ```
1. Inicia la aplicación Streamlit:
   ```
   streamlit run Inicio.py
   ```

2. Abre tu navegador en `http://localhost:8501`

## Ingestión de nuevos documentos

Para incorporar nuevos documentos al sistema:

1. Coloca los documentos en la carpeta correspondiente dentro de `data/`
2. Ejecuta el script de ingestión apropiado:
   ```
   python ingest_renta_docs.py  # para documentos de Renta
   python ingest_iva_docs.py    # para documentos de IVA
   ```
## Licencia

Para uso académico.