FROM swernst/locusts:latest

COPY ./run.py /run.py

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["python3.6", "-u", "/run.py"]
