# migrate_permissions.py
import sqlite3

conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

new_columns = [
    'can_create_racking',
    'can_create_stock',
    'can_create_order',
    'can_transfer_stock',
    'can_transfer_batch',
    'can_mass_transfer',
    'can_bulk_transfer',
    'can_add_sku',
    'can_view_orders',   # ← new
    'can_cycle_count',   # ← new
]

for col in new_columns:
    try:
        cursor.execute(f'ALTER TABLE users ADD COLUMN {col} BOOLEAN DEFAULT 0')
        print(f'✅ Added: {col}')
    except sqlite3.OperationalError as e:
        print(f'⚠️  Skipped {col}: {e}')

conn.commit()
conn.close()
print('Done.')