FROM swernst/locusts:latest

COPY ./scripts /scripts
COPY ./run.py /run.py

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["python3.6", "-u", "/run.py"]
