
7. Write Prometheus exporter in Python/Golang that connects to specified RabbitMQ HTTP API (it's in the management plugin) and periodically reads the following information about all queues in all vhosts:
    >Install libs: `pip install -f ./requirements.txt`

    `rabbitmq_exporter.py`

8. Write a script to restart the Laravel backend service if CPU usage exceeds 80%.
    > `./restart_laravel_on_high_cpu.sh`

9. A Postgres query is running slower than expected. Explain your approach to
troubleshooting it.
    > EXPLAIN ANALYZE, check VACUUM running, Disk space, IO, missed INDEX, pg_stat_activity