FROM tesseractshadow/tesseract4re
LABEL maintainer="sjuarez@csticorp.biz"

#RUN apt-get update && apt-get install -y \
#    software-properties-common
#RUN add-apt-repository universe
#RUN apt-get update && apt-get install -y \
RUN apt-get update && apt-get install -y \
    python3.4 \
    python3-pip
RUN apt-get install python3-dev

#ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
COPY . /tesseract
WORKDIR /tesseract
RUN pip3 install Flask
RUN pip3 install fitz
RUN pip3 install --upgrade pip
RUN pip3 install pymupdf
RUN pip3 install --upgrade pymupdf
RUN pip3 install tools
#RUN pip3 install pymupdf
RUN pip3 install Pillow==6.2.2
RUN pip3 install pytesseract
RUN mkdir png
RUN mkdir pdfs2process
RUN mkdir pdfs2delete
RUN mkdir static

RUN pip3 install -r /tesseract/requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["/tesseract/server.py"]