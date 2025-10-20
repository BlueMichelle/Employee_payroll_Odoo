#!/bin/bash

# Database backup script for Odoo
# Usage: docker-compose exec ubuntu bash /scripts/backup_db.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/scripts/backups"
DB_NAME="odoo"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create database backup
echo "Creating database backup..."
pg_dump -h postgres -U odoo -d $DB_NAME > $BACKUP_DIR/odoo_backup_$DATE.sql

if [ $? -eq 0 ]; then
    echo "Backup created successfully: $BACKUP_DIR/odoo_backup_$DATE.sql"
else
    echo "Backup failed!"
    exit 1
fi

# Compress the backup
gzip $BACKUP_DIR/odoo_backup_$DATE.sql

if [ $? -eq 0 ]; then
    echo "Backup compressed: $BACKUP_DIR/odoo_backup_$DATE.sql.gz"
else
    echo "Compression failed!"
fi

# Clean up old backups (keep last 5)
echo "Cleaning up old backups..."
cd $BACKUP_DIR
ls -t odoo_backup_*.sql.gz | tail -n +6 | xargs rm -f

echo "Database backup completed!"