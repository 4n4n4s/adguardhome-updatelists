#!/bin/bash
# Set default cinterval to 86400 seconds if not provided (1 day)
if [ -z "$INTERVAL_SECONDS" ]; then
    INTERVAL_SECONDS=86400
fi

if [ -z "$USERNAME" ]; then
    USERNAME="admin"
fi

if [ -z "$PASSWORD" ]; then
    PASSWORD="admin"
fi

echo "Starting in 30 seconds..."
sleep 30

while true; do
    echo "Starting task"
    python3 main.py --adguard_url $ADGUARD_URL --username $USERNAME --password $PASSWORD --adlist_url $ADLIST_URL
    echo "Sleeping for $INTERVAL_SECONDS seconds..."
    sleep $INTERVAL_SECONDS
done