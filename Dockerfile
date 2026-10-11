FROM rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

COPY app/ /app/
COPY models/ /models/

RUN mkdir -p /app/output

ENTRYPOINT ["python3", "/app/app.py"]
