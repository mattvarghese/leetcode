# 1. Stop and remove containers and internal Docker volumes
docker compose down -v

# 2. Delete the protected data folders (requires escalation)
sudo rm -rf ./data
