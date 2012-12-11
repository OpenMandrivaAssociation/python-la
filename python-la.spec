%define	module	la
%define name	python-%{module}
%define version 0.6.0
%define	rel	1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Label the rows, columns, any dimension of your NumPy arrays
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/l/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://berkeleyanalytics.com/la/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	hdf5-devel >= 1.8
BuildRequires:	python-devel, python-sphinx
Requires:	python-numpy, python-bottleneck
Suggests:	python-scipy

%description
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and
the labels as a list of lists (one list per dimension).

You can archive larrys in HDF5 format using save and load or using a
dictionary-like interface.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
pushd doc
export PYTHONPATH=`dir -1d ../build/lib.*| head -1`
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.rst doc/build/html
%py_platsitedir/%{module}*


%changelog
* Tue Jun 26 2012 Lev Givon <lev@mandriva.org> 0.6.0-1
+ Revision: 806921
- imported package python-la

