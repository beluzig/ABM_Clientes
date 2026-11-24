DROP TRIGGER IF EXISTS tr_customers_before ON customers;
DROP TRIGGER IF EXISTS tr_customers_del ON customers;

DROP FUNCTION IF EXISTS tr_valid_customer();
DROP FUNCTION IF EXISTS tr_delete_customer();
DROP FUNCTION IF EXISTS fn_abm_cli(
    text, text, text, text, text, text, text, text, text, text, text, text
);

DROP VIEW IF EXISTS vw_ordenes;

--Funcion ABM 
create or replace function fn_abm_cli(
	accion text, 
    id text, 
    nombre text, 
    contacto text,
    titulo text,
    direccion text,
    ciudad text, 
    p_region text,
    codp text,
    pais text,
    telefono text,
    p_fax text
)
returns text as $$
begin
	if accion not in ('A','M','B') then
		raise exception 'Accion invalida: %',accion;
	end if;
	
	if accion in ('A','M') and id is not null and length(trim(id))>5 then
		raise exception 'El ID del CLIENTE debe tener exactamente 5 letras';
	end if;
	
	if accion = 'A' then
		RAISE NOTICE 'SQL_LOG: %',
      format(
        'INSERT INTO customers(customerid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax) VALUES (%L, %L, %L, %L, %L, %L, %L, %L, %L, %L, %L)',
        id, nombre, contacto, titulo, direccion, ciudad,
        p_region, codp, pais, telefono, p_fax
      );
		insert into customers(customerid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax)
		values(id,nombre,contacto,titulo,direccion,ciudad,p_region,codp,pais,telefono,p_fax);
		return 'El cliente se creo correctamente.';
	elsif accion = 'M' then
	  RAISE NOTICE 'SQL_LOG: %',
      format(
        'UPDATE customers SET companyname = %L, contactname = %L, contacttitle = %L, address = %L, city = %L, region = %L, postalcode = %L, country = %L, phone = %L, fax = %L WHERE customerid = %L',
        nombre, contacto, titulo, direccion, ciudad,
        p_region, codp, pais, telefono, p_fax, id
      );
		update customers
		SET companyname = nombre, contactname = contacto, contacttitle = titulo, address = direccion, city = ciudad, region = p_region, postalcode = codp, country = pais, phone = telefono, fax = p_fax
		where customerid = id;
		return 'Cliente actualizado exitosamente.';
	elsif accion = 'B' then
		RAISE NOTICE 'SQL_LOG: %',
      format(
        'DELETE FROM customers WHERE customerid = %L',
        id
      );
		delete from customers
		where customerid = id;
		return 'Cliente eliminado correctamente';
	end if;
end;
$$
language plpgsql;

create or replace function tr_valid_customer()
returns trigger as $$ 
begin

	if TG_OP = 'INSERT' then
		RAISE NOTICE 'SQL_LOG: %',
      format(
        'SELECT 1 FROM customers WHERE customerid = %L',
        NEW.customerid
      );

		if exists (
			select 1 
			from customers 
			where customerid = new.customerid
		) then
			raise exception 'Ya existe un cliente con el ID %.', new.customerid;
    	end if;
	end if;

	if length(trim(new.customerid)) <> 5 then
        RAISE EXCEPTION 'El ID del cliente debe tener exactamente 5 letras';
    end if;

	if new.customerid is null or trim(new.customerid)='' then
		raise exception 'El ID es obligatorio';
	end if;
	
	if new.companyname is null or trim(new.companyname) = '' then
		raise exception 'El nombre de la empresa es obligatorio';
	end if;
	
	if trim(new.customerid) !~ '^[a-zA-Z]+$' then
		raise exception 'El ID debe contener únicamente letras';
	end if;
	
	if new.customerid <> upper(new.customerid) then
    	raise exception 'El ID debe estar en mayúsculas';
	END IF;   
	
	return new;
end;
$$
language plpgsql;

create trigger tr_customers_before
before insert or update
on customers
for each row 
execute function tr_valid_customer();

create or replace function tr_delete_customer()
returns trigger AS $$
declare
	v_cant int;
begin
		RAISE NOTICE 'SQL_LOG: %',
      format(
        'SELECT COUNT(*) FROM orders WHERE customerid = %L',
        OLD.customerid
      );

   	select count(*) into v_cant
   	from orders
   	where customerid = old.customerid;
   	
   	if v_cant > 0 then
   		raise exception 'No se puede eliminar este cliente porque tiene pedidos asociados.';
   	end if;
   	
   	return old;
END;
$$ LANGUAGE plpgsql;

create trigger tr_customers_del
before delete
on customers
for each row 
execute function tr_delete_customer();

-- 4. Vista de Órdenes (Resuelve JOINs y monto total)
CREATE OR REPLACE VIEW vw_ordenes AS
SELECT 
    o.orderid,
    o.customerid,
    c.companyname,
    o.employeeid,
    e.firstname,
    e.lastname,
    o.orderdate,
    o.requireddate,
    o.shippeddate,
    o.shipvia,
    o.freight,
    o.shipname,
    o.shipaddress,
    o.shipcity,
    o.shipregion,
    o.shippostalcode,
    o.shipcountry
FROM orders o
INNER JOIN customers c ON o.customerid = c.customerid
INNER JOIN employees e ON o.employeeid = e.employeeid
INNER JOIN orderdetails od ON o.orderid = od.orderid
GROUP BY 
    o.orderid, o.orderdate, o.customerid, c.companyname, 
    o.employeeid, e.lastname, e.firstname;