FROM elek/spark-base:2.1.0
ENV HADOOP_CONF_DIR /opt/livy/conf
ENV CONF_DIR /opt/livy/conf
ENV SPARK_HOME /opt/spark
ENV SPARK_CONF_DIR /opt/livy/conf
ADD url ./
RUN wget `cat url` -O livy.zip && unzip livy.zip && rm livy.zip && mv livy* livy 
ADD defaults/* defaults/
RUN mkdir /opt/livy/logs
CMD ["/opt/livy/bin/livy-server"]

