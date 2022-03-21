docker container run -it\
                     -p 5000:5000\
                     --mount type=bind,src=$(pwd)/src,dst=/app/src\
                     python-flask:latest
