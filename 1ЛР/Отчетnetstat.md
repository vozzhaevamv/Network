## Отчет по работе утилиты nestat
netstat — это утилита командной строки, которая отображает различную информацию, связанную с сетью, включая:
·	Сетевые соединения (как входящие, так и исходящие)
·	Таблицы маршрутизации
·	Статистику сетевых интерфейсов
·	Соединения маскировки
·	Членство в мультикастах
·	Статистику протоколов
## Результаты выполнения
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 debian:51804            93.243.107.34.bc.:https ESTABLISHED
tcp        0      0 debian:58382            47.91.78.155:https      TIME_WAIT  
tcp        0      0 debian:51322            47.246.133.115:https    ESTABLISHED
tcp        0      0 debian:49216            47.91.78.155:https      ESTABLISHED
tcp        0      0 debian:47136            onlyoffice.disk.y:https ESTABLISHED
tcp        0      0 debian:39406            149.154.167.99:https    ESTABLISHED
tcp        0      0 debian:45520            149.154.167.99:https    ESTABLISHED
tcp        0      0 debian:51278            47.91.78.155:https      TIME_WAIT  
tcp        0      0 debian:37702            162.159.61.4:https      ESTABLISHED
tcp        0      0 debian:50740            149.154.167.99:https    ESTABLISHED
tcp        0      0 debian:41204            xiva-daria.stable:https ESTABLISHED
tcp        0      0 debian:41188            xiva-daria.stable:https ESTABLISHED
tcp        0      0 debian:58960            ec2-35-174-127-31:https ESTABLISHED
## Анализ результатов
Основные данные:
 - Всего соединений: 13 (10 ESTABLISHED, 2 TIME_WAIT)
 - 92% трафика - HTTPS (порт 443)
