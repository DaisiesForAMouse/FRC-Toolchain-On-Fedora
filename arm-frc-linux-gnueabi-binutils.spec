Name:           arm-frc-linux-gnueabi-binutils
Version:        2.29
Release:        1%{?dist}
Summary:        Assemble and manipulate binary and object files for FRC arm targets 

License:        GPLv3
URL:            http://sources.redhat.com/binutils
Source0:        ftp://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2

BuildRequires:      glibc, bison
Requires(post):     info
Requires(preun):    info

%description
Part of the FRC 2018 Power Up C++ tool-chain.

%prep
%setup -q -n binutils-%{version}

%build
%configure
./configure \
    --prefix=/usr \
    --infodir=/usr/arm-frc-linux-gnueabi/share/info \
    --target=arm-frc-linux-gnueabi \
    --with-sysroot=/usr/arm-frc-linux-gnueabi \
    --with-pkgversion='GNU Binutils for FRC' \
    --disable-multilib \
    --disable-nls \
    --enable-lto \
    --disable-libiberty-install \
    --enable-ld \
    --enable-gold=default \
    --enable-plugins


%define info /usr/arm-frc-linux-gnueabi/share/info
make configure-host
make

%install
%make_install

%files
%{_prefix}/arm-frc-linux-gnueabi/bin/ar
%{_prefix}/arm-frc-linux-gnueabi/bin/as
%{_prefix}/arm-frc-linux-gnueabi/bin/ld
%{_prefix}/arm-frc-linux-gnueabi/bin/ld.bfd
%{_prefix}/arm-frc-linux-gnueabi/bin/ld.gold
%{_prefix}/arm-frc-linux-gnueabi/bin/nm
%{_prefix}/arm-frc-linux-gnueabi/bin/readelf
%{_prefix}/arm-frc-linux-gnueabi/bin/objcopy
%{_prefix}/arm-frc-linux-gnueabi/bin/objdump
%{_prefix}/arm-frc-linux-gnueabi/bin/ranlib
%{_prefix}/arm-frc-linux-gnueabi/bin/strip
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.x
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xbn
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xd
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xdc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xdw
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xn
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xr
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xs
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xsc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xsw
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xu
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelf_linux_eabi.xw
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.x
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xbn
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xd
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xdc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xdw
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xn
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xr
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xs
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xsc
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xsw
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xu
%{_prefix}/arm-frc-linux-gnueabi/lib/ldscripts/armelfb_linux_eabi.xw
%{_bindir}/arm-frc-linux-gnueabi-addr2line
%{_bindir}/arm-frc-linux-gnueabi-ar
%{_bindir}/arm-frc-linux-gnueabi-as
%{_bindir}/arm-frc-linux-gnueabi-c++filt
%{_bindir}/arm-frc-linux-gnueabi-elfedit
%{_bindir}/arm-frc-linux-gnueabi-gprof
%{_bindir}/arm-frc-linux-gnueabi-ld
%{_bindir}/arm-frc-linux-gnueabi-ld.bfd
%{_bindir}/arm-frc-linux-gnueabi-ld.gold
%{_bindir}/arm-frc-linux-gnueabi-nm
%{_bindir}/arm-frc-linux-gnueabi-objcopy
%{_bindir}/arm-frc-linux-gnueabi-objdump
%{_bindir}/arm-frc-linux-gnueabi-ranlib
%{_bindir}/arm-frc-linux-gnueabi-readelf
%{_bindir}/arm-frc-linux-gnueabi-size
%{_bindir}/arm-frc-linux-gnueabi-strings
%{_bindir}/arm-frc-linux-gnueabi-strip
%{_bindir}/arm-frc-linux-gnueabi-dwp
#%%{info}/as.info.gz
#%%{info}/bfd.info.gz
#%%{info}/binutils.info.gz
#%%{info}/configure.info.gz
#%%{info}/dir
#%%{info}/gprof.info.gz
#%%{info}/ld.info.gz
#%%{info}/standards.info.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-addr2line.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-ar.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-as.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-c++filt.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-dlltool.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-elfedit.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-gprof.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-ld.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-nlmconv.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-nm.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-objcopy.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-objdump.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-ranlib.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-readelf.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-size.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-strings.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-strip.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-windmc.1.gz
%{_mandir}/man1/arm-frc-linux-gnueabi-windres.1.gz
/usr/arm-frc-linux-gnueabi/share/info/as.info
/usr/arm-frc-linux-gnueabi/share/info/bfd.info
/usr/arm-frc-linux-gnueabi/share/info/binutils.info
/usr/arm-frc-linux-gnueabi/share/info/dir
/usr/arm-frc-linux-gnueabi/share/info/gprof.info
/usr/arm-frc-linux-gnueabi/share/info/ld.info


%changelog
* Fri Jan 12 2018 David Chen <david.chen9909@gmail.com> 2.24-1 
- Initial version of the package
