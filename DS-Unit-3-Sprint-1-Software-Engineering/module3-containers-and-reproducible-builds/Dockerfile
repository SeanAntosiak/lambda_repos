FROM debian

# makes logging/io working with Docker
ENV PYTHONUNBUFFERED=1

# Gets basic Python dependencies
RUN apt-get update
RUN apt-get install python3-pip curl nano -y
RUN pip3 install pandas numpy
RUN pip3 install -i https://test.pypi.org/simple/ lambdataSeanAntosiak 
RUN python3 -c "import lambdataSeanAntosiak; print('Package Imported!')" 
