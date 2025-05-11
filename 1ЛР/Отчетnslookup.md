## Отчет по работе утилиты nslookup
nslookup  - это утилита для запросов к DNS-серверам, которая позволяет:
1.	Получать IP-адреса по доменным именам (прямые запросы)
2.	Определять доменные имена по IP-адресам (обратные запросы)
3.	Проверять работу DNS-серверов
4.	Анализировать MX-записи (почтовые серверы)
5.	Исследовать другие типы DNS-записей (NS, SOA, TXT и др.)

## Результаты выполнения
Server:  192.168.50.1
Address: 192.168.50.1#53
Non-authoritative answer:
Name: example.com
Address: 96.7.128.175
Name: example.com
Address: 96.7.128.198
Name: example.com
Address: 23.215.0.136
Name: example.com
Address: 23.192.228.84
Name: example.com
Address: 23.215.0.138
Name: example.com
Address: 23.192.228.80
Name: example.com
Address: 2600:1406:bc00:53::b81e:94c8
Name: example.com
Address: 2600:1406:bc00:53::b81e:94ce
Name: example.com
Address: 2600:1406:3a00:21::173e:2e66
Name: example.com
Address: 2600:1406:3a00:21::173e:2e65
Name: example.com
Address: 2600:1408:ec00:36::1736:7f31
Name: example.com
Address: 2600:1408:ec00:36::1736:7f24
## Анализ результатов
## Основные данные:
DNS-сервер:
·	Локальный кэширующий: 192.168.50.1 (роутер)
·	Порт: 53 
·	IPv4 :96.7.128.175/198, 23.215.0.136/138, 23.192.228.80/84
·	IPv6 :2600:1406:bc00:53::..., 2600:1408:ec00:36::...
