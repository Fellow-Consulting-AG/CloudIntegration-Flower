docker build -t dajor85570/flower-dev -f Dockerfile_DEV . 
docker tag dajor85570/flower-dev registry.digitalocean.com/sumup2srvdesk/flower-dev
docker push registry.digitalocean.com/sumup2srvdesk/flower-dev

