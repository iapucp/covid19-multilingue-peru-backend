FROM lambci/lambda:build-python3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /var/task

RUN pip install -U pip-tools

RUN echo 'export PS1="\[\e[36m\]coronashell>\[\e[m\] "' >> /root/.bashrc

CMD ["bash"]
