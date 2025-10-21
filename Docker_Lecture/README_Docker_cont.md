# Docker Tutorial - Introduction for Beginners (Continued)

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

**Why is running as root dangerous?**

By default, containers run as the `root` user (user ID 0), which has full administrative privileges. This creates several security risks:

**🚨 Security Risks:**
1. **Container Escape**: If an attacker finds a vulnerability in your application or Docker itself, they could potentially escape the container with root privileges
2. **Host System Access**: A compromised container running as root has more potential to affect the host system
3. **File System Damage**: If your application has a bug, it could accidentally modify or delete critical files
4. **Privilege Escalation**: Malicious code could exploit root access to gain control over the entire system

**Real-world scenario:**
```bash
# Running as root (BAD)
docker run -v /:/host ubuntu
# Inside container: You're root! You could accidentally run:
# rm -rf /host/*  # This would delete files on your HOST machine!
```

**The principle of least privilege:**
Your application should run with the **minimum permissions** needed to do its job. Most web applications don't need root access - they just need to:
- Read their own code files
- Write to log files
- Listen on a network port (ports > 1024 don't require root)

**Benefits of running as non-root:**
- ✅ **Better security**: Limits damage if container is compromised
- ✅ **Prevents accidents**: Can't accidentally delete system files
- ✅ **Industry standard**: Required by many security policies and Kubernetes clusters
- ✅ **Defense in depth**: One more security layer protecting your system

**Dockerfile (with non-root user)**
```dockerfile
FROM python:3.11-slim

# Create non-root user with specific UID
# -m creates home directory, -u sets user ID
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Install dependencies as root (needed for system packages)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Change ownership of application files to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user for running the application
# Everything after this line runs as 'appuser', not root
USER appuser

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**What's happening:**
1. **Line 4-5**: Create a user called `appuser` with UID 1000 (standard for first user)
2. **Lines 7-11**: Still running as root to install dependencies (needed for system-level operations)
3. **Line 17**: Change file ownership so `appuser` can read/write application files
4. **Line 21**: Switch to `appuser` - from here on, everything runs as non-root
5. **Line 23**: The application process runs as `appuser`, not root

**Verify it's working:**
```bash
# Build and run your container
docker build -t my-secure-app .
docker run -it my-secure-app bash

# Inside container, check who you are:
whoami
# Output: appuser (not root!)

id
# Output: uid=1000(appuser) gid=1000(appuser)
```

**Common gotcha - File permissions with volumes:**
When using bind mounts, you might encounter permission issues. The non-root user inside the container needs access to mounted files:

```bash
# If you get "Permission Denied" errors with volumes:
# Option 1: Match the container UID to your host user
RUN useradd -m -u $(id -u) appuser

# Option 2: On your host, give permissions to the directory
chmod -R 755 ./app-data
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

## Part 11: Docker Pricing and Enterprise Alternatives

As you move from learning to production use, it's important to understand Docker's licensing and the alternatives available, especially for enterprise environments.

### Docker Pricing Overview (2024)

Docker offers several pricing tiers:

| Plan | Price | Target Users | Key Features |
|------|-------|--------------|--------------|
| **Docker Personal** | Free | Individual developers, students, educators, open source | Unlimited public repos, 1 private repo, Docker Desktop |
| **Docker Pro** | $9/month | Professional developers | Unlimited private repos, parallel builds, vulnerability scanning |
| **Docker Team** | $15/user/month | Small teams | Team management, advanced image management, SSO |
| **Docker Business** | $24/user/month | Enterprises | Centralized management, security scanning, support SLA |

**Important notes:**
- **Docker Desktop** requires a paid license for companies with more than 250 employees OR more than $10M in annual revenue
- **Docker Engine** (command-line tool on Linux) remains free and open source
- **For students**: You're covered by the free Personal plan for learning and non-commercial use

**What's included in the free tier:**
- ✅ Docker Desktop for personal use
- ✅ Docker Hub (with limits: 1 private repository, unlimited public)
- ✅ Command-line tools (docker, docker-compose)
- ✅ All the features covered in this tutorial

**What requires a paid license:**
- ❌ Docker Desktop in companies meeting the size criteria mentioned above
- ❌ Advanced security scanning and vulnerability detection
- ❌ Enhanced support and SLAs
- ❌ Team collaboration features (SSO, centralized billing)

### Enterprise Alternatives to Docker

For companies looking for alternatives to Docker (for licensing, support, or technical reasons), several options exist:

#### 1. Podman - The Drop-In Replacement

**What is Podman?**
- Developed by Red Hat
- Designed as a **daemonless** alternative to Docker
- Nearly 100% compatible with Docker commands
- **Completely free and open source**

**Key differences from Docker:**
- No daemon required (more secure)
- Rootless containers by default (better security)
- Compatible with Docker images and Dockerfiles
- Pods support (Kubernetes-style pod management)

**Example - Same commands work:**
```bash
# Docker command
docker run -it python:3.11-slim bash

# Podman equivalent (usually identical!)
podman run -it python:3.11-slim bash

# Docker Compose equivalent
podman-compose up -d
```

**When to use Podman:**
- ✅ Enterprise Linux environments (RHEL, CentOS, Fedora)
- ✅ Need for rootless containers
- ✅ Want to avoid Docker licensing fees
- ✅ Security-focused organizations
- ✅ Kubernetes-native workflows

**Migration effort:** Very low - most Docker commands work with minimal changes

#### 2. containerd - The Underlying Engine

**What is containerd?**
- The core container runtime that Docker itself uses
- Industry-standard, maintained by Cloud Native Computing Foundation (CNCF)
- Used by Kubernetes as its default container runtime
- **Completely free and open source**

**Key characteristics:**
- Lower-level than Docker (fewer built-in features)
- Very stable and production-ready
- What Kubernetes uses under the hood
- No built-in image build capabilities (needs buildkit)

**When to use containerd:**
- ✅ Kubernetes environments
- ✅ Minimal runtime overhead needed
- ✅ Cloud-native infrastructure
- ✅ When you don't need Docker's high-level features

**Note:** containerd is more technical and less user-friendly than Docker Desktop

#### 3. Rancher Desktop - The User-Friendly Alternative

**What is Rancher Desktop?**
- Open-source alternative to Docker Desktop
- Provides a GUI similar to Docker Desktop
- Works on Windows, Mac, and Linux
- **Completely free and open source**

**Key features:**
- Container management with containerd or Moby (Docker)
- Built-in Kubernetes cluster
- Compatible with docker and kubectl commands
- No licensing restrictions

**When to use Rancher Desktop:**
- ✅ Need a free Docker Desktop alternative
- ✅ Want Kubernetes integration
- ✅ Enterprise use without licensing costs
- ✅ Cross-platform development teams

**Great for:** Companies that want Docker Desktop functionality without the licensing fees

## Additional Resources

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
- [Play with Docker](https://labs.play-with-docker.com/) - Online Docker playground
- [Podman Documentation](https://podman.io/)
- [containerd Documentation](https://containerd.io/)
- [Rancher Desktop](https://rancherdesktop.io/)

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