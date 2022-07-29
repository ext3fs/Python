CC = pyinstaller
MAIN = main

.PHONY: install clean run

#install:
#	$(CC) --onefile --console $(MAIN).py 

#clean:
#	rm -rf $(MAIN).spec ./build ./dist ./core*

run:
	python3 $(MAIN).py  
	
clean:
	rm -rf ./__pycache__ ./core*

