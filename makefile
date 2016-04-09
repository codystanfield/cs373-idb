FILES :=           \
    .gitignore		 \
    .travis.yml    \
		makefile       \
		apiary.apib		 \
		IDB1.log			 \
		models.html		 \
		models.py			 \
		tests.py			 \
		UML.pdf


check:
	@not_found=0;                                 	\
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f TestOutput.tmp
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  model.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: TestOutput.tmp
	rm TestOutput.tmp

# TestOutput.tmp: tests.py
# 	coverage3 run --omit=*flask*,*sqlalchemy*,*dist-packages*,tests.py,config.py,*jinja*,*itsdangerous.py,/usr/local/lib/* tests.py >  TestOutput.tmp 2>&1
# 	coverage3 report -m              >> TestOutput.tmp
# 	cat TestOutput.tmp
# 	rm TestOutput.tmp

TestOutput.tmp: tests.py
	coverage3 run --branch tests.py > TestOutput.tmp 2>&1
	coverage3 report -m --omit='*/site-packages/*' >> TestOutput.tmp
	cat TestOutput.tmp
	# rm TestOutput.tmp

models.html: models.py
	pydoc -w models

IDB1.log:
	git log > IDB1.log
