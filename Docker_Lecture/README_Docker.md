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

### 💡 Building for Different Operating Systems and Architectures

Docker images can be built for different platforms (operating systems and CPU architectures). This is increasingly important because:

**Why cross-platform builds matter:**
- 🍎 **Apple Silicon Macs** (M1, M2, M3, M4) use ARM64 architecture
- 💻 **Most Intel/AMD computers** use AMD64 (x86_64) architecture
- ☁️ **Cloud servers** might use different architectures than your laptop
- 🤝 **Team collaboration**: Your teammates might have different machines

**The problem:**
If you build an image on your Mac M1 (ARM64), it might not run on your colleague's Intel laptop (AMD64) or on your production server!

**Example scenario:**
```bash
# You build on Mac M1
docker build -t my-app .

# Your teammate on Intel Mac tries to run it
docker run my-app
# Warning: The requested image's platform (linux/arm64) does not match
# the detected host platform (linux/amd64)
```

**Solution: Multi-platform builds**

Docker Buildx allows building for multiple platforms at once:

```bash
# Build for both ARM64 and AMD64
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .

# Or build for a specific platform
docker buildx build --platform linux/amd64 -t my-app .
```

**Common platforms:**
- `linux/amd64` - Intel/AMD processors (most servers and older Macs)
- `linux/arm64` - Apple Silicon Macs, some cloud instances
- `linux/arm/v7` - Raspberry Pi and other ARM devices

**When do you need this?**
- ✅ **Sharing images** with teammates on different machines
- ✅ **Deploying to cloud** servers with different architectures
- ✅ **Publishing to Docker Hub** for others to use
- ✅ **Working on Apple Silicon** but deploying to AMD64 servers



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

### 💡 Understanding CMD vs ENTRYPOINT

Both `CMD` and `ENTRYPOINT` define what command runs when a container starts, but they work differently. Understanding this helps you create more flexible containers.

**CMD - The Default Command (Easy to Override)**

`CMD` provides default arguments that can be **easily overridden** when you run the container:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

```bash
# Runs python app.py (uses CMD)
docker run my-app

# Override CMD - runs bash instead
docker run -it my-app bash

# Override CMD - runs a different script
docker run my-app python another_script.py
```

**ENTRYPOINT - The Fixed Command (Harder to Override)**

`ENTRYPOINT` sets a **fixed command** that will always run. Arguments you pass become additional parameters:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
ENTRYPOINT ["python"]
CMD ["app.py"]
```

```bash
# Runs: python app.py
docker run my-app

# Runs: python another_script.py (CMD is overridden)
docker run my-app another_script.py

# To override ENTRYPOINT, you need --entrypoint flag
docker run --entrypoint bash my-app
```

**When to Use What?**

| Use Case | Instruction | Example |
|----------|-------------|---------|
| **Application container** (one purpose) | `ENTRYPOINT` | Web server, database |
| **Flexible container** (multiple uses) | `CMD` | Development image, utilities |
| **Best of both** | `ENTRYPOINT` + `CMD` | ENTRYPOINT=command, CMD=default args |

**Example 1: Web Server (Use ENTRYPOINT)**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# ENTRYPOINT ensures uvicorn always runs
# CMD provides default arguments that can be overridden
ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Runs: uvicorn app:app --host 0.0.0.0 --port 8000
docker run my-app

# Runs: uvicorn app:app --host 0.0.0.0 --port 8080 --reload
# (Overrides CMD with different port and reload flag)
docker run my-app app:app --host 0.0.0.0 --port 8080 --reload
```

**Example 2: Utility Container (Use CMD)**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .

# CMD makes it easy to run different things
CMD ["python", "--version"]
```

```bash
# Runs: python --version
docker run my-app

# Runs: python my_script.py (completely overrides CMD)
docker run my-app python my_script.py

# Runs: bash (for debugging)
docker run -it my-app bash
```

**Example 3: CLI Tool (Use ENTRYPOINT + CMD)**
```dockerfile
FROM alpine:latest

# Install a tool (e.g., curl)
RUN apk add --no-cache curl

# ENTRYPOINT sets the main command
ENTRYPOINT ["curl"]

# CMD provides default flags
CMD ["--help"]
```

```bash
# Runs: curl --help
docker run my-curl

# Runs: curl https://example.com
docker run my-curl https://example.com

# Runs: curl -I https://example.com (get headers only)
docker run my-curl -I https://example.com
```

**Key Differences Summary:**

| Feature | CMD | ENTRYPOINT |
|---------|-----|------------|
| **Purpose** | Default command/args | Main executable |
| **Override** | Easy (`docker run image <command>`) | Requires `--entrypoint` flag |
| **Best for** | Flexible containers | Single-purpose containers |
| **Combined** | Provides default args to ENTRYPOINT | Sets the main command |

**Pro Tip:** Many production images use both:
- `ENTRYPOINT` = the program that should always run
- `CMD` = default arguments that users can easily override

This pattern gives you the best of both worlds: a clear purpose with flexibility!

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
