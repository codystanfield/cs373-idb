# This was easier than getting make test to run from a different directory

test: TestOutput.tmp

TestOutput.tmp: tests.py
	coverage3 run --omit=*flask*,*sqlalchemy*,*dist-packages*,tests.py,config.py,*jinja*,*itsdangerous.py,/usr/local/lib/* --branch tests.py >  TestOutput.tmp 2>&1
	coverage3 report -m              >> TestOutput.tmp
	cat TestOutput.tmp
	rm TestOutput.tmp
