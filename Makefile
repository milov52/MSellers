up:
	docker compose -f docker-compose-dev.yml up -d

down:
	docker compose -f docker-compose-dev.yml down && docker network prune --force