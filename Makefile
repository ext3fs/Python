CC = pyinstaller
TARGET = curr

.PHONY: install clean run

#install:
#	$(CC) --onefile --console $(TARGET).py 

#clean:
#	rm -rf $(TARGET).spec ./build ./dist ./core*

run:
	python3 $(TARGET).py  
	
clean:
	rm -rf ./__pycache__ ./core*

