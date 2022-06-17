USE sql_store; -- Datensatz der genutzt wird

SELECT  -- was davon ausgewählt werden soll (* =alles)
	first_name, 
    last_name, 
    points, 
    points + 10 AS 'points II',  -- mit (hier) points + 10 wird gerechner 
    points +10 * 2 AS 'points III', -- Points + 20
    (points +10) * 2  AS 'points IVorders',-- Points +10 * 2, AS = Alias
	state
FROM customers	-- von welcher Tabelle
-- WHERE points >1000 -- Zeigt nur Leute an, die mehr als 1.000 points haben
-- Andere Möglichkeiten:
-- >= , <, <=, =, != (ungleich)
--  WHERE state='VA' -- Zeigt nur Leute aus VA an
-- WHERE state!='VA' -- Zeigt nur Leute an, die nicht aus VA kommen