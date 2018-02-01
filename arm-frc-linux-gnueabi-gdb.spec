Name:           arm-frc-linux-gnueabi-gdb
Version:        8.0
Release:        1%{?dist}
Summary:        The GNU Debugger (arm-frc-linux-gnueabi)

License:        GPLv3
URL:            http://www.gnu.org/software/gdb/
Source0:        ftp://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz

%description
The GNU Debugger for use in the 2018 FRC C++ toolchain.

%prep
%setup -q -n gdb-%{version}

%define procs 10
%build
%configure
./configure \
    --prefix=/usr \
    --program-prefix=arm-frc-linux-gnueabi- \
    --target=${_target} \
    --infodir=/usr/arm-frc-linux-gnueabi/share/info \
    --disable-nls \
    --with-python=/usr/bin/python3 \
    --with-sysroot=/usr/${_target} \
    --enable-lto

make -j%{procs}

%install
%make_install

rm -f %{buildroot}/usr/arm-frc-linux-gnueabi/share/info/dir %{buildroot}/usr/arm-frc-linux-gnueabi/share/info/bfd.info

rm -rf %{buildroot}/usr/share/man/*
rm -rf %{buildroot}/usr/include/*

%files
%{_prefix}/arm-frc-linux-gnueabi/share/info/annotate.info
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-1
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-2
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-3
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-4
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-5
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-6
%{_prefix}/arm-frc-linux-gnueabi/share/info/gdb.info-7
%{_prefix}/arm-frc-linux-gnueabi/share/info/stabs.info
%{_prefix}/bin/arm-frc-linux-gnueabi-gcore
%{_prefix}/bin/arm-frc-linux-gnueabi-gdb
%{_prefix}/bin/arm-frc-linux-gnueabi-gdbserver
%{_prefix}/lib/debug/usr/bin/arm-frc-linux-gnueabi-gdb-8.0-1.fc27.x86_64.debug
%{_prefix}/lib/debug/usr/bin/arm-frc-linux-gnueabi-gdbserver-8.0-1.fc27.x86_64.debug
%{_prefix}/lib/debug/usr/lib/libinproctrace.so-8.0-1.fc27.x86_64.debug
%{_prefix}/lib/libbfd.a
%{_prefix}/lib/libbfd.la
%{_prefix}/lib/libinproctrace.so
%{_prefix}/lib/libopcodes.a
%{_prefix}/lib/libopcodes.la
%{_prefix}/share/gdb/python/gdb/FrameDecorator.py
%{_prefix}/share/gdb/python/gdb/FrameDecorator.pyc
%{_prefix}/share/gdb/python/gdb/FrameDecorator.pyo
%{_prefix}/share/gdb/python/gdb/FrameIterator.py
%{_prefix}/share/gdb/python/gdb/FrameIterator.pyc
%{_prefix}/share/gdb/python/gdb/FrameIterator.pyo
%{_prefix}/share/gdb/python/gdb/__init__.py
%{_prefix}/share/gdb/python/gdb/__init__.pyc
%{_prefix}/share/gdb/python/gdb/__init__.pyo
%{_prefix}/share/gdb/python/gdb/command/__init__.py
%{_prefix}/share/gdb/python/gdb/command/__init__.pyc
%{_prefix}/share/gdb/python/gdb/command/__init__.pyo
%{_prefix}/share/gdb/python/gdb/command/explore.py
%{_prefix}/share/gdb/python/gdb/command/explore.pyc
%{_prefix}/share/gdb/python/gdb/command/explore.pyo
%{_prefix}/share/gdb/python/gdb/command/frame_filters.py
%{_prefix}/share/gdb/python/gdb/command/frame_filters.pyc
%{_prefix}/share/gdb/python/gdb/command/frame_filters.pyo
%{_prefix}/share/gdb/python/gdb/command/pretty_printers.py
%{_prefix}/share/gdb/python/gdb/command/pretty_printers.pyc
%{_prefix}/share/gdb/python/gdb/command/pretty_printers.pyo
%{_prefix}/share/gdb/python/gdb/command/prompt.py
%{_prefix}/share/gdb/python/gdb/command/prompt.pyc
%{_prefix}/share/gdb/python/gdb/command/prompt.pyo
%{_prefix}/share/gdb/python/gdb/command/type_printers.py
%{_prefix}/share/gdb/python/gdb/command/type_printers.pyc
%{_prefix}/share/gdb/python/gdb/command/type_printers.pyo
%{_prefix}/share/gdb/python/gdb/command/unwinders.py
%{_prefix}/share/gdb/python/gdb/command/unwinders.pyc
%{_prefix}/share/gdb/python/gdb/command/unwinders.pyo
%{_prefix}/share/gdb/python/gdb/command/xmethods.py
%{_prefix}/share/gdb/python/gdb/command/xmethods.pyc
%{_prefix}/share/gdb/python/gdb/command/xmethods.pyo
%{_prefix}/share/gdb/python/gdb/frames.py
%{_prefix}/share/gdb/python/gdb/frames.pyc
%{_prefix}/share/gdb/python/gdb/frames.pyo
%{_prefix}/share/gdb/python/gdb/function/__init__.py
%{_prefix}/share/gdb/python/gdb/function/__init__.pyc
%{_prefix}/share/gdb/python/gdb/function/__init__.pyo
%{_prefix}/share/gdb/python/gdb/function/as_string.py
%{_prefix}/share/gdb/python/gdb/function/as_string.pyc
%{_prefix}/share/gdb/python/gdb/function/as_string.pyo
%{_prefix}/share/gdb/python/gdb/function/caller_is.py
%{_prefix}/share/gdb/python/gdb/function/caller_is.pyc
%{_prefix}/share/gdb/python/gdb/function/caller_is.pyo
%{_prefix}/share/gdb/python/gdb/function/strfns.py
%{_prefix}/share/gdb/python/gdb/function/strfns.pyc
%{_prefix}/share/gdb/python/gdb/function/strfns.pyo
%{_prefix}/share/gdb/python/gdb/printer/__init__.py
%{_prefix}/share/gdb/python/gdb/printer/__init__.pyc
%{_prefix}/share/gdb/python/gdb/printer/__init__.pyo
%{_prefix}/share/gdb/python/gdb/printer/bound_registers.py
%{_prefix}/share/gdb/python/gdb/printer/bound_registers.pyc
%{_prefix}/share/gdb/python/gdb/printer/bound_registers.pyo
%{_prefix}/share/gdb/python/gdb/printing.py
%{_prefix}/share/gdb/python/gdb/printing.pyc
%{_prefix}/share/gdb/python/gdb/printing.pyo
%{_prefix}/share/gdb/python/gdb/prompt.py
%{_prefix}/share/gdb/python/gdb/prompt.pyc
%{_prefix}/share/gdb/python/gdb/prompt.pyo
%{_prefix}/share/gdb/python/gdb/types.py
%{_prefix}/share/gdb/python/gdb/types.pyc
%{_prefix}/share/gdb/python/gdb/types.pyo
%{_prefix}/share/gdb/python/gdb/unwinder.py
%{_prefix}/share/gdb/python/gdb/unwinder.pyc
%{_prefix}/share/gdb/python/gdb/unwinder.pyo
%{_prefix}/share/gdb/python/gdb/xmethod.py
%{_prefix}/share/gdb/python/gdb/xmethod.pyc
%{_prefix}/share/gdb/python/gdb/xmethod.pyo
%{_prefix}/share/gdb/syscalls/aarch64-linux.xml
%{_prefix}/share/gdb/syscalls/amd64-linux.xml
%{_prefix}/share/gdb/syscalls/arm-linux.xml
%{_prefix}/share/gdb/syscalls/freebsd.xml
%{_prefix}/share/gdb/syscalls/gdb-syscalls.dtd
%{_prefix}/share/gdb/syscalls/i386-linux.xml
%{_prefix}/share/gdb/syscalls/mips-n32-linux.xml
%{_prefix}/share/gdb/syscalls/mips-n64-linux.xml
%{_prefix}/share/gdb/syscalls/mips-o32-linux.xml
%{_prefix}/share/gdb/syscalls/ppc-linux.xml
%{_prefix}/share/gdb/syscalls/ppc64-linux.xml
%{_prefix}/share/gdb/syscalls/s390-linux.xml
%{_prefix}/share/gdb/syscalls/s390x-linux.xml
%{_prefix}/share/gdb/syscalls/sparc-linux.xml
%{_prefix}/share/gdb/syscalls/sparc64-linux.xml
%{_prefix}/share/gdb/system-gdbinit/elinos.py
%{_prefix}/share/gdb/system-gdbinit/elinos.pyc
%{_prefix}/share/gdb/system-gdbinit/elinos.pyo
%{_prefix}/share/gdb/system-gdbinit/wrs-linux.py
%{_prefix}/share/gdb/system-gdbinit/wrs-linux.pyc
%{_prefix}/share/gdb/system-gdbinit/wrs-linux.pyo

%changelog
* Fri Jan 12 2018 David Chen <david.chen9909@gmail.com> 2.24-1 
- Initial version of the package
