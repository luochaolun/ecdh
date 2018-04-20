yum -y install gcc gcc-c++

g++ -std=c++11 -fPIC -c -o ecdh.o ecdh.cpp -I./
ar cr libecdh.a ecdh.o
g++ -std=c++11 -shared -fPIC -o libecdh_x64.so -Wl,--whole-archive libecdh.a libssl.a libcrypto.a -Wl,--no-whole-archive

Linux下OpenSSL静态库编译及使用
https://www.linuxidc.com/Linux/2017-09/147117.htm

先安装perl
yum install perl
yum install cpan

或

wget http://www.cpan.org/src/5.0/perl-5.26.2.tar.gz
tar -xzf perl-5.26.2.tar.gz
cd perl-5.26.2
./Configure -des -Dprefix=$HOME/localperl
make
make test
make install

wget https://www.openssl.org/source/old/1.0.2/openssl-1.0.2k.tar.gz
tar zxf openssl-1.0.2k.tar.gz
cd openssl-1.0.2k
./config -fPIC no-shared
make

其中，-fPIC：指示生成位置无关的代码，这个选项是在把openssl生成的静态库链接到动态库的时候提示错误添加的；no-shared：指示生成静态库。
最终在当前目录下会编译出libssl.a和libcrypto.a两个库文件，在开发的时候只需要包含头件并链接这两个库就可以了。