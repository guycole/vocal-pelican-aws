# vocal-pelican-aws
Vocal Pelican collects METAR (weather observations) from the US NOAA and stores the results in a database.  

docker build -t guycole/vocal-pelican .
docker run -it --rm --name testaroo guycole/vocal-pelican
