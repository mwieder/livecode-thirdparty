NAME=libpcre
TYPE=archive

include ../../rules/environment.linux.makefile

# TDZ-2013-09-29 : [[ libpcre update ]]

SOURCES=\
	pcre_byte_order.c pcre_chartables.c pcre_compile.c pcre_config.c pcre_dfa_exec.c \
	pcre_exec.c pcre_fullinfo.c pcre_get.c pcre_globals.c pcre_info_fullinfo.c \
	pcre_jit_compile.c pcre_maketables.c pcre_newline.c pcre_ord2utf8.c pcre_refcount.c \
	pcre_string_utils.c pcre_study.c pcre_tables.c pcre_ucd.c pcre_valid_utf8.c \
	pcre_version.c pcre_xclass.c

CUSTOM_DEFINES=

CUSTOM_INCLUDES=./src

CUSTOM_CCFLAGS=

include ../../rules/archive.linux.makefile
