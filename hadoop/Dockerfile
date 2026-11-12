FROM examen_bigdata-hadoop:latest

WORKDIR /app

RUN mkdir -p /app/mapreduce /app/data

RUN echo '<?xml version="1.0"?>' > /opt/hadoop/etc/hadoop/core-site.xml && \
    echo '<configuration>' >> /opt/hadoop/etc/hadoop/core-site.xml && \
    echo '<property><name>fs.defaultFS</name><value>file:///</value></property>' >> /opt/hadoop/etc/hadoop/core-site.xml && \
    echo '</configuration>' >> /opt/hadoop/etc/hadoop/core-site.xml

RUN echo '<?xml version="1.0"?>' > /opt/hadoop/etc/hadoop/mapred-site.xml && \
    echo '<configuration>' >> /opt/hadoop/etc/hadoop/mapred-site.xml && \
    echo '<property><name>mapreduce.framework.name</name><value>local</value></property>' >> /opt/hadoop/etc/hadoop/mapred-site.xml && \
    echo '</configuration>' >> /opt/hadoop/etc/hadoop/mapred-site.xml

CMD ["/bin/bash", "-c", "/usr/sbin/sshd && tail -f /dev/null"]
