pyinstaller --icon=images\journal_book.ico ^
	--windowed ^
	--add-data="images;images" ^
	-n "Dream Journaller" ^
	main.py