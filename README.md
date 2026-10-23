# PokeFetch

PokeFetch is a REST API built with **Python and FastAPI** that retrieves Pokémon statistics from a PostgreSQL database. The application is containerised with Docker Compose and includes pgAdmin for database administration.

## Prerequisites

Before getting started, ensure you have installed Docker

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:BenjaminCDavies/PokeFetch.git
cd pokefetch
```

### 2. Configure environment variables

Create a `.env` file in the repository root. Configure the PostgreSQL database and pgAdmin credentials as follows:

```dotenv
POSTGRES_DB=pokefetch
POSTGRES_USER=pokefetch
POSTGRES_PASSWORD=your_secure_database_password

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=your_secure_pgadmin_password
```

## Running the Application

PokeFetch supports separate development and production Docker Compose configurations.

### Development Environment

The development environment uses `compose.yaml` together with `compose.dev.yaml` to configure the development API, PostgreSQL database, and pgAdmin services.

**1. Build the development API container**

```bash
docker compose -f compose.yaml -f compose.dev.yaml build
```

**2. Start the containers**

```bash
docker compose -f compose.yaml -f compose.dev.yaml up -d
```

This starts the services defined by the combined Compose configuration in detached mode.

**3. Verify the API is running**

Open the interactive API documentation:

[http://localhost:8000/docs](http://localhost:8000/docs)

You can also check the API health using:

```bash
curl http://localhost:8000/health
```

### Production Environment

To build and start the production containers, use the default Compose configuration.

**1. Build the containers**

```bash
docker compose build
```

**2. Start the containers**

```bash
docker compose up -d
```

The API should be available at:

[http://localhost:8000](http://localhost:8000)

Interactive documentation is available at:

[http://localhost:8000/docs](http://localhost:8000/docs)

## API Documentation

The API provides the following endpoints.

| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| `GET`  | `/health`         | Check API health           |
| `GET`  | `/pokemon`        | Retrieve all Pokémon       |
| `GET`  | `/pokemon/{name}` | Retrieve a Pokémon by name |

### Interactive Documentation with Swagger UI

FastAPI automatically generates interactive API documentation from the application's endpoint definitions.

1. Start the application using either the development or production instructions.
2. Open [http://localhost:8000/docs](http://localhost:8000/docs).
3. Expand the endpoint you want to use.
4. Click **Try it out**.
5. Enter any required parameters, such as a Pokémon name.
6. Click **Execute** to send the request.
7. Review the response body, HTTP status code, and response headers.

## API Usage with cURL

The following examples assume the API is running locally on port `8000`.

### Health Check

**Endpoint:** `GET /health`

Check whether the API is responding.

```bash
curl http://localhost:8000/health
```

The endpoint returns the response defined by the application's health check handler.

### Retrieve All Pokémon

**Endpoint:** `GET /pokemon`

Retrieve all Pokémon available through the API.

```bash
curl http://localhost:8000/pokemon
```

To format a JSON response for easier reading, use `jq`:

```bash
curl -s http://localhost:8000/pokemon | jq .
```

### Retrieve a Single Pokémon

**Endpoint:** `GET /pokemon/{name}`

Retrieve a Pokémon by its name. Replace `{name}` with the Pokémon you want to look up.

For example, to retrieve Pikachu:

```bash
curl http://localhost:8000/pokemon/pikachu
```

To format the JSON response:

```bash
curl -s http://localhost:8000/pokemon/pikachu | jq .
```

## Database Administration with pgAdmin

The development environment includes pgAdmin for administering the PostgreSQL database.

1. Start the development containers.
2. Open the pgAdmin web interface using the port configured in your Compose files.
3. Log in with the credentials configured by `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`.
4. Register a PostgreSQL server connection if one has not already been configured.

When registering the database server, use the PostgreSQL **service name** defined in your Compose configuration as the hostname when connecting from the pgAdmin container. Use the configured PostgreSQL username, password, and database name.

## Stopping the Application

### Stop Production Containers

```bash
docker compose down
```

### Stop Development Containers

```bash
docker compose -f compose.yaml -f compose.dev.yaml down
```

These commands stop and remove the containers and associated Compose network. By default, named volumes are retained, so database data can persist between runs.

### Remove Containers and Volumes

To remove the containers and their associated Compose-managed volumes, append `-v` to the relevant command.

**Production:**

```bash
docker compose down -v
```

**Development:**

```bash
docker compose -f compose.yaml -f compose.dev.yaml down -v
```

**Warning:** Removing volumes can permanently delete persisted PostgreSQL data and other data stored in those volumes. Only use `-v` when you intend to reset the associated persistent data.
