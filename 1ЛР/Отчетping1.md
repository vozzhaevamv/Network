# Отчет по работе утилиты ping
Утилита ping является одним из базовых инструментов сетевой диагностики, используемым для проверки доступности узлов в IP-сетях. Она работает по протоколу ICMP, отправляя пакеты на указанный адрес и измеряя время до получения ответа. Основные задачи ping включают проверку связи с удаленным хостом, измерение времени отклика и выявление потерь пакетов.

## Результаты выполнения
Результаты выполнения
PING example.com (23.192.228.80) 56(84) bytes of data.
64 bytes from a23-192-228-80.deploy.static.akamaitechnologies.com (23.192.228.80): icmp_seq=1 ttl=45 time=309 ms
64 bytes from a23-192-228-80.deploy.static.akamaitechnologies.com (23.192.228.80): icmp_seq=2 ttl=45 time=259 ms
64 bytes from a23-192-228-80.deploy.static.akamaitechnologies.com (23.192.228.80): icmp_seq=3 ttl=45 time=356 ms
64 bytes from a23-192-228-80.deploy.static.akamaitechnologies.com (23.192.228.80): icmp_seq=4 ttl=45 time=276 ms
64 bytes from a23-192-228-80.deploy.static.akamaitechnologies.com (23.192.228.80): icmp_seq=5 ttl=45 time=299 ms
## Анализ результатов

### Доступность узла:
- Узел example.com доступен
- IP-адрес: 23.192.228.80
- Хост принадлежит Akamai Technologies
- Среднее время отклика: 299.679 мс
- Минимальное время: 258.668 мс
- Максимальное время: 355.678 мс
- Отклонение (mdev): 32.984 мс

### TTL (Time To Live):
- TTL=45
