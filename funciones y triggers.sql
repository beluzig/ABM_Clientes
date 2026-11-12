//Funcion ABM 
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
	
	if length(id)>5 then
		raise exception 'El ID del cliente no puede tenear más de 5 caracteres.';
	end if;
	
	if accion = 'A' then
		insert into customers(customerid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax)
		values(id,nombre,contacto,titulo,direccion,ciudad,p_region,codp,pais,telefono,p_fax);
		return 'El cliente se creo correctamente.';
	elsif accion = 'M' then
		update customers
		SET companyname = nombre, contactname = contacto, contacttitle = titulo, address = direccion, city = ciudad, region = p_region, postalcode = codp, country = pais, phone = telefono, fax = p_fax
		where customerid = id;
		return 'Cliente actualizado exitosamente.';
	elsif accion = 'B' then
		delete from customers
		where customerid = id;
		return 'Cliente eliminado correctamente';
	end if;
end;
$$
language plpgsql;

drop function fn_abm_cli

create or replace function tr_valid_customer()
returns trigger as $$ 
begin

	if new.customerid is null or trim(new.customerid)='' then
		raise exception 'El ID es obligatorio';
	end if;
	
	if new.companyname is null or trim(new.companyname) = '' then
		raise exception 'El nombre de la empresa es obligatorio';
	end if;
	
	if new.customerid !~ '^[a-zA-Z]+$' then
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

DROP TRIGGER IF EXISTS tr_customers_del ON customers;
drop function tr_delete_customer