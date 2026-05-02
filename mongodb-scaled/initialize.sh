#!/bin/bash
set -e # Exit immediately if a command fails

echo "Preparing data directory structure..."
mkdir -p data/{config01,config02,config03,shard1a,shard1b,shard2a,shard2b,shard3a,shard3b}

echo "Starting containers..."
docker compose up -d

echo "Waiting for containers to be reachable (20s)..."
sleep 20

echo "Initializing Config Server Replica Set..."
docker exec configsvr01 mongosh --quiet --eval '
  rs.initiate({
    _id: "cfgrs", 
    configsvr: true, 
    members: [
      {_id: 0, host: "configsvr01:27017"}, 
      {_id: 1, host: "configsvr02:27017"}, 
      {_id: 2, host: "configsvr03:27017"}
    ]
  })'

# CRITICAL: Wait for Config Server to elect a Primary before shards try to talk to it
echo "Waiting for Config Server Primary election..."
until docker exec configsvr01 mongosh --quiet --eval "rs.status().ok" | grep -q "1"; do
  sleep 2
done

echo "Initializing Shard Replica Sets..."
# We can run these in parallel or sequence; sequence is safer for debugging
for i in 1 2 3; do
  echo "Initializing Shard $i..."
  docker exec shard${i}a mongosh --quiet --eval "
    rs.initiate({
      _id: 'shard${i}rs', 
      members: [
        {_id: 0, host: 'shard${i}a:27017'}, 
        {_id: 1, host: 'shard${i}b:27017'}
      ]
    })"
done

echo "Waiting for Shard Primaries to be elected..."
sleep 15

echo "Adding shards to the cluster..."
for i in 1 2 3; do
  # We use --quiet and check for ok: 1 without strict quote requirements
  until docker exec mongos mongosh --port 27017 --quiet --eval "sh.addShard('shard${i}rs/shard${i}a:27017,shard${i}b:27017')" | grep -E "ok: 1|\"ok\": 1"; do
    echo "Waiting for Shard $i to be ready for joining..."
    # Debug: Print the actual output if it fails
    docker exec mongos mongosh --port 27017 --quiet --eval "sh.addShard('shard${i}rs/shard${i}a:27017,shard${i}b:27017')"
    sleep 5
  done
  echo "Shard $i added successfully."
done

echo "Finalizing Cluster Configuration..."
docker exec mongos mongosh --quiet --eval 'sh.enableSharding("practice_db")'

echo "------------------------------------------------"
echo "Cluster is ready! Status:"
docker exec mongos mongosh --quiet --eval "sh.status()"
