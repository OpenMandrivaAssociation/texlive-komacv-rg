Name:		texlive-komacv-rg
Version:	49064
Release:	2
Summary:	LaTeX packages that aid in creating CVs based on the komacv class and creating related documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/komacv-rg
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The komacv-rg bundle provides packages that aid in creating CVs
based on the komacv class and creating related documents, such
as cover letters and cover sheets for job applications.
Concretely, the bundle consists of three packages:
komacv-addons, komacv-lco, and komacv-multilang. komacv-addons
is a small collection of add-ons and fixes for the komacv
class; komacv-lco enables the use of letter class options from
scrlttr2 also in komacv-based and other non-scrlttr2-based
documents; komacv-multilang enables the provisioning of CVs in
multiple languages and the selection of a language via babel or
polyglossia.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/komacv-rg
%{_texmfdistdir}/tex/latex/komacv-rg
%doc %{_texmfdistdir}/doc/latex/komacv-rg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
