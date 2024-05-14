import pytest
from many_to_many import Author, Book, Contract

class TestManyToMany:
    """Test suite for the many_to_many module"""

    @classmethod
    def setup_class(cls):
        """Reset any global state before running the test suite"""
        Contract.all = []

    def test_book_init(self):
        """Test Book class initialization with title"""
        book = Book("Title")
        assert book.title == "Title"

    def test_author_init(self):
        """Test Author class initialization with name"""
        author = Author("Name")
        assert author.name == "Name"

    def test_contract_init(self):
        """Test Contract class initialization with author, book, date, royalties"""
        author = Author("Name")
        book = Book("Title")
        date = '01/01/2001'
        royalties = 40000
        contract = Contract(author, book, date, royalties)
        assert contract.author == author
        assert contract.book == book
        assert contract.date == date
        assert contract.royalties == royalties

    def test_contract_validates_author(self):
        """Test Contract class validation of author type"""
        book = Book("Title")
        date = '01/01/2001'
        royalties = 40000
        with pytest.raises(Exception):
            Contract("Author", book, date, royalties)

    # Add more test methods as needed

    def test_contract_contracts_by_date(self):
        """Test Contract class contracts_by_date() sorts contracts by date"""
        author1 = Author("Name 1")
        author2 = Author("Name 2")
        book1 = Book("Title 1")
        book2 = Book("Title 2")
        book3 = Book("Title 3")
        book4 = Book("Title 4")
        contract1 = Contract(author1, book1, "02/01/2001", 10)
        contract2 = Contract(author1, book2, "01/01/2001", 20)
        contract3 = Contract(author1, book3, "03/01/2001", 30)
        contract4 = Contract(author2, book4, "01/01/2001", 40)

        sorted_contracts = Contract.contracts_by_date('01/01/2001')
        assert sorted_contracts == [contract2, contract4]
