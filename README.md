# Задание 1
SELECT c.login, COUNT(o.id)
    FROM "Couriers" AS c
    LEFT JOIN "Orders" AS o ON c.id = o."courierId"
    WHERE o."inDelivery" = true
    GROUP BY c.login;

# Задание 2
SELECT   
    track,  
    CASE   
        WHEN finished = TRUE THEN 2  
        WHEN cancelled = TRUE THEN -1  
        WHEN “inDelivery” = TRUE THEN 1  
        ELSE 0  
    END AS status  
FROM “Orders”;

# Задание 3
# Тест на проверку создания заказа на самокат и статуса заказа в Яндекс.Самокат с помощью API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest