# Odoo Docker Project

A complete Docker setup for Odoo ERP with PostgreSQL database and pgAdmin for database management, plus an Ubuntu utility container.

## Services

- **Odoo 17**: ERP application accessible at http://localhost:8069
- **PostgreSQL 15**: Database server on port 5432
- **pgAdmin 4**: Database management tool at http://localhost:8080
- **Ubuntu 22.04**: Utility container for debugging and scripts

## Quick Start

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd odoo-docker-project
   ```

2. Start all services:
   ```bash
   docker-compose up -d
   ```

3. Access the applications:
   - **Odoo**: http://localhost:8069
   - **pgAdmin**: http://localhost:8080

## Configuration

### Environment Variables

Copy and modify `.env` file to customize:

- `POSTGRES_DB`: Database name (default: odoo)
- `POSTGRES_USER`: Database user (default: odoo)
- `POSTGRES_PASSWORD`: Database password (default: odoo123)
- `PGADMIN_EMAIL`: pgAdmin login email (default: admin@example.com)
- `PGADMIN_PASSWORD`: pgAdmin login password (default: admin123)

### Default Credentials

**pgAdmin Login:**
- Email: admin@example.com
- Password: admin123

**Database Connection in pgAdmin:**
- Host: postgres
- Port: 5432
- Database: odoo
- Username: odoo
- Password: odoo123

## Directory Structure

```
odoo-docker-project/
├── docker-compose.yml    # Main Docker Compose configuration
├── .env                 # Environment variables
├── config/              # Odoo configuration files
├── addons/              # Custom Odoo addons
├── scripts/             # Utility scripts for Ubuntu container
└── README.md           # This file
```

## Usage

### Starting Services
```bash
# Start all services in background
docker-compose up -d

# Start services with logs
docker-compose up

# Start specific service
docker-compose up odoo
```

### Stopping Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (WARNING: This will delete data!)
docker-compose down -v
```

### Viewing Logs
```bash
# View logs for all services
docker-compose logs

# View logs for specific service
docker-compose logs odoo
docker-compose logs postgres
docker-compose logs pgadmin

# Follow logs in real-time
docker-compose logs -f odoo
```

### Database Management

1. Open pgAdmin at http://localhost:8080
2. Login with configured credentials
3. Add server with these settings:
   - Name: Odoo Database
   - Host: postgres
   - Port: 5432
   - Database: odoo
   - Username: odoo
   - Password: odoo123

### Ubuntu Utility Container

Access the Ubuntu container for debugging or running scripts:

```bash
# Execute bash in Ubuntu container
docker-compose exec ubuntu bash

# Run commands directly
docker-compose exec ubuntu ls /scripts
```

## Customization

### Adding Odoo Addons

1. Place your custom addons in the `addons/` directory
2. Restart Odoo service:
   ```bash
   docker-compose restart odoo
   ```

### Odoo Configuration

1. Add configuration files to the `config/` directory
2. Restart Odoo service to apply changes

### Scripts

Add utility scripts to the `scripts/` directory to use with the Ubuntu container.

## Troubleshooting

### Port Conflicts
If ports 8069, 8080, or 5432 are already in use, modify the port mappings in `docker-compose.yml`:

```yaml
ports:
  - "8070:8069"  # Change host port
```

### Database Issues
If you encounter database connection issues:

1. Check if PostgreSQL container is running:
   ```bash
   docker-compose ps postgres
   ```

2. View PostgreSQL logs:
   ```bash
   docker-compose logs postgres
   ```

### Reset Database
To start with a fresh database:

```bash
docker-compose down -v
docker-compose up -d
```

## Development

This setup is designed for development purposes. For production use:

1. Change default passwords in `.env`
2. Use proper SSL certificates
3. Configure backup strategies
4. Review security settings