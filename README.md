# CrewAI Agent MCP

Un agente inteligente de CrewAI que utiliza el protocolo MCP (Model Context Protocol) para realizar scraping web y extraer información de portafolios de SoftwareOne Company.

## 🚀 Características

- **Agente de Scraping Inteligente**: Utiliza CrewAI para crear un agente especializado en extracción de información web
- **Protocolo MCP**: Integración con Model Context Protocol para herramientas avanzadas
- **LLM Configurable**: Soporte para múltiples modelos de lenguaje (Gemini, OpenAI, Claude)
- **Scraping Dirigido**: Enfocado en extraer información de portafolios específicos de SoftwareOne

## 📋 Requisitos Previos

- Python 3.13+
- UV (gestor de paquetes)
- API Key de Google Gemini (o el LLM de tu preferencia)
- Servidor MCP ejecutándose en `http://localhost:8000/mcp`

### 🔗 Servidor MCP Requerido

Este proyecto requiere el servidor MCP de CrewAI para funcionar correctamente. El servidor proporciona las herramientas de scraping web necesarias:

**Repositorio del Servidor MCP**: [crewai-mcp-server](https://github.com/OrlandContreras/crewai-mcp-server)

El servidor MCP integra herramientas de CrewAI para proporcionar capacidades de scraping web a través del protocolo Model Context Protocol (MCP).

## 🛠️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <tu-repositorio>
   cd crewai-agent-mcp
   ```

2. **Instala las dependencias**:
   ```bash
   uv sync
   ```

3. **Configura el servidor MCP**:
   
   Clona e instala el servidor MCP requerido:
   ```bash
   # En otra terminal o directorio
   git clone https://github.com/OrlandContreras/crewai-mcp-server.git
   cd crewai-mcp-server
   uv sync
   python main.py
   ```
   
   El servidor debe estar ejecutándose en `http://localhost:8000/mcp` antes de ejecutar el agente.

4. **Configura las variables de entorno**:
   ```bash
   cp .env.example .env
   ```
   
   Edita el archivo `.env` y agrega tus API keys:
   ```env
   GOOGLE_API_KEY=tu_google_api_key_aqui
   MCP_SERVER_URL=http://localhost:8000/mcp
   ```

## 🚀 Uso

### Ejecución Básica

```bash
python main.py
```

### Configuración del Agente

El agente está configurado para:
- **Rol**: Scraper Agent
- **Objetivo**: Extraer información de portafolios de SoftwareOne Company
- **Website objetivo**: `https://www.softwareone.com/es-co/{portfolio_type}`
- **Tipo de portafolio por defecto**: "Digital Workplace Services"

### Personalización

Puedes modificar el tipo de portafolio editando la variable en `main.py`:

```python
result = crew.kickoff(
    inputs={
        "portfolio_type": "Cloud Services"  # Cambia aquí
    }
)
```

## 📁 Estructura del Proyecto

```
crewai-agent-mcp/
├── main.py              # Archivo principal del agente
├── pyproject.toml        # Configuración del proyecto y dependencias
├── .env.example          # Plantilla de variables de entorno
├── .gitignore           # Archivos ignorados por Git
├── README.md            # Este archivo
└── uv.lock              # Lockfile de dependencias
```

## 🔧 Configuración Avanzada

### Variables de Entorno Disponibles

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `GOOGLE_API_KEY` | API Key de Google Gemini | Requerido |


### Modelos LLM Soportados

- **Google Gemini**: `gemini/gemini-2.0-flash`

## 🏗️ Arquitectura del Sistema

Este proyecto utiliza una arquitectura de dos componentes:

```
┌─────────────────────┐       ┌─────────────────────┐
│   CrewAI Agent      │  MCP  │   MCP Server        │
│   (main.py)         │<----->│   (crewai-mcp-server)│
│                     │       │                     │
│ - Gemini LLM        │       │ - Scraping Tools    │
│ - Task Execution    │       │ - Web Content Fetch │
│ - Result Processing │       │ - HTTP API          │
└─────────────────────┘       └─────────────────────┘
```

### 🔄 Componentes

- **Agent CrewAI**: Orquesta las tareas de scraping usando inteligencia artificial
- **Servidor MCP**: Proporciona las herramientas de scraping web a través del protocolo MCP
- **Protocolo MCP**: Facilita la comunicación entre el agente y las herramientas de scraping

## 🤖 Funcionamiento del Agente

1. **Inicialización**: El agente se conecta al servidor MCP para obtener herramientas de scraping
2. **Configuración**: Se establece el LLM (Gemini por defecto) y los parámetros
3. **Creación de Tarea**: Se define la tarea de scraping con el tipo de portafolio específico
4. **Ejecución**: El crew ejecuta la tarea de forma secuencial
5. **Resultado**: Se retorna la información extraída del portafolio

## 📊 Salida Esperada

El agente extraerá información estructurada sobre los servicios del portafolio, incluyendo:
- Servicios en la nube
- Transformación digital
- Ciberseguridad
- Servicios de TI

## 🛠️ Desarrollo

### Dependencias Principales

- `crewai`: Framework para agentes AI colaborativos
- `crewai-tools[mcp]`: Herramientas MCP para CrewAI

### Ejecutar en Modo Desarrollo

```bash
# Activar el entorno virtual
source .venv/bin/activate

# Ejecutar con logs detallados
CREWAI_VERBOSE=true python main.py
```

## 🐛 Resolución de Problemas

### Error: "Import crewai could not be resolved"
```bash
uv sync
```

### Error: "MCP Server not available"
- Verificar que el servidor MCP esté ejecutándose en `http://localhost:8000/mcp`
- Comprobar la configuración en `MCP_SERVER_URL`
- Asegurarse de que el servidor [crewai-mcp-server](https://github.com/OrlandContreras/crewai-mcp-server) esté clonado e iniciado
- Verificar que no haya conflictos de puertos en el sistema

### Error: "API Key not found"
- Verificar que `.env` existe y contiene `GOOGLE_API_KEY`
- Comprobar que la API key es válida

