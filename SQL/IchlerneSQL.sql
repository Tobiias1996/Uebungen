USE sql_store; -- Datensatz der genutzt wird

SELECT  -- was davon ausgewählt werden soll (* =alles)
	first_name, 
    last_name, 
    points, 
    points + 10 AS 'points II',  -- mit (hier) points + 10 wird gerechner 
    points +10 * 2 AS 'points III', -- Points + 20
    (points +10) * 2  AS 'points IVorders',-- Points +10 * 2, AS = Alias
	state,
    birth_date,
    customer_id,
    phone
FROM customers	-- von welcher Tabelle
-- WHERE points >1000 -- Zeigt nur Leute an, die mehr als 1.000 points haben
-- Andere Möglichkeiten:
-- >= , <, <=, =, != (ungleich)
--  WHERE state='VA' -- Zeigt nur Leute aus VA an
-- WHERE state!='VA' -- Zeigt nur Leute an, die nicht aus VA kommen
-- WHERE birth_date>'1990-10-13' OR 
				-- (points > 1000 AND state='CO') -- And, OR --> Selbsterklärend AND>OR
-- WHERE NOT  points<1500 -- Selbsterklärend
-- WHERE order_id=6 AND unit_price*quantity>30 -- komplexe Rechnung möglich
-- WHERE state  IN ("VA", "CO", "TX") -- mehrere Sachen in einem string, funzt auch mit WHERE NOT
-- WHERE points BETWEEN 1000 AND 5000 -- leicher als points>1000 AND points<5000
-- WHERE last_name LIKE "b%" -- zeigt jeden an, dessen Namen mit "b" beginnt, "%b%" -- zeigt jeden an, bei dem ein b im Namen steht       NOT LIKE gibts auch
-- WHERE last_name LIKE "_____y" -- zeigt jeden an, dessen Name aus 6 Buchstaben besteht und der letzte muss ein y sein, b____y --> b 4 egale Buchstaben y
-- WHERE first_name LIKE "i%" OR last_name LIKE "b%"
-- WHERE last_name REGEXP "field" (muss im Namen sein), ^field (muss am Anfang stehen), field$ (muss am Ende stehen), field|mac (sucht nach mehreren)
-- WHERE last_name REGEXP " [gim]e" -- jeder, der ge, ie oder me im Namen hat   Buchstabenreihe: "[a-h]e"
-- WHERE phone IS NULL (Um nicht erfasste Daten zu finden)
-- ORDER BY first_name, state -- nach Namen sortiert
-- LIMIT Zahl -- selbsterklärend



	