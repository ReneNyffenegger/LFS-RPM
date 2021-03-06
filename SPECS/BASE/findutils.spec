Summary:	The Findutils package contains programs to find files.
Name:		findutils
Version:	4.6.0
Release:	1
License:	Any
URL:		Any
Group:		LFS/Base
Vendor:		Octothorpe
Distribution:	LFS-8.1
ExclusiveArch:	x86_64
Requires:	filesystem
Source0:	http://ftp.gnu.org/gnu/findutils/%{name}-%{version}.tar.gz
%description
	The Findutils package contains programs to find files. These programs
	are provided to recursively search through a directory tree and to 
	create, maintain, and search a database (often faster than the recursive 
	find, but unreliable if the database has not been recently updated). 
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	./configure \
		--prefix=%{_prefix} \
		--localstatedir=/var/lib/locate
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
	install -vdm 755 %{buildroot}/bin
	mv -v %{buildroot}/usr/bin/find %{buildroot}/bin
	sed -i 's|find:=${BINDIR}|find:=/bin|' %{buildroot}/usr/bin/updatedb
	#	Copy license/copying file 
	#	install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
	#	Create file list
	rm  %{buildroot}/usr/share/info/dir
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
%files -f filelist.rpm
	%defattr(-,root,root)
	%dir /var/lib/locate
%changelog
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> -1
-	Initial build.	First version