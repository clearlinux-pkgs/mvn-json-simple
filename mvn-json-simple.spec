#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-json-simple
Version  : tag.1.1.1
Release  : 3
URL      : https://github.com/fangyidong/json-simple/archive/tag_release_1_1_1.tar.gz
Source0  : https://github.com/fangyidong/json-simple/archive/tag_release_1_1_1.tar.gz
Source1  : https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar
Source2  : https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.pom
Source3  : https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar
Source4  : https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-json-simple-data = %{version}-%{release}
Requires: mvn-json-simple-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Please visit:
http://code.google.com/p/json-simple/

%package data
Summary: data components for the mvn-json-simple package.
Group: Data

%description data
data components for the mvn-json-simple package.


%package license
Summary: license components for the mvn-json-simple package.
Group: Default

%description license
license components for the mvn-json-simple package.


%prep
%setup -q -n json-simple-tag_release_1_1_1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-json-simple
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-json-simple/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar
/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.pom
/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar
/usr/share/java/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-json-simple/LICENSE.txt
