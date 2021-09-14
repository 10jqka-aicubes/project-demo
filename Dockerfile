FROM hub-dev.hexin.cn/jupyterhub/nvidia_cuda:py37-cuda100-ubuntu18.04-v2

COPY ./ /home/jovyan/project-demo

RUN cd /home/jovyan/project-demo  && \
    python -m pip install -r requirements.txt 