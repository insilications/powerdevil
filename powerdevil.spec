#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : powerdevil
Version  : 5.23.5
Release  : 305
URL      : https://download.kde.org/stable/plasma/5.23.5/powerdevil-5.23.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.5/powerdevil-5.23.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: powerdevil-data = %{version}-%{release}
Requires: powerdevil-lib = %{version}-%{release}
Requires: powerdevil-libexec = %{version}-%{release}
Requires: powerdevil-locales = %{version}-%{release}
Requires: powerdevil-services = %{version}-%{release}
BuildRequires : bluez-qt-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kded-dev
BuildRequires : kdoctools-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : kirigami2-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kwayland-dev
BuildRequires : libcap-dev
BuildRequires : libkscreen-dev
BuildRequires : mesa-dev
BuildRequires : networkmanager-qt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(xcb)
BuildRequires : plasma-workspace-dev
BuildRequires : qtbase-dev
BuildRequires : systemd-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the powerdevil package.
Group: Data

%description data
data components for the powerdevil package.


%package dev
Summary: dev components for the powerdevil package.
Group: Development
Requires: powerdevil-lib = %{version}-%{release}
Requires: powerdevil-data = %{version}-%{release}
Provides: powerdevil-devel = %{version}-%{release}
Requires: powerdevil = %{version}-%{release}

%description dev
dev components for the powerdevil package.


%package doc
Summary: doc components for the powerdevil package.
Group: Documentation

%description doc
doc components for the powerdevil package.


%package lib
Summary: lib components for the powerdevil package.
Group: Libraries
Requires: powerdevil-data = %{version}-%{release}
Requires: powerdevil-libexec = %{version}-%{release}

%description lib
lib components for the powerdevil package.


%package libexec
Summary: libexec components for the powerdevil package.
Group: Default

%description libexec
libexec components for the powerdevil package.


%package locales
Summary: locales components for the powerdevil package.
Group: Default

%description locales
locales components for the powerdevil package.


%package services
Summary: services components for the powerdevil package.
Group: Systemd services

%description services
services components for the powerdevil package.


%prep
%setup -q -n powerdevil-5.23.5
cd %{_builddir}/powerdevil-5.23.5

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643435594
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
%cmake .. -DKDE_INSTALL_CONFDIR=/usr/share/xdg \
-DBUILD_TESTING:BOOL=OFF
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1643435594
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
pushd clr-build
%make_install
popd
%find_lang libpowerdevilcommonconfig
%find_lang powerdevil
%find_lang powerdevilactivitiesconfig
%find_lang powerdevilglobalconfig
%find_lang powerdevilprofilesconfig

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
/usr/share/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
/usr/share/knotifications5/powerdevil.notifyrc
/usr/share/kservices5/powerdevilactivitiesconfig.desktop
/usr/share/kservices5/powerdevilbrightnesscontrolaction.desktop
/usr/share/kservices5/powerdevildimdisplayaction.desktop
/usr/share/kservices5/powerdevildpmsaction.desktop
/usr/share/kservices5/powerdevilglobalconfig.desktop
/usr/share/kservices5/powerdevilhandlebuttoneventsaction.desktop
/usr/share/kservices5/powerdevilkeyboardbrightnesscontrolaction.desktop
/usr/share/kservices5/powerdevilpowerprofileaction.desktop
/usr/share/kservices5/powerdevilprofilesconfig.desktop
/usr/share/kservices5/powerdevilrunscriptaction.desktop
/usr/share/kservices5/powerdevilsuspendsessionaction.desktop
/usr/share/kservices5/powerdevilwirelesspowersavingaction.desktop
/usr/share/kservicetypes5/powerdevilaction.desktop
/usr/share/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
/usr/share/qlogging-categories5/powerdevil.categories
/usr/share/xdg/autostart/powerdevil.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/libpowerdevilconfigcommonprivate.so
/usr/lib64/libpowerdevilcore.so
/usr/lib64/libpowerdevilui.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/de/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/en/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/es/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/et/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/fr/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/id/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/it/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/nl/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/pt/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/ru/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/sv/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/uk/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/powerdevil/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpowerdevilconfigcommonprivate.so.5
/usr/lib64/libpowerdevilconfigcommonprivate.so.5.23.5
/usr/lib64/libpowerdevilcore.so.2
/usr/lib64/libpowerdevilcore.so.5.23.5
/usr/lib64/libpowerdevilui.so.5
/usr/lib64/libpowerdevilui.so.5.23.5
/usr/lib64/qt5/plugins/kcm_powerdevilactivitiesconfig.so
/usr/lib64/qt5/plugins/kcm_powerdevilglobalconfig.so
/usr/lib64/qt5/plugins/kcm_powerdevilprofilesconfig.so
/usr/lib64/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
/usr/lib64/qt5/plugins/powerdevilbrightnesscontrolaction_config.so
/usr/lib64/qt5/plugins/powerdevildimdisplayaction_config.so
/usr/lib64/qt5/plugins/powerdevildpmsaction_config.so
/usr/lib64/qt5/plugins/powerdevilhandlebuttoneventsaction_config.so
/usr/lib64/qt5/plugins/powerdevilkeyboardbrightnesscontrolaction_config.so
/usr/lib64/qt5/plugins/powerdevilpowerprofileaction_config.so
/usr/lib64/qt5/plugins/powerdevilrunscriptaction_config.so
/usr/lib64/qt5/plugins/powerdevilsuspendsessionaction_config.so
/usr/lib64/qt5/plugins/powerdevilwirelesspowersavingaction_config.so

%files libexec
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/backlighthelper
/usr/lib64/libexec/kauth/chargethresholdhelper
/usr/lib64/libexec/kauth/discretegpuhelper
/usr/lib64/libexec/org_kde_powerdevil

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-powerdevil.service

%files locales -f libpowerdevilcommonconfig.lang -f powerdevil.lang -f powerdevilactivitiesconfig.lang -f powerdevilglobalconfig.lang -f powerdevilprofilesconfig.lang
%defattr(-,root,root,-)
