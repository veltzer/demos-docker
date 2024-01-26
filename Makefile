##########
# params #
##########
# do you want to see the commands executed ?
DO_MKDBG:=0
# do you want to check bash syntax?
DO_SHELLCHECK:=1
# do you want dependency on the Makefile itself ?
DO_ALLDEP:=1
# do you want to check python syntax?
DO_SYNTAX:=1
# do you want to lint python files using pylit?
DO_PYLINT:=1
# do you want to lint python files using flake8?
DO_FLAKE8:=1
# do you want to lint python files using mypy?
DO_MYPY:=1
# do you want to run mdl on md files?
DO_MD_MDL:=1
# do spell check on all?
DO_MD_ASPELL:=1

########
# code #
########
ALL:=

# silent stuff
ifeq ($(DO_MKDBG),1)
Q:=
# we are not silent in this branch
else # DO_MKDBG
Q:=@
#.SILENT:
endif # DO_MKDBG

# dependency on the makefile itself
ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif # DO_ALLDEP

ALL_SH:=$(shell find . -type f -name "*.sh" -and -not -path "./.venv/*" -and -not -path "./config/*" -printf "%P\n")
ALL_SHELLCHECK:=$(addprefix out/, $(addsuffix .shellcheck, $(ALL_SH)))

ALL_PY:=$(shell find . -type f -name "*.py" -and -not -path "./.venv/*" -and -not -path "./config/*" -printf "%P\n")
ALL_SYNTAX:=$(addprefix out/,$(addsuffix .syntax, $(basename $(ALL_PY))))
ALL_PYLINT:=$(addprefix out/,$(addsuffix .pylint, $(basename $(ALL_PY))))
ALL_FLAKE8:=$(addprefix out/,$(addsuffix .flake8, $(basename $(ALL_PY))))
ALL_MYPY:=$(addprefix out/,$(addsuffix .mypy, $(basename $(ALL_PY))))

MD_SRC:=$(shell find examples exercises -type f -and -name "*.md")
MD_BAS:=$(basename $(MD_SRC))
MD_ASPELL:=$(addprefix out/,$(addsuffix .aspell,$(MD_BAS)))
MD_MDL:=$(addprefix out/,$(addsuffix .mdl,$(MD_BAS)))

ifeq ($(DO_SHELLCHECK),1)
ALL+=$(ALL_SHELLCHECK)
endif # DO_SHELLCHECK

ifeq ($(DO_SYNTAX),1)
ALL+=$(ALL_SYNTAX)
endif # DO_SYNTAX

ifeq ($(DO_PYLINT),1)
ALL+=$(ALL_PYLINT)
endif # DO_PYLINT

ifeq ($(DO_FLAKE8),1)
ALL+=$(ALL_FLAKE8)
endif # DO_FLAKE8

ifeq ($(DO_MYPY),1)
ALL+=$(ALL_MYPY)
endif # DO_MYPY

ifeq ($(DO_MD_MDL),1)
ALL+=$(MD_MDL)
endif # DO_MD_MDL

ifeq ($(DO_MD_ASPELL),1)
ALL+=$(MD_ASPELL)
endif # DO_MD_ASPELL

#########
# rules #
#########
.PHONY: all
all: $(ALL)
	@true

.PHONY: debug
debug:
	$(info doing [$@])
	$(info ALL_SH is $(ALL_SH))
	$(info ALL_SHELLCHECK is $(ALL_SHELLCHECK))
	$(info ALL_PY is $(ALL_PY))
	$(info MD_SRC is $(MD_SRC))
	$(info MD_BAS is $(MD_BAS))
	$(info MD_ASPELL is $(MD_ASPELL))
	$(info MD_MDL is $(MD_MDL))

.PHONY: first_line_stats
first_line_stats:
	$(info doing [$@])
	$(Q)head -1 -q $(ALL_SH) | sort -u

.PHONY: clean
clean:
	$(info doing [$@])
	$(Q)rm -f $(ALL)

.PHONY: clean_hard
clean_hard:
	$(info doing [$@])
	$(Q)git clean -qffxd

.PHONY: check
check:
	$(Q)git grep -l latest -- **/*.sh || true
# $(info doing [$@])
# git grep latest -- **/Dockerfile
# git grep latest

############
# patterns #
############
$(MD_ASPELL): out/%.aspell: %.md .aspell.conf .aspell.en.prepl .aspell.en.pws
	$(info doing [$@])
	$(Q)aspell --conf-dir=. --conf=.aspell.conf list < $< | pymakehelper error_on_print sort -u
	$(Q)pymakehelper touch_mkdir $@
$(ALL_SHELLCHECK): out/%.shellcheck: % .shellcheckrc
	$(info doing [$@])
	$(Q)shellcheck --shell=bash --external-sources --source-path="$$HOME" $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_SYNTAX): out/%.syntax: %.py
	$(info doing [$@])
	$(Q)pycmdtools python_check_syntax $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_PYLINT): out/%.pylint: %.py
	$(info doing [$@])
	$(Q)python -m pylint --reports=n --score=n $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_FLAKE8): out/%.flake8: %.py
	$(info doing [$@])
	$(Q)python -m flake8 $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_MYPY): out/%.mypy: %.py
	$(info doing [$@])
	$(Q)pymakehelper only_print_on_error mypy $<
	$(Q)pymakehelper touch_mkdir $@
$(MD_MDL): out/%.mdl: %.md .mdlrc .mdl.style.rb
	$(info doing [$@])
	$(Q)GEM_HOME=gems gems/bin/mdl $<
	$(Q)mkdir -p $(dir $@)
	$(Q)touch $@
