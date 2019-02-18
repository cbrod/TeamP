CREATE OR REPLACE FUNCTION public.closespots()
 RETURNS TABLE(area text, blockname text, spacecount double precision, key double precision, geotag text, distance_from_su double precision)
 LANGUAGE plpgsql
AS $function$
BEGIN
return query select p48.paidparkingarea, p48.blockfacename, avg(parkingspacecount) as parkingspacecount, 
p48.sourceelementkey, p48.location as geotag,
(point(cast(trim(substring(p48.location from 8 for 8)) as float),
(cast(trim(substring(p48.location from 20 for 8)) as double precision))) 
<@> point(47.6082294,-122.317634317)) as distance
from parking_48 as p48
group by p48.paidparkingarea, p48.blockfacename, p48.sourceelementkey, geotag, distance
order by distance asc
limit 10;
            
END; $function$


CREATE OR REPLACE FUNCTION public.daytimespots(timeinhour double precision, timeinday double precision)
 RETURNS TABLE(sourceelementkey double precision, blockfacename text, sideofstreet text, parkingtimelimitcategory double precision, geolocation text, difference double precision)
 LANGUAGE plpgsql
AS $function$BEGIN
return query select p48.sourceelementkey, p48.blockfacename, p48.sideofstreet, p48.parkingtimelimitcategory,
p48.location,
ceiling(avg(p48.parkingspacecount-p48.paidoccupancy)) as difference
from parking_48 as p48
where (p48.paidparkingarea = 'Capitol Hill' 
	   or p48.paidparkingarea = 'First Hill' 
	   or p48.paidparkingarea = '12th Avenue'
	   or p48.paidparkingarea = 'Pike-Pine')
and p48.paidoccupancy != 0
and date_part('hour', p48.occupancydatetime) = timeInHour
and EXTRACT (DOW from p48.occupancydatetime) = timeInDay
group by p48.sourceelementkey, p48.blockfacename, p48.sideofstreet, p48.parkingtimelimitcategory,p48.location
order by difference Desc
limit 10;
            
END; $function$


"CREATE OR REPLACE FUNCTION public.top10spots(timeinhour double precision)
 RETURNS TABLE(sourceelementkey double precision, blockfacename text, sideofstreet text, parkingtimelimitcategory double precision, geotag text, difference double precision)
 LANGUAGE plpgsql
AS $function$BEGIN

return query select p48.sourceelementkey, p48.blockfacename, p48.sideofstreet, p48.parkingtimelimitcategory, 
p48.location,
ceiling(avg(p48.parkingspacecount-p48.paidoccupancy)) as difference
from parking_48 as p48
where (p48.paidparkingarea = 'Capitol Hill' 
	   or p48.paidparkingarea = 'First Hill' 
	   or p48.paidparkingarea = '12th Avenue'
	   or p48.paidparkingarea = 'Pike-Pine')
and p48.paidoccupancy != 0
and date_part('hour', p48.occupancydatetime) = timeInHour
group by p48.sourceelementkey, p48.blockfacename, p48.sideofstreet, p48.parkingtimelimitcategory, p48.location
order by difference Desc
limit 10;
			
END; $function$