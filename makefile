deploy: docker-compose.yaml
	docker compose -p mmchatgpt up -d

down: docker-compose.yaml
	docker compose -p mmchatgpt down

rebuild: docker-compose.yaml
	docker compose -p mmchatgpt up -d --build --force-recreate
