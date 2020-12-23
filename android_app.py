!pip install buildozer
      
!pip install cython==0.29.19

!lsb_release -a
      
!sudo apt-get install -y \
        python3-pip \
        build-essential \
        git \
        python3 \
        python3-dev \
        ffmpeg \
        libsdl2-dev \
        libsdl2-image-dev \
        libsdl2-mixer-dev \
        libsdl2-ttf-dev \
        libportmidi-dev \
        libswscale-dev \
        libavformat-dev \
        libavcodec-dev \
        zlib1g-dev


!sudo apt-get install -y \
        libgstreamer1.0 \
        gstreamer1.0-plugins-base \
        gstreamer1.0-plugins-good
      
!sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
      
!sudo apt-get install libffi-dev
      
## From here your work starts, it will generate .spec file, follow tutorial video
      
      
!buildozer init"
      
## From here you can Build APK from \"main.py\""
      
      
!buildozer -v android debug
