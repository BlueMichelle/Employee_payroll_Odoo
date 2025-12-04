# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Docker-based Odoo 17 ERP development environment with PostgreSQL database, pgAdmin for database management, and an Ubuntu utility container for debugging and scripts.

## Common Commands

### Development Workflow
```bash
# Start all services (recommended for development)
docker-compose up -d

# View logs in real-time
docker-compose logs -f odoo

# Restart Odoo after config/addon changes
docker-compose restart odoo

# Stop all services
docker-compose down

# Reset database and volumes (destructive)
docker-compose down -v && docker-compose up -d
```

### Database Operations
```bash
# Access database via pgAdmin
# Navigate to http://localhost:8080 (admin@example.com / admin123)

# Create database backup
docker-compose exec ubuntu bash /scripts/backup_db.sh

# Access PostgreSQL directly
docker-compose exec postgres psql -U odoo -d odoo

# View database logs
docker-compose logs postgres
```

### Debugging and Development
```bash
# Access Ubuntu utility container
docker-compose exec ubuntu bash

# Execute commands in containers
docker-compose exec odoo bash
docker-compose exec postgres bash

# View service status
docker-compose ps

# View specific service logs
docker-compose logs [odoo|postgres|pgadmin|ubuntu]
```

### Testing Custom Addons
```bash
# After adding addons to ./addons/ directory
docker-compose restart odoo

# Access Odoo at http://localhost:8069 to install/test addons
# Apps menu -> Update Apps List -> Install custom modules
```

## Architecture

### Service Architecture
The project uses a multi-container Docker setup with these interconnected services:

- **odoo**: Main ERP application (port 8069)
- **postgres**: Database backend (port 5432) 
- **pgadmin**: Web-based database management (port 8080)
- **ubuntu**: Utility container for scripts and debugging

All services communicate through the `odoo_network` Docker network.

### Volume Structure
- `postgres_data`: PostgreSQL data persistence
- `odoo_web_data`: Odoo application data
- `pgadmin_data`: pgAdmin configuration
- `./config`: Odoo configuration files (mounted)
- `./addons`: Custom Odoo addons (mounted)
- `./scripts`: Utility scripts for Ubuntu container (mounted)

### Configuration Management
- `.env`: Environment variables for database credentials and pgAdmin
- `config/odoo.conf`: Odoo server configuration with database connection, performance settings, and addon paths
- `docker-compose.yml`: Service definitions, networking, and volume mounts

## Development Guidelines

### Adding Custom Addons
1. Place addon directories in `./addons/`
2. Restart Odoo: `docker-compose restart odoo`
3. Update apps list in Odoo interface
4. Install/test the custom addon

### Configuration Changes
- Odoo config: Edit `config/odoo.conf`, then `docker-compose restart odoo`
- Environment variables: Edit `.env`, then `docker-compose up -d`
- Docker services: Edit `docker-compose.yml`, then `docker-compose up -d`

### Database Management
- Use pgAdmin at http://localhost:8080 for GUI management
- Connection settings: host=postgres, port=5432, db=odoo, user=odoo
- Backup script available at `/scripts/backup_db.sh` in Ubuntu container
- Direct SQL access via `docker-compose exec postgres psql -U odoo -d odoo`

### Troubleshooting
- Port conflicts: Modify port mappings in `docker-compose.yml`
- Database issues: Check `docker-compose logs postgres`
- Odoo startup problems: Check `docker-compose logs odoo`
- Fresh start: Use `docker-compose down -v` to reset all data

## Access Points

- **Odoo ERP**: http://localhost:8069
- **pgAdmin**: http://localhost:8080 (admin@example.com / admin123)
- **PostgreSQL**: localhost:5432 (odoo / odoo123)

## Important Files

- `docker-compose.yml`: Main orchestration file
- `.env`: Environment variables (contains sensitive data)
- `config/odoo.conf`: Odoo server configuration
- `scripts/backup_db.sh`: Database backup utility
- `addons/`: Directory for custom Odoo addons (currently empty)
