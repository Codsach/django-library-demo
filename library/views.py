from django.shortcuts import render, redirect

# Fake database
books = []

def book_list(request):
    return render(request, 'library/list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        books.append({
            'id': len(books),
            'title': request.POST['title'],
            'author': request.POST['author']
        })
        return redirect('book_list')
    return render(request, 'library/add.html')

def edit_book(request, id):
    book = books[id]
    if request.method == 'POST':
        book['title'] = request.POST['title']
        book['author'] = request.POST['author']
        return redirect('book_list')
    return render(request, 'library/edit.html', {'book': book, 'id': id})

def delete_book(request, id):
    books.pop(id)
    return redirect('book_list')
