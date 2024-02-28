from book_classes import DatesLevel
from book_classes import PagesLevel

# Object 1
dune_book = DatesLevel('Dune', 'Frank Herbert', 'Science Fiction')
# Object 2
platform_book = PagesLevel('People on Platform 5', 'Clare Pooley', 'Fiction', 384)

dune_book.set_start_date(12, 5, 2023)
dune_book.set_end_date(22,8, 2023)
print(dune_book, '\n')

platform_book.set_start_date(29, 9, 2023)

platform_book.set_pages(150)
platform_book.track_progress()

print(platform_book, '\n')