FROM debian
MAINTAINER Guy Cole "guycole@gmail.com"
RUN apt-get update -y
RUN apt-get install -y wget
#RUN apt-get install -y 
#COPY entrypoint.sh /
#ENTRYPOINT ["/entrypoint.sh"]
#CMD ["curl"]
