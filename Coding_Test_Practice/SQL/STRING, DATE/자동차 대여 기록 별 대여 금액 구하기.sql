-- 코드를 입력하세요
SELECT 
    H.HISTORY_ID, 
    CASE
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) >= 90 THEN 
            ROUND(C.DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1) * 
            (100 - (SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                    WHERE DURATION_TYPE LIKE '90%' 
                    AND CAR_TYPE = '트럭')) / 100, 0)
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) >= 30 THEN 
            ROUND(C.DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1) * 
            (100 - (SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                    WHERE DURATION_TYPE LIKE '30%' 
                    AND CAR_TYPE = '트럭')) / 100, 0)
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) >= 7 THEN 
            ROUND(C.DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1) * 
            (100 - (SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                    WHERE DURATION_TYPE LIKE '7%' 
                    AND CAR_TYPE = '트럭')) / 100, 0)
        ELSE 
            C.DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1)
    END AS FEE
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
JOIN 
    (SELECT CAR_ID, DAILY_FEE 
     FROM CAR_RENTAL_COMPANY_CAR 
     WHERE CAR_TYPE = '트럭') AS C 
ON H.CAR_ID = C.CAR_ID
ORDER BY 
    FEE DESC, 
    HISTORY_ID DESC;