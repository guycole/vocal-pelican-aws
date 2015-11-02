# vocal-pelican-aws
Vocal Pelican collects METAR (weather observations) from the US NOAA and stores the results in AWS DynamoDB.

Collection, parse and load are performed w/python and boto.

## aws
* Weather observations are stored in DynamoDb table VocalPelicanObservation
* Primary key is "CompositeKey" (concatenation of weather station ID and observation time)
* Global secondary index of "StationId" (hash) and ObservationTime (number) where station id looks like 'KRBL' and observation time is epoch seconds

## docker
```
Available at https://hub.docker.com/r/guycole/vocal-pelican/
```

```
docker build -t guycole/vocal-pelican .
docker run -e AWS_ACCESS_KEY=<secret> -e AWS_SECRET_KEY=<secret> -e AWS_DEFAULT_REGION=<region> -it --rm guycole/vocal-pelican
```
