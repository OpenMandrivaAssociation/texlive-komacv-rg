%global tl_name komacv-rg
%global tl_revision 49064

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.2
Release:	%{tl_revision}.1
Summary:	LaTeX packages that aid in creating CVs based on the komacv class and creatin...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/komacv-rg
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv-rg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The komacv-rg bundle provides packages that aid in creating CVs based on
the komacv class and creating related documents, such as cover letters
and cover sheets for job applications. Concretely, the bundle consists
of three packages: komacv-addons, komacv-lco, and komacv-multilang.
komacv-addons is a small collection of add-ons and fixes for the komacv
class; komacv-lco enables the use of letter class options from scrlttr2
also in komacv-based and other non-scrlttr2-based documents; komacv-
multilang enables the provisioning of CVs in multiple languages and the
selection of a language via babel or polyglossia.

