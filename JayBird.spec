Summary:	Firebird Class 4 JCA-JDBC driver
Name:		JayBird
Version:	2.1.0
Release:	%mkrel 5
License:	LGPL
Group:		Development/Java
URL:		https://www.firebirdsql.org/
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/firebird/%{name}-%{version}-src.tar.bz2
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-nodeps
BuildRequires:	ant-trax
BuildRequires:	docbook-style-xsl
BuildRequires:	java-gcj-compat-devel
BuildRequires:	java-rpmbuild >= 0:1.6
BuildRequires:	xalan-j2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
JayBird is JCA/JDBC driver suite to connect to Firebird database server.
Historically Borland opened sources of type 3 JDBC driver called InterClient.
However due to some inherent limitations of Firebird client library it was
decided that type 3 driver is a dead end, and Firebird team developed pure Java
implementation of wire protocol. This implementation became basis for JayBird,
pure Java driver for Firebird relational database.

This driver is based on both the new JCA standard for application server
connections to enterprise information systems and the well known JDBC standard.
The JCA standard specifies an architecture in which an application server can
cooperate with a driver so that the application server manages transactions,
security, and resource pooling, and the driver supplies only the connection
functionality. While similar to the JDBC 2 XADataSource idea, the JCA
specification is considerably clearer on the division of responsibility between
the application server and driver.
 
%package manual
Summary:	Manual for %{name}
Group:		Development/Java

%description manual
Documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src

# GNU Java doesn't support this option
sed -i '/extdirs="${module.thirdparty}"/d' ./build/dist.xml

%build
./build.sh compile dist

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_javadir}
#%{__mkdir_p} %{buildroot}%{_javadir}/jar
%{__cp} -a output/lib/*.jar %{buildroot}%{_javadir}/
#%{__rm} -rf output/lib/*.rar
#%{__mkdir_p} %{buildroot}/examples
#%{__cp} -a output/examples/*.class %{buildroot}/examples/
#%{__cp} -a output/etc/faq.html %{buildroot}
#%{__cp} -a output/etc/FAQ.txt %{buildroot}
#%{__cp} -a output/etc/JDBC20_conformance.html %{buildroot}
#%{__cp} -a output/etc/release_notes.html %{buildroot}
%{__mkdir_p} %{buildroot}%{_libdir}
%{__cp} -a native/libjaybird21.so %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_docdir}
%{__cp} -a output/docs/* %{buildroot}%{_docdir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc output/etc/faq.html
%doc output/etc/FAQ.txt
%doc output/etc/JDBC20_conformance.html
%doc output/etc/release_notes.html
%doc output/examples/
%{_javadir}
%{_libdir}

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/*
