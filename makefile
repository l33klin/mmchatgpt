deploy: docker-compose.yaml
	docker compose -p mmchatgpt up -d

down: docker-compose.yaml
	docker compose -p mmchatgpt down

rebuild: docker-compose.yaml
	mv .env.crissielee .env
	docker compose -p mmchatgpt up -d --build --force-recreate

deploy_chatter: docker-compose.yaml
	docker compose -p mmchatgpt_chatter up -d

down_chatter: docker-compose.yaml
	docker compose -p mmchatgpt_chatter down

rebuild_chatter: docker-compose.yaml
	mv .env.chatgpt-bot .env
	docker compose -p mmchatgpt_chatter up -d --build --force-recreate
