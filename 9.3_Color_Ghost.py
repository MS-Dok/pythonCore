select LASTNAME,FIRSTNAME from CUSTOMERS 
where ID in (select ID_CUSTOMER from orders 
            where ID_CUSTOMER is not NULL 
            group by ID_CUSTOMER  
            order by sum(AMOUNT*PRODUCT_PRICE) 
            desc limit 3)
            order by FIRSTNAME,LASTNAME;