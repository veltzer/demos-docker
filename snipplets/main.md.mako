<%!
    import pydmt.helpers.git
    file_number = pydmt.helpers.git.count_files("exercises/**/Dockerfile") +\
	pydmt.helpers.git.count_files("examples/**/Dockerfile")
%>${"##"} How to run

* 'docker.io' must be installed and running.
* user running must be in group 'docker'.

${"##"} Number of examples

Currently there are ${file_number} examples in this repo.
