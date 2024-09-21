class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book has been deleted")

b=Book('python rocks','jose',200)

#print(b.author)

#print(b.pages)

#print(b.title)

#print(len(b))

#print(str(b))

print(b)
