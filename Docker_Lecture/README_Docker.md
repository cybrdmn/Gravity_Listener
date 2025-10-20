# Docker Tutorial - Introduction for Beginners

## What is Docker?

**Docker** is a platform that allows you to package and run applications in isolated environments called **containers**.

### Why Use Docker?

1. **Consistency**: "It works on my machine" becomes "It works everywhere"
   - Your code runs the same on your laptop, your classmate's computer, and the server

2. **Isolation**: Applications don't interfere with each other
   - Running Python 3.11 and Python 3.9 projects? No problem!

3. **Portability**: Share your entire development environment
   - No more "but I have a different setup" problems

4. **Efficiency**: Containers are lightweight and start in seconds
   - Unlike virtual machines which take minutes

## Key Concepts

### 1. Image
A **Docker image** is like a blueprint or template. It contains:
- Your application code
- Required libraries and dependencies
- Runtime environment (e.g., Python, Node.js, Java)
- Configuration files

### 2. Container
A **container** is a running instance of an image. You can create multiple containers from the same image.

**Analogy**: If an image is a recipe, a container is the actual dish you cook from that recipe.

### 3. Dockerfile
A **Dockerfile** is a text file with instructions on how to build a Docker image.

### 4. Docker Hub
**Docker Hub** is a public registry where you can find pre-built images (like Python, Node.js, MySQL, etc.).

## Prerequisites

### Install Docker

**Before the lecture, please install Docker:**

- **Windows/Mac**: Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
- **Linux**: Follow the installation guide for your distribution

**Verify installation** by opening your terminal/command prompt:
```bash
docker --version
```

You should see something like: `Docker version 24.0.0, build abc123`

**Troubleshooting**: If the command doesn't work:
1. Make sure Docker Desktop is running (look for the whale icon in your system tray)
2. Restart your terminal
3. On Windows, you might need to restart your computer after installation

## Part 1: Running Your First Container

Let's start by running a simple pre-built container. This is like test-driving Docker!

### Step 1: Run Hello World

Open your terminal and type:

```bash
docker run hello-world
```

**What happens?** (Step-by-step)
1. Docker checks if the `hello-world` **image** exists on your computer
2. If not found, it **downloads** it from Docker Hub (like an app store for Docker)
3. Docker creates and runs a **container** from that image
4. The container prints a welcome message and exits

**Expected output:**
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
[... more text ...]
```

✅ If you see this, congratulations! Docker is working correctly.

### Step 2: Run an Interactive Container

Let's run an Ubuntu Linux container and interact with it:

```bash
docker run -it ubuntu bash
```

**Flags explained:**
- `-i`: **Interactive** mode (keeps input open so you can type)
- `-t`: Allocates a **terminal** (gives you a command prompt)
- `ubuntu`: The **image name** (Linux distribution)
- `bash`: The **command** to run inside the container (a shell/terminal)

**What just happened?** You now have a complete Ubuntu Linux system running inside a container on your computer! Your command prompt should change to something like `root@abc123:/#`

Try some commands inside the container:
```bash
ls          # List files
pwd         # Show current directory
cat /etc/os-release   # Show Linux version info
```

**Exit the container** when you're done:
```bash
exit
```

💡 **Note**: Once you exit, the container stops but still exists. We'll learn how to manage these stopped containers next.

## Part 2: Managing Containers

### View Running Containers

```bash
docker ps
```

### View All Containers (including stopped ones)

```bash
docker ps -a
```

### Start a Stopped Container

```bash
docker start <container-id>
```

### Stop a Running Container

```bash
docker stop <container-id>
```

### Remove a Container

```bash
docker rm <container-id>
```

### Remove All Stopped Containers

```bash
docker container prune
```

## Part 3: Working with Images

### List Local Images

```bash
docker images
```

### Pull an Image from Docker Hub

```bash
docker pull python:3.11
```

### Remove an Image

```bash
docker rmi <image-id>
```

### Search for Images

```bash
docker search nginx
```

## Part 4: Building Your Own Image

Let's create a simple Python application and containerize it.

### Step 1: Create a Simple Python App

Create a directory and files:

**app.py**
```python
print("Hello from Docker!")
print("This is my first containerized application.")

name = input("What's your name? ")
print(f"Welcome, {name}!")
```

### Step 2: Create a Dockerfile

In the same directory, create a file named `Dockerfile` (no extension):

```dockerfile
# Use an official Python runtime as base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY app.py /app/

# Run the application
CMD ["python", "app.py"]
```

**Dockerfile Instructions Explained:**
- `FROM`: Specifies the base image
  - We use `python:3.11-slim` instead of `python:3.11` - see "Why Slim Images?" below
- `WORKDIR`: Sets the working directory inside the container
- `COPY`: Copies files from your machine to the container
- `CMD`: Specifies the command to run when the container starts

**💡 Why Slim Images?**

Notice we use `python:3.11-slim` instead of just `python:3.11`. Here's why:

| Image Type | Size | What's Inside | Best For |
|------------|------|---------------|----------|
| `python:3.11` | ~900 MB | Full Debian OS + compilers + many libraries | Development, need to compile packages |
| `python:3.11-slim` | ~120 MB | Minimal Debian + Python only | Most applications (recommended!) |
| `python:3.11-alpine` | ~50 MB | Tiny Alpine Linux + Python | Advanced users, smallest size needed |

**Benefits of slim images:**
- ✅ **Faster downloads**: 120 MB vs 900 MB means faster `docker pull`
- ✅ **Less disk space**: Important when you have many images
- ✅ **Faster deployments**: Upload to servers much quicker
- ✅ **Better security**: Fewer packages = fewer potential vulnerabilities
- ✅ **Quicker builds**: Less data to process

Always use `-slim` images unless you have a specific reason not to!

### Step 3: Build the Image

```bash
docker build -t my-python-app .
```

**Flags explained:**
- `-t`: Tags the image with a name
- `.`: Build context (current directory)

### Step 4: Run Your Container

```bash
docker run -it my-python-app
```

Congratulations! You've built and run your first Docker image.

## Part 5: A More Realistic Example - Web API

Now let's create a simple web application that you can access in your browser!

**What's FastAPI?** FastAPI is a modern Python framework that makes it easy to build web APIs. We're using it because:
- It's beginner-friendly
- It creates automatic interactive documentation
- It's widely used in industry

### Step 1: Create Application Files

**app.py**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Docker!",
        "description": "This is a containerized FastAPI app"
    }

@app.get("/about")
def read_about():
    return {
        "title": "About",
        "description": "This app is running inside a Docker container",
        "framework": "FastAPI"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {
        "item_id": item_id,
        "query": q
    }
```

**requirements.txt**
```
fastapi==0.119.1
uvicorn[standard]==0.38.0
```

### Step 2: Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py /app/

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**New Instructions:**
- `RUN`: Executes commands during image build
- `EXPOSE 8000`: **Documentation only** - tells other developers (and tools) that the application listens on port 8000
  - ⚠️ **Important**: `EXPOSE` does NOT publish the port or make it accessible from your computer
  - To actually access the port, you must use the `-p` flag when running the container
  - Think of it as a note saying "this app expects to use port 8000"
- `CMD`: Uses uvicorn (ASGI server) to run FastAPI

### Step 3: Build and Run

```bash
docker build -t my-fastapi-app .
docker run -p 8000:8000 my-fastapi-app
```

**Flag explained:**
- `-p 8000:8000`: Maps port 8000 on your machine to port 8000 in the container

### Step 4: Access the Application

Open your browser and go to:
- `http://localhost:8000/` - Main endpoint
- `http://localhost:8000/about` - About endpoint
- `http://localhost:8000/items/42?q=test` - Example with parameters
- `http://localhost:8000/docs` - Interactive API documentation (Swagger UI)
- `http://localhost:8000/redoc` - Alternative API documentation

**Note**: FastAPI automatically generates interactive API documentation!

Press `Ctrl+C` to stop the container.

### Step 5: Run in Detached Mode

```bash
docker run -d -p 8000:8000 --name fastapi-container my-fastapi-app
```

**New flags:**
- `-d`: Detached mode (runs in background)
- `--name`: Assigns a name to the container

Check logs:
```bash
docker logs fastapi-container
```

Follow logs in real-time:
```bash
docker logs -f fastapi-container
```

Stop the container:
```bash
docker stop fastapi-container
```

## Part 6: Persisting Data - Volumes and Bind Mounts

So far, all our containers lose their data when stopped or deleted. Let's learn how to persist data!

### Understanding the Problem

Try this experiment:
```bash
# Run a container and create a file
docker run -it ubuntu bash
# Inside the container, create a file:
echo "Important data" > /data.txt
exit

# Run the same image again
docker run -it ubuntu bash
# Try to find your file:
cat /data.txt  # File not found!
```

**Why?** Each container is isolated and ephemeral. When it's deleted, everything inside is gone.

### Two Ways to Persist Data

Docker provides **two different methods** for persisting data. It's important to understand when to use each:

| Method | Use Case | Where Data Lives | Best For |
|--------|----------|------------------|----------|
| **Named Volumes** | Production data (databases, uploads) | Managed by Docker | Database storage, user uploads, production |
| **Bind Mounts** | Development | Your project folder | Live code editing, sharing config files |

### Method 1: Named Volumes (Recommended for Databases)

**Named volumes** are managed by Docker and stored in a special location on your computer. They're the recommended way to persist application data.

**Syntax:** `-v volume-name:/container/path`

**Example: PostgreSQL with Named Volume**

```bash
# Create a named volume (Docker manages where it's stored)
docker volume create postgres-db-data

# Run PostgreSQL using the named volume
docker run -d \
  --name my-database \
  -e POSTGRES_PASSWORD=secret123 \
  -v postgres-db-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15-alpine
```

**Test persistence:**
```bash
# Connect and create data
docker exec -it my-database psql -U postgres
# In PostgreSQL:
CREATE DATABASE testdb;
\q

# Stop and remove the container
docker stop my-database
docker rm my-database

# Start a NEW container with the SAME volume
docker run -d \
  --name my-database-new \
  -e POSTGRES_PASSWORD=secret123 \
  -v postgres-db-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15-alpine

# Check if data is still there
docker exec -it my-database-new psql -U postgres -l
# Your testdb database is still there!
```

**Managing Named Volumes:**
```bash
# List all volumes
docker volume ls

# Inspect a volume (see where it's stored)
docker volume inspect postgres-db-data

# Remove a volume (careful - this deletes the data!)
docker volume rm postgres-db-data

# Remove all unused volumes
docker volume prune
```

**Why use named volumes for databases?**
- ✅ Docker manages the storage location (works the same on Windows/Mac/Linux)
- ✅ More portable (no hardcoded paths)
- ✅ Better performance on Windows/Mac (Docker Desktop optimization)
- ✅ Data is separated from your project folder
- ✅ Can be backed up and restored easily

### Method 2: Bind Mounts (Best for Development)

**Bind mounts** map a folder on your computer directly into the container. Perfect for development!

**Syntax:** `-v /host/path:/container/path`

**Example 1: Share code with a container**
```bash
# Create a folder and file on your computer
mkdir my-app
echo "print('Hello from shared folder!')" > my-app/app.py

# Run container with bind mount
docker run -it -v $(pwd)/my-app:/app python:3.11-slim bash

# Inside the container:
cd /app
ls           # You'll see app.py!
python app.py  # Runs your code
exit
```

**What happened?**
- The `my-app` folder on your computer is mapped to `/app` inside the container
- Changes in either location are reflected **immediately**
- Perfect for development!

**Example 2: Live code reloading for web development**
```bash
# Run FastAPI with your code mounted
docker run -v $(pwd):/app -p 8000:8000 my-fastapi-app

# Now edit app.py on your computer - changes appear instantly!
# No need to rebuild the image during development
```

### When to Use What?

**Use Named Volumes when:**
- ✅ Persisting database data (PostgreSQL, MySQL, MongoDB)
- ✅ Storing user uploads or generated files
- ✅ Production deployments
- ✅ You want Docker to manage where data is stored

**Use Bind Mounts when:**
- ✅ Developing and want live code changes
- ✅ Sharing configuration files with containers
- ✅ Need to access container logs on your machine
- ✅ You need the data in a specific location on your computer

### Quick Comparison

**Named Volume:**
```bash
# Docker manages where postgres-db-data is stored
docker run -v postgres-db-data:/var/lib/postgresql/data postgres:15-alpine
```

**Bind Mount:**
```bash
# You specify exactly where (./postgres-data on your computer)
docker run -v $(pwd)/postgres-data:/var/lib/postgresql/data postgres:15-alpine
```

### Tips for Bind Mounts

- Use `$(pwd)` for current directory on Mac/Linux
- Use `${PWD}` for current directory on Windows PowerShell
- The folder is created automatically if it doesn't exist
- Can be slower on Windows/Mac due to file system differences
- Add these folders to `.dockerignore` (e.g., `data/`)

## Part 7: Docker Networks - Connecting Containers

Now you know how to run containers and persist data. But what if containers need to talk to each other?

### Understanding the Problem

Imagine you have:
- A web application container
- A database container

How does the web app connect to the database? They need to communicate!

### Docker Networks Make It Easy

When containers are on the same network, they can talk to each other using **container names** as hostnames.

### Basic Network Commands

```bash
# List networks
docker network ls

# Create a custom network
docker network create my-app-network

# Inspect a network
docker network inspect my-app-network
```

### Practical Example: Web App + Database

**Step 1: Create a network**
```bash
docker network create app-network
```

**Step 2: Run a database container on the network**
```bash
docker run -d \
  --name db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret123 \
  postgres:15-alpine
```

**Step 3: Run a web app container on the same network**
```bash
docker run -d \
  --name webapp \
  --network app-network \
  -p 8000:8000 \
  -e DATABASE_HOST=db \
  my-fastapi-app
```

**The magic:** Inside the webapp container, you can connect to the database using the hostname `db`!

```python
# In your Python code:
DATABASE_URL = f"postgresql://postgres:secret123@db:5432/mydb"
# "db" is the container name!
```

### Why This Works

- Both containers are on the `app-network`
- Docker provides automatic DNS resolution
- Container name → IP address
- No need to know IP addresses!

### Quick Demo with Ping

```bash
# Create network and containers
docker network create test-network
docker run -d --name container1 --network test-network alpine sleep 3600
docker run -d --name container2 --network test-network alpine sleep 3600

# From container1, ping container2 by name
docker exec container1 ping container2
# It works! Containers can talk to each other

# Clean up
docker stop container1 container2
docker rm container1 container2
docker network rm test-network
```

### Key Concepts: Networks

- Containers on the **same network** can communicate
- Use **container names** as hostnames
- Docker creates a **default bridge network** automatically
- Create **custom networks** for better isolation

---

## Part 8: Docker Compose - Putting It All Together

You've learned about volumes (Part 6) and networks (Part 7). Now, instead of typing long `docker run` commands with all those flags, let's use **Docker Compose** to manage everything in one simple file!

### The Problem Without Docker Compose

Remember our web app + database example from Part 7? We had to type:

```bash
docker network create app-network

docker run -d \
  --name db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret123 \
  -v $(pwd)/data:/var/lib/postgresql/data \
  postgres:15-alpine

docker run -d \
  --name webapp \
  --network app-network \
  -p 8000:8000 \
  -e DATABASE_HOST=db \
  -v $(pwd):/app \
  my-fastapi-app
```

That's a lot to remember! And if you restart your computer, you have to type it all again.

### The Solution: Docker Compose

Docker Compose lets you define everything in one `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  webapp:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_HOST=db
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=secret123
    volumes:
      - ./data:/var/lib/postgresql/data
```

Then just run: `docker compose up -d`

**That's it!** Docker Compose automatically:
- Creates a network for your services
- Starts containers in the right order
- Connects everything together

### Why Docker Compose?

- ✅ **Simplicity**: Define all services in one file
- ✅ **Reproducibility**: Share the file with your team
- ✅ **Easy management**: One command to start/stop everything
- ✅ **Automatic networking**: Services can talk to each other by name
- ✅ **Volume management**: Persist data easily

### Example 1: Simple FastAPI App with Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app  # Remember bind mounts from Part 6?
    environment:
      - ENVIRONMENT=development
```

**Key concepts:**
- `services`: Defines containers to run
- `build`: Build from Dockerfile in current directory
- `ports`: Port mapping (same as `-p` flag from Part 5)
- `volumes`: Bind mount from Part 6 - live code changes!
- `environment`: Set environment variables

Start the application:
```bash
docker compose up
```

Start in detached mode:
```bash
docker compose up -d
```

Stop all services:
```bash
docker compose down
```

View logs:
```bash
docker compose logs -f
```

### Example 2: FastAPI with PostgreSQL Database

Let's create a more realistic application with a database.

**app.py** (updated)
```python
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    db_host = os.getenv("DATABASE_HOST", "not configured")
    return {
        "message": "Hello from Docker Compose!",
        "database": db_host
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

**docker-compose.yml**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_HOST=db
      - DATABASE_PORT=5432
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
      - POSTGRES_DB=mydb
    volumes:
      - ./data:/var/lib/postgresql/data  # Database files stored in ./data folder
    ports:
      - "5432:5432"

```

**New concepts from Parts 6 & 7 in action:**
- `volumes`: Bind mount from Part 6 - database data persists!
- `depends_on`: Ensures database starts before web service
- **Automatic networking**: Services can use each other's names as hostnames (remember Part 7?)
  - The web service connects to `DATABASE_HOST=db` - that's the container name!
  - Docker Compose creates a network automatically - no `docker network create` needed!

Start everything:
```bash
docker compose up -d
```

Check status:
```bash
docker compose ps
```

Access web service: `http://localhost:8000`

Stop and remove everything (including volumes):
```bash
docker compose down -v
```

### Example 3: Complete Application Stack

**docker-compose.yml** (full stack)
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - .:/app

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
      - POSTGRES_DB=mydb
    volumes:
      - ./data:/var/lib/postgresql/data  # Database files stored in ./data folder

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

```

This creates:
- FastAPI web application
- PostgreSQL database
- Redis cache
- All connected via Docker network

### Useful Docker Compose Commands

| Command | Description |
|---------|-------------|
| `docker compose up` | Start all services |
| `docker compose up -d` | Start in background |
| `docker compose down` | Stop and remove containers |
| `docker compose down -v` | Stop and remove containers + volumes |
| `docker compose ps` | List services |
| `docker compose logs` | View logs |
| `docker compose logs -f web` | Follow logs for specific service |
| `docker compose exec web bash` | Execute command in running service |
| `docker compose build` | Build/rebuild services |
| `docker compose restart` | Restart services |

### Development Workflow with Compose

1. **Start services**:
   ```bash
   docker compose up -d
   ```

2. **View logs**:
   ```bash
   docker compose logs -f web
   ```

3. **Make code changes** (with volume mounted, changes are live)

4. **Restart specific service**:
   ```bash
   docker compose restart web
   ```

5. **Stop everything**:
   ```bash
   docker compose down
   ```

## Common Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `docker run <image>` | Create and start a container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker images` | List images |
| `docker build -t <name> .` | Build an image |
| `docker stop <container>` | Stop a container |
| `docker rm <container>` | Remove a container |
| `docker rmi <image>` | Remove an image |
| `docker logs <container>` | View container logs |
| `docker exec -it <container> bash` | Enter a running container |

## Best Practices

1. **Use Official Images**: Start with official base images from Docker Hub
2. **Keep Images Small**: Use slim or alpine variants when possible (see Part 4 for comparison table)
   - Smaller images = faster builds, downloads, and deployments
   - Less disk space usage
   - Improved security (fewer packages = fewer vulnerabilities)
3. **One Process per Container**: Each container should have a single responsibility
4. **Use .dockerignore**: Exclude unnecessary files (like `.git`, `node_modules`)
5. **Don't Run as Root**: Create a non-root user in your Dockerfile for security
6. **Layer Caching**: Order Dockerfile instructions from least to most frequently changing

---

## Part 9: Docker Best Practices for Production

### 1. Use Multi-Stage Builds

Reduce image size by separating build and runtime environments.

**Dockerfile (multi-stage)**
```dockerfile
# Build stage
FROM python:3.11 as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY app.py .

# Make sure scripts are in PATH
ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Benefits:**
- Smaller final image
- Faster deployment
- More secure (no build tools in production)

### 2. Keep Images Small

**Why care about image size?**
- Faster to build and deploy
- Uses less disk space on your computer and servers
- Faster to download for your teammates
- Lower bandwidth costs in production
- Better security (fewer packages = smaller attack surface)

**How to keep images small:**
- ✅ Use `-slim` base images (e.g., `python:3.11-slim` instead of `python:3.11`)
- ✅ Use `.dockerignore` to exclude unnecessary files
- ✅ Use multi-stage builds (see example above)
- ✅ Remove build dependencies after installation
- ✅ Combine RUN commands to reduce layers

### 3. Use .dockerignore

Create a `.dockerignore` file to exclude unnecessary files (this also makes images smaller!):

```
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.git
.gitignore
.dockerignore
.env
*.md
tests/
.pytest_cache
.vscode
.idea
*.log
data/
```

### 4. Don't Run as Root

**Dockerfile (with non-root user)**
```dockerfile
FROM python:3.11-slim

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Change ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 5. Health Checks

Add health checks to monitor container status:

**Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Health check parameters explained:**
- `--interval=30s`: Check health every 30 seconds
- `--timeout=3s`: Consider check failed if it takes longer than 3 seconds
- `--start-period=5s`: Give the container 5 seconds to start before checking
- `--retries=3`: Mark as unhealthy after 3 consecutive failures

Check container health:
```bash
docker ps
# Look for health status in output: healthy, unhealthy, or starting
```

**Health Checks in Docker Compose**

You can also define health checks in your `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=secret123
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - ./data:/var/lib/postgresql/data
```

**What this does:**
- The `web` service won't start until `db` is healthy (not just started)
- Docker automatically runs health checks and reports status
- Orchestration tools (like Kubernetes) can use this to restart unhealthy containers

Check health status with compose:
```bash
docker compose ps
# Shows health status for each service
```

### 6. Use Specific Image Tags

**Bad:**
```dockerfile
FROM python:latest
```

**Good:**
```dockerfile
FROM python:3.11-slim
```

**Why?** `latest` can change, breaking your builds. Specific tags ensure reproducibility.

### 7. Layer Caching Optimization

Order matters! Put frequently changing instructions last:

**Dockerfile (optimized)**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dependencies change less frequently - install first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code changes frequently - copy last
COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 8. Environment-Specific Configurations

**docker-compose.yml (with env file)**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    env_file:
      - .env.db
    volumes:
      - ./data:/var/lib/postgresql/data  # Database files stored in ./data folder

```

**.env**
```
ENVIRONMENT=production
DATABASE_URL=postgresql://user:pass@db:5432/mydb
SECRET_KEY=your-secret-key
```

## Part 10: Debugging and Troubleshooting Docker Issues

### Inspect Running Containers

```bash
# View container details
docker inspect <container-id>

# View resource usage
docker stats

# View processes inside container
docker top <container-id>
```

### Access Container Shell

```bash
# For running containers
docker exec -it <container-id> bash

# If bash not available (alpine images)
docker exec -it <container-id> sh

# For stopped containers (debug)
docker run -it --entrypoint bash <image-name>
```

### View and Follow Logs

```bash
# View logs
docker logs <container-id>

# Follow logs (real-time)
docker logs -f <container-id>

# Last 100 lines
docker logs --tail 100 <container-id>

# With timestamps
docker logs -t <container-id>
```

### Common Issues and Solutions

#### Issue 1: Port Already in Use

**Error:** `Bind for 0.0.0.0:8000 failed: port is already allocated`

**Solution:**
```bash
# Find what's using the port (macOS/Linux)
lsof -i :8000

# Use different host port
docker run -p 8080:8000 my-app
```

#### Issue 2: Container Exits Immediately

**Solution:**
```bash
# Check logs
docker logs <container-id>

# Run interactively to see errors
docker run -it <image-name>
```

#### Issue 3: Changes Not Reflected

**Solution:**
```bash
# Rebuild image (no cache)
docker build --no-cache -t my-app .

# For compose
docker compose build --no-cache
```

#### Issue 4: Permission Denied

**Solution:**
```bash
# On Linux, add user to docker group
sudo usermod -aG docker $USER

# Log out and back in

# Or run with sudo (not recommended)
sudo docker run ...
```

#### Issue 5: Out of Disk Space

**Solution:**
```bash
# Remove unused data
docker system prune

# Remove everything (including volumes)
docker system prune -a --volumes

# Check disk usage
docker system df
```

## Troubleshooting

### Container Exits Immediately
- Check logs: `docker logs <container-id>`
- Run interactively: `docker run -it <image> bash`

### Port Already in Use
- Use a different port: `-p 8080:5000` (maps local 8080 to container 5000)
- Check what's using the port: `lsof -i :5000` (macOS/Linux)

### Image Not Found
- Check spelling
- Pull explicitly: `docker pull <image>`

### Permission Denied
- On Linux, you may need to add your user to the docker group:
  ```bash
  sudo usermod -aG docker $USER
  ```

## Additional Resources

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
- [Play with Docker](https://labs.play-with-docker.com/) - Online Docker playground

## 📚 Summary - What You Should Know After This Tutorial

### ✅ Essential Skills (Parts 1-8) - Core Docker Concepts
After completing the core sections, you should be able to:

**Basics (Parts 1-5):**
- ✅ **Explain** what Docker is and why it's useful
- ✅ **Run** containers from pre-built images (`docker run`)
- ✅ **Manage** containers (start, stop, remove)
- ✅ **Create** your own Dockerfile
- ✅ **Build** and run your own Docker images
- ✅ **Understand** port mapping (`-p 8000:8000`)

**Advanced Basics (Parts 6-8):**
- ✅ **Persist data** using volumes and bind mounts
- ✅ **Connect containers** using Docker networks
- ✅ **Orchestrate multi-container apps** with Docker Compose
- ✅ **Understand** how volumes, networks, and compose work together

### 🎓 Production Skills (Parts 9-11)

- ✅ Apply production best practices (multi-stage builds, security)
- ✅ Debug and troubleshoot Docker issues effectively
- ✅ Build complete real-world applications

## 🎯 Final Thoughts

Docker is a powerful tool that will help you develop, deploy, and manage applications more efficiently.

**Learning path for first semester students:**
1. **Master Parts 1-5 first** - Basic Docker usage
2. **Then learn Parts 6-8** - Volumes, Networks, and Compose (essential for real projects!)
3. **Parts 9-11 are optional** - Come back when you need them

Practice regularly, and don't be afraid to make mistakes. Every expert was once a beginner who kept practicing.

**Remember**:
- Containers are **isolated** - experiment freely!
- Docker **saves time** - no more "works on my machine" problems
- This skill is **valuable** - employers look for Docker experience